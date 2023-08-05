from __future__ import annotations

import asyncio
import concurrent.futures
import contextvars
import functools
import inspect
import os
import threading
import weakref
from collections import deque
from concurrent.futures.thread import ThreadPoolExecutor
from types import TracebackType
from typing import (
    Any,
    AsyncGenerator,
    AsyncIterator,
    Awaitable,
    Callable,
    Coroutine,
    Deque,
    Generic,
    Iterator,
    List,
    MutableSet,
    Optional,
    Protocol,
    Type,
    TypeVar,
    Union,
    cast,
    runtime_checkable,
)

from ..utils.inspect import ensure_coroutine

__all__ = [
    "AsyncEventIterator",
    "AsyncEvent",
    "async_event",
    "AsyncTaskingEventIterator",
    "AsyncTaskingEvent",
    "async_tasking_event_iterator",
    "async_tasking_event",
    "AsyncThreadingEventIterator",
    "AsyncThreadingEvent",
    "async_threading_event_iterator",
    "async_threading_event",
    "check_canceled",
    "run_in_thread",
    "run_coroutine_in_thread",
    "Lock",
    "create_sub_task",
    "FutureInfo",
]

_T = TypeVar("_T")

_TResult = TypeVar("_TResult")
_TCallable = TypeVar("_TCallable", bound=Callable[..., Any])


class AsyncEventResultIteratorBase(Generic[_TCallable, _TResult]):
    def __init__(self) -> None:
        self._lock = threading.RLock()

        self._listeners: MutableSet[weakref.ref[Any]] = set()
        self._loop = asyncio.get_event_loop()

    def add(self, callback: _TCallable) -> None:
        def remove_listener(ref: Any) -> None:
            with self._lock:
                self._listeners.remove(ref)

        with self._lock:
            if inspect.ismethod(callback):
                self._listeners.add(weakref.WeakMethod(callback, remove_listener))
            else:
                self._listeners.add(weakref.ref(callback, remove_listener))

    def remove(self, callback: _TCallable) -> None:
        with self._lock:
            try:
                if inspect.ismethod(callback):
                    self._listeners.remove(weakref.WeakMethod(callback))
                else:
                    self._listeners.remove(weakref.ref(callback))
            except KeyError:
                pass

    def __contains__(self, obj: Any) -> bool:
        if inspect.ismethod(obj):
            return weakref.WeakMethod(obj) in self._listeners
        else:
            return weakref.ref(obj) in self._listeners

    def __len__(self) -> int:
        return len(self._listeners)

    def __iter__(self) -> Iterator[_TCallable]:
        for r in self._listeners:
            c = r()
            if c is not None:
                yield c

    async def __aiter__(self) -> AsyncIterator[_TCallable]:
        for r in self.__iter__():
            yield r

    async def _notify(
        self, *args: Any, callback_filter: Optional[Callable[[_TCallable], bool]] = None, **kwargs: Any
    ) -> AsyncIterator[_TResult]:

        for method in filter(
            lambda x: callback_filter(x) if callback_filter is not None else True,
            set(self),
        ):
            result = method(*args, **kwargs)
            if inspect.isawaitable(result):
                result = await result

            yield result


class AsyncEventIterator(AsyncEventResultIteratorBase[_TCallable, _TResult]):
    def __call__(self, *args: Any, **kwargs: Any) -> AsyncIterator[_TResult]:
        return self._notify(*args, **kwargs)


class AsyncEvent(AsyncEventResultIteratorBase[_TCallable, _TResult]):
    async def __call__(self, *args: Any, **kwargs: Any) -> List[_TResult]:
        return [a async for a in self._notify(*args, **kwargs)]


_TEvent = TypeVar("_TEvent")


class AsyncEventDescriptorBase(Generic[_TCallable, _TResult, _TEvent]):
    def __init__(
        self, _func: _TCallable, factory: Callable[..., _TEvent], *factory_args: Any, **factory_kwargs: Any
    ) -> None:
        self._func = _func
        self.__factory = factory
        self.__factory_args = factory_args
        self.__factory_kwargs = factory_kwargs
        self._owner: Optional[Any] = None
        self._owner_name: Optional[str] = None

    def __set_name__(self, owner: Any, name: str) -> None:
        self._owner = owner
        self._owner_name = name

    def __get__(self, obj: Any, objtype: Type[Any]) -> _TEvent:
        if obj is None:
            return self  # type: ignore

        name = f"__async_event_{self._func.__name__}__"
        if not hasattr(obj, name):
            setattr(obj, name, self.__factory(*self.__factory_args, **self.__factory_kwargs))

        return cast("_TEvent", getattr(obj, name))


class async_event_iterator(  # noqa: N801
    AsyncEventDescriptorBase[_TCallable, Any, AsyncEventIterator[_TCallable, Any]]
):
    def __init__(self, _func: _TCallable) -> None:
        super().__init__(_func, AsyncEventIterator[_TCallable, _TResult])


class async_event(AsyncEventDescriptorBase[_TCallable, Any, AsyncEvent[_TCallable, Any]]):  # noqa: N801
    def __init__(self, _func: _TCallable) -> None:
        super().__init__(_func, AsyncEvent[_TCallable, _TResult])


_F = TypeVar("_F", bound=Callable[..., Any])


def threaded(enabled: bool = True) -> Callable[[_F], _F]:
    def decorator(func: _F) -> _F:
        setattr(func, "__threaded__", enabled)
        return func

    return decorator


@runtime_checkable
class HasThreaded(Protocol):
    __threaded__: bool


class AsyncTaskingEventResultIteratorBase(AsyncEventResultIteratorBase[_TCallable, _TResult]):
    def __init__(self, *, task_name_prefix: Optional[str] = None) -> None:
        super().__init__()
        self._task_name_prefix = task_name_prefix or type(self).__qualname__

    async def _notify(  # type: ignore
        self,
        *args: Any,
        result_callback: Optional[Callable[[Optional[_TResult], Optional[BaseException]], Any]] = None,
        return_exceptions: Optional[bool] = True,
        callback_filter: Optional[Callable[[_TCallable], bool]] = None,
        **kwargs: Any,
    ) -> AsyncIterator[Union[_TResult, BaseException]]:
        def _done(f: asyncio.Future[_TResult]) -> None:
            if result_callback is not None:
                try:
                    result_callback(f.result(), f.exception())
                except (SystemExit, KeyboardInterrupt):
                    raise
                except BaseException as e:
                    result_callback(None, e)

        awaitables: List[asyncio.Future[_TResult]] = []
        for method in filter(
            lambda x: callback_filter(x) if callback_filter is not None else True,
            set(self),
        ):
            if method is not None:
                if isinstance(method, HasThreaded) and cast(HasThreaded, method).__threaded__:
                    future = run_coroutine_in_thread(ensure_coroutine(method), *args, **kwargs)
                else:
                    future = create_sub_task(ensure_coroutine(method)(*args, **kwargs))

                awaitables.append(future)

                if result_callback is not None:
                    future.add_done_callback(_done)

        for a in asyncio.as_completed(awaitables):
            try:
                yield await a
            except asyncio.CancelledError:
                for f in awaitables:
                    if not f.done():
                        f.cancel()
                        try:
                            yield await a
                        except (SystemExit, KeyboardInterrupt):
                            raise
                        except BaseException:
                            pass

                raise
            except (SystemExit, KeyboardInterrupt):
                raise
            except BaseException as e:
                if return_exceptions:
                    yield e
                else:
                    raise


class AsyncTaskingEventIterator(AsyncTaskingEventResultIteratorBase[_TCallable, _TResult]):
    def __call__(self, *args: Any, **kwargs: Any) -> AsyncIterator[Union[_TResult, BaseException]]:
        return self._notify(*args, **kwargs)


def _get_name_prefix(descriptor: AsyncEventDescriptorBase[Any, Any, Any]) -> str:
    if descriptor._owner is None:
        return type(descriptor).__qualname__

    return f"{descriptor._owner.__qualname__}.{descriptor._owner_name}"


class AsyncTaskingEvent(AsyncTaskingEventResultIteratorBase[_TCallable, _TResult]):
    async def __call__(self, *args: Any, **kwargs: Any) -> List[Union[_TResult, BaseException]]:
        return [a async for a in self._notify(*args, **kwargs)]


class AsyncThreadingEventResultIteratorBase(AsyncEventResultIteratorBase[_TCallable, _TResult]):
    __executor: Optional[ThreadPoolExecutor] = None

    def __init__(self, *, thread_name_prefix: Optional[str] = None) -> None:
        super().__init__()
        self.__executor = None
        self.__thread_name_prefix = thread_name_prefix or type(self).__qualname__

    def __del__(self) -> None:
        if self.__executor:
            self.__executor.shutdown(False)

    def _run_in_asyncio_thread(
        self,
        executor: ThreadPoolExecutor,
        coro: Union[asyncio.Future[_TResult], Awaitable[_TResult]],
        method_name: Optional[str] = None,
    ) -> asyncio.Future[_TResult]:
        def run(loop: asyncio.AbstractEventLoop) -> None:
            if method_name is not None:
                threading.current_thread().name = (
                    self.__thread_name_prefix() if callable(self.__thread_name_prefix) else self.__thread_name_prefix
                ) + f"->{method_name}(...)"

            asyncio.set_event_loop(loop)
            try:
                loop.run_forever()
            finally:
                loop.close()

        loop = asyncio.new_event_loop()

        # loop.set_debug(True)

        executor.submit(run, loop)

        result = asyncio.wrap_future(asyncio.run_coroutine_threadsafe(coro, loop=loop))

        def stop_loop(t: asyncio.Future[_TResult]) -> None:
            async def loop_stop() -> bool:
                loop.stop()
                return True

            asyncio.run_coroutine_threadsafe(loop_stop(), loop=loop)

        result.add_done_callback(stop_loop)
        return result

    async def _notify(  # type: ignore
        self,
        *args: Any,
        result_callback: Optional[Callable[[Optional[_TResult], Optional[BaseException]], Any]] = None,
        executor: Optional[ThreadPoolExecutor] = None,
        return_exceptions: Optional[bool] = True,
        callback_filter: Optional[Callable[[_TCallable], bool]] = None,
        **kwargs: Any,
    ) -> AsyncGenerator[Union[_TResult, BaseException], None]:
        def _done(f: asyncio.Future[_TResult]) -> None:
            if result_callback is not None:
                try:
                    result_callback(f.result(), f.exception())
                except (SystemExit, KeyboardInterrupt):
                    raise
                except BaseException as e:
                    result_callback(None, e)

        if executor is None:
            if AsyncThreadingEventResultIteratorBase.__executor is None:
                AsyncThreadingEventResultIteratorBase.__executor = ThreadPoolExecutor(
                    thread_name_prefix=self.__thread_name_prefix()
                    if callable(self.__thread_name_prefix)
                    else self.__thread_name_prefix
                )
            executor = AsyncThreadingEventResultIteratorBase.__executor

        awaitables: List[asyncio.Future[_TResult]] = []
        for method in filter(
            lambda x: callback_filter(x) if callback_filter is not None else True,
            set(self),
        ):
            if method is not None:
                future = self._run_in_asyncio_thread(
                    executor,
                    ensure_coroutine(method)(*args, **kwargs),
                    method.__qualname__,
                )
                if result_callback is not None:
                    future.add_done_callback(_done)
                awaitables.append(future)

        for a in asyncio.as_completed(awaitables):
            try:
                yield await a
            except asyncio.CancelledError:
                for f in awaitables:
                    if not f.done():
                        f.cancel()
                        try:
                            yield await a
                        except (SystemExit, KeyboardInterrupt):
                            raise
                        except BaseException:
                            pass
                raise
            except (SystemExit, KeyboardInterrupt):
                raise
            except BaseException as e:
                if return_exceptions:
                    yield e
                else:
                    raise


class AsyncThreadingEventIterator(AsyncThreadingEventResultIteratorBase[_TCallable, _TResult]):
    def __call__(self, *args: Any, **kwargs: Any) -> AsyncIterator[Union[_TResult, BaseException]]:
        return self._notify(*args, **kwargs)


class async_threading_event_iterator(  # noqa: N801
    AsyncEventDescriptorBase[_TCallable, Any, AsyncThreadingEventIterator[_TCallable, Any]]
):
    def __init__(self, _func: _TCallable) -> None:
        super().__init__(
            _func, AsyncThreadingEventIterator[_TCallable, Any], thread_name_prefix=lambda: _get_name_prefix(self)
        )


class AsyncThreadingEvent(AsyncThreadingEventResultIteratorBase[_TCallable, _TResult]):
    async def __call__(self, *args: Any, **kwargs: Any) -> List[Union[_TResult, BaseException]]:
        return [a async for a in self._notify(*args, **kwargs)]


class async_threading_event(  # noqa: N801
    AsyncEventDescriptorBase[_TCallable, Any, AsyncThreadingEvent[_TCallable, Any]]
):
    def __init__(self, _func: _TCallable) -> None:
        super().__init__(_func, AsyncThreadingEvent[_TCallable, Any], thread_name_prefix=lambda: _get_name_prefix(self))


class async_tasking_event_iterator(  # noqa: N801
    AsyncEventDescriptorBase[_TCallable, Any, AsyncTaskingEventIterator[_TCallable, Any]]
):
    def __init__(self, _func: _TCallable) -> None:
        super().__init__(
            _func, AsyncTaskingEventIterator[_TCallable, Any], task_name_prefix=lambda: _get_name_prefix(self)
        )


class async_tasking_event(AsyncEventDescriptorBase[_TCallable, Any, AsyncTaskingEvent[_TCallable, Any]]):  # noqa: N801
    def __init__(self, _func: _TCallable) -> None:
        super().__init__(_func, AsyncTaskingEvent[_TCallable, Any], task_name_prefix=lambda: _get_name_prefix(self))


async def check_canceled() -> bool:
    await asyncio.sleep(0)

    return True


def check_canceled_sync() -> bool:
    info = get_current_future_info()
    if info is not None and info.canceled():
        raise asyncio.CancelledError()
    return True


THREADPOOL_POOL_MAX_WORKERS = None

__tread_pool_executor: Optional[ThreadPoolExecutor] = None


def run_in_thread(func: Callable[..., _T], /, *args: Any, **kwargs: Any) -> asyncio.Future[_T]:
    global __tread_pool_executor
    loop = asyncio.get_running_loop()
    ctx = contextvars.copy_context()
    func_call = functools.partial(ctx.run, func, *args, **kwargs)

    if __tread_pool_executor is None:
        __tread_pool_executor = ThreadPoolExecutor(
            max_workers=(
                int(s)
                if (s := os.environ.get("ROBOT_THREADPOOL_POOL_MAX_WORKERS", None)) and s.isnumeric()
                else THREADPOOL_POOL_MAX_WORKERS
            )
        )

    return cast("asyncio.Future[_T]", loop.run_in_executor(__tread_pool_executor, cast(Callable[..., _T], func_call)))


def run_coroutine_in_thread(
    coro: Callable[..., Coroutine[Any, Any, _T]], *args: Any, **kwargs: Any
) -> asyncio.Future[_T]:
    callback_added_event = Event()
    inner_task: Optional[asyncio.Task[_T]] = None
    canceled = False
    result: Optional[asyncio.Future[_T]] = None

    async def create_inner_task() -> _T:
        nonlocal inner_task

        ct = asyncio.current_task()

        old_name = threading.current_thread().getName()
        threading.current_thread().setName(coro.__qualname__)
        try:
            await callback_added_event.wait()

            if ct is not None and result is not None:
                _running_tasks[result].children.add(ct)

            inner_task = create_sub_task(coro(*args, **kwargs))

            if canceled:
                inner_task.cancel()

            return await inner_task
        finally:
            threading.current_thread().setName(old_name)

    def run() -> _T:
        return asyncio.run(create_inner_task())

    cti = get_current_future_info()
    result = run_in_thread(run)

    _running_tasks[result] = FutureInfo(result)
    if cti is not None:
        cti.children.add(result)

    def done(task: asyncio.Future[_T]) -> None:
        nonlocal canceled

        canceled = task.cancelled()

        if task.cancelled() and inner_task is not None and not inner_task.done():
            inner_task._loop.call_soon_threadsafe(inner_task.cancel)

    result.add_done_callback(done)

    callback_added_event.set()

    return result


class Event:
    """Thread safe version of an async Event"""

    def __init__(self) -> None:
        self._waiters: Deque[asyncio.Future[Any]] = deque()
        self._value = False
        self._lock = threading.RLock()

    def __repr__(self) -> str:
        res = super().__repr__()
        extra = "set" if self._value else "unset"
        if self._waiters:
            extra = f"{extra}, waiters:{len(self._waiters)}"
        return f"<{res[1:-1]} [{extra}]>"

    def is_set(self) -> bool:
        return self._value

    def set(self) -> None:
        if not self._value:
            self._value = True

            with self._lock:
                for fut in self._waiters:
                    if not fut.done():
                        if fut._loop == asyncio.get_running_loop():
                            fut.set_result(True)
                        else:
                            fut._loop.call_soon_threadsafe(fut.set_result, True)

    def clear(self) -> None:
        self._value = False

    async def wait(self) -> bool:
        if self._value:
            return True

        with self._lock:
            fut = create_sub_future()
            self._waiters.append(fut)
        try:
            await fut
            return True
        finally:
            with self._lock:
                self._waiters.remove(fut)


class Lock:
    """Threadsafe version of an async Lock."""

    def __init__(self) -> None:
        self._waiters: Optional[Deque[asyncio.Future[Any]]] = None
        self._locked = False
        self._lock = threading.RLock()

    async def __aenter__(self) -> None:
        await self.acquire()

    async def __aexit__(
        self, exc_type: Optional[Type[BaseException]], exc_val: Optional[BaseException], exc_tb: Optional[TracebackType]
    ) -> None:
        self.release()

    def __repr__(self) -> str:
        res = super().__repr__()
        extra = "locked" if self._locked else "unlocked"
        if self._waiters:
            extra = f"{extra}, waiters:{len(self._waiters)}"
        return f"<{res[1:-1]} [{extra}]>"

    def locked(self) -> bool:
        return self._locked

    async def acquire(self) -> bool:

        with self._lock:
            if not self._locked and (self._waiters is None or all(w.cancelled() for w in self._waiters)):
                self._locked = True
                return True

        if self._waiters is None:
            self._waiters = deque()
        fut = create_sub_future()
        with self._lock:
            self._waiters.append(fut)

        try:
            try:
                await fut
            finally:
                self._waiters.remove(fut)
        except asyncio.CancelledError:
            if not self._locked:
                self._wake_up_first()
            raise

        with self._lock:
            self._locked = True

        return True

    def release(self) -> None:
        if self._locked:
            with self._lock:
                self._locked = False
            self._wake_up_first()
        else:
            raise RuntimeError("Lock is not acquired.")

    def _wake_up_first(self) -> None:
        if not self._waiters:
            return
        try:
            fut = next(iter(self._waiters))
        except StopIteration:
            return

        if not fut.done():
            if fut._loop == asyncio.get_running_loop():
                fut.set_result(True)
            else:
                fut._loop.call_soon_threadsafe(fut.set_result, True)


class FutureInfo:
    def __init__(self, future: asyncio.Future[Any]) -> None:
        self.task: weakref.ref[asyncio.Future[Any]] = weakref.ref(future)
        self.children: weakref.WeakSet[asyncio.Future[Any]] = weakref.WeakSet()

        future.add_done_callback(self._done)

    def _done(self, future: asyncio.Future[Any]) -> None:
        if future.cancelled():
            for t in self.children.copy():
                if not t.done() and not t.cancelled():

                    if t._loop == asyncio.get_running_loop():
                        t.cancel()
                    else:
                        t._loop.call_soon_threadsafe(t.cancel)

    def canceled(self) -> bool:
        task = self.task()
        if task is not None and task.cancelled():
            return True
        return False


_running_tasks: weakref.WeakKeyDictionary[asyncio.Future[Any], FutureInfo] = weakref.WeakKeyDictionary()


def get_current_future_info() -> Optional[FutureInfo]:
    ct = asyncio.current_task()

    if ct is None:
        return None

    if ct not in _running_tasks:
        _running_tasks[ct] = FutureInfo(ct)

    return _running_tasks[ct]


def create_sub_task(coro: Awaitable[_T], *, name: Optional[str] = None) -> asyncio.Task[_T]:

    ct = get_current_future_info()

    result = asyncio.create_task(coro, name=name)

    if ct is not None:
        ct.children.add(result)

    _running_tasks[result] = FutureInfo(result)
    return result


def create_sub_future(loop: Optional[asyncio.AbstractEventLoop] = None) -> asyncio.Future[Any]:

    ct = get_current_future_info()

    if loop is None:
        loop = asyncio.get_running_loop()

    result = loop.create_future()

    _running_tasks[result] = FutureInfo(result)

    if ct is not None:
        ct.children.add(result)

    return result


class _FutureHolder(Generic[_T]):
    def __init__(self, cfuture: concurrent.futures.Future[_T]):
        self.cfuture = cfuture
        self.afuture = wrap_sub_future(cfuture)


def spawn_coroutine_from_thread(
    func: Callable[..., Coroutine[Any, Any, _T]],
    *args: Any,
    loop: Optional[asyncio.AbstractEventLoop] = None,
    **kwargs: Any,
) -> concurrent.futures.Future[_T]:
    if loop is None:
        loop = asyncio.get_running_loop()

    result = _FutureHolder(asyncio.run_coroutine_threadsafe(func(*args), loop))
    return result.cfuture


def run_coroutine_from_thread(
    func: Callable[..., Coroutine[Any, Any, _T]],
    *args: Any,
    loop: Optional[asyncio.AbstractEventLoop] = None,
    **kwargs: Any,
) -> _T:
    if loop is None:
        loop = asyncio.get_running_loop()

    result = _FutureHolder(asyncio.run_coroutine_threadsafe(func(*args), loop))

    return result.cfuture.result()


def run_coroutine_from_thread_as_future_async(
    func: Callable[..., Coroutine[Any, Any, _T]],
    *args: Any,
    loop: Optional[asyncio.AbstractEventLoop] = None,
    **kwargs: Any,
) -> asyncio.Future[_T]:
    if loop is None:
        loop = asyncio.get_running_loop()

    return wrap_sub_future(asyncio.run_coroutine_threadsafe(func(*args, **kwargs), loop))


async def run_coroutine_from_thread_async(
    func: Callable[..., Coroutine[Any, Any, _T]],
    *args: Any,
    loop: Optional[asyncio.AbstractEventLoop] = None,
    **kwargs: Any,
) -> _T:
    if loop is None:
        loop = asyncio.get_running_loop()

    return await run_coroutine_from_thread_as_future_async(func, *args, loop=loop, **kwargs)


def wrap_sub_future(
    future: Union[asyncio.Future[_T], concurrent.futures.Future[_T]],
    *,
    loop: Optional[asyncio.AbstractEventLoop] = None,
) -> asyncio.Future[_T]:
    result = asyncio.wrap_future(future, loop=loop)
    ci = get_current_future_info()
    if ci is not None:
        ci.children.add(result)
    return result
