# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['robotcode',
 'robotcode.debugger',
 'robotcode.debugger.launcher',
 'robotcode.debugger.modifiers',
 'robotcode.jsonrpc2',
 'robotcode.language_server',
 'robotcode.language_server.common',
 'robotcode.language_server.common.parts',
 'robotcode.language_server.robotframework',
 'robotcode.language_server.robotframework.diagnostics',
 'robotcode.language_server.robotframework.parts',
 'robotcode.language_server.robotframework.utils',
 'robotcode.utils']

package_data = \
{'': ['*']}

install_requires = \
['robotframework>=4.0.0']

setup_kwargs = {
    'name': 'robotcode',
    'version': '0.7.9',
    'description': 'Language server, debugger and tools for Robot Framework',
    'long_description': '# RobotCode\n\nAn [extension](https://marketplace.visualstudio.com/VSCode) which brings support for [RobotFramework](https://robotframework.org/) to [Visual Studio Code](https://code.visualstudio.com/), including features like IntelliSense, linting, debugging, code navigation, code formatting, test explorer, find references for keywords and variables, and more!\n\n## Requirements\n\n* Python 3.8 or above\n* Robotframework 4.0 and above\n* VSCode version 1.61 and above\n\n## Installed extensions\n\nRobotCode will automatically install [Python extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python).\n\nExtensions installed through the marketplace are subject to the [Marketplace Terms of Use](https://cdn.vsassets.io/v/M146_20190123.39/_content/Microsoft-Visual-Studio-Marketplace-Terms-of-Use.pdf).\n\n## Features\n\nWith RobotCode you can edit your code with auto-completion, code navigation, syntax checking and many more.\nHere is a list of Features:\n\n- [Autocomplete and IntelliSense](#Autocomplete-and-IntelliSense)\n- [Code Navigation](#code-navigation)\n- [Diagnostics]()\n- [Diagnostics and Linting](#diagnostics-and-linting)\n- [Code Formatting](#code-formatting)\n- [Running and Debugging](#running-and-debugging)\n- [Multi-root Workspace folders](#multi-root-workspace-folders)\n- Test Explorer\n- and many more\n\n### Autocomplete and IntelliSense\n\nAutocompletion for:\n- Libraries with parameters\n- Resources,\n- Variables\n- Keywords with parameters\n- Namespaces\n\n![Autocomplete Libraries and Keywords](https://raw.githubusercontent.com/d-biehl/robotcode/v0.7.9/doc/images/autocomplete1.gif)\n\nAutocompletion supports all supported variables types\n  - local variables\n  - variables from resource files\n  - variables from variables file (.py and .yaml)\n    - static and dynamic\n  - command line variables\n  - builtin variables\n\n![Autocomplete Variables](https://raw.githubusercontent.com/d-biehl/robotcode/v0.7.9/doc/images/autocomplete2.gif)\n\n### Code Navigation\n\n- Symbols\n- Goto definitions and implementations\n  - Keywords\n  - Variables\n  - Libraries\n  - Resources\n- Find references\n  - Keywords\n  - Variables\n  - Imports\n    - Libraries\n    - Resources\n    - Variables\n- Errors and Warnings\n\n### Diagnostics and Linting\n\nRobotCode analyse your code and show diagnostics for:\n- Syntax Errors\n- Unknown keywords\n- Duplicate keywords\n- Missing libraries, resource and variable imports\n- Duplicate libraries, resource and variable imports\n- ... and many more\n\nFor most things RobotCode uses the installed RobotFramework version to parse and analyse the code, so you get the same errors as when you run it.\n\n\nGet additional code analysis with [Robocop](https://robocop.readthedocs.io/). Just install it in your python environment.\n\n### Code Formatting\n\nRobotCode can format your code with the internal RobotFramework robot.tidy tool (deprecated), but also with [Robotidy](https://robotidy.readthedocs.io/). Just install it.\n\n### Running and Debugging\n\nRobotCode supports running and debugging of RobotFramework testcases and tasks out of the box, directly from the definition of the test or suite.\n\n![Running Tests](https://raw.githubusercontent.com/d-biehl/robotcode/v0.7.9/doc/images/running_tests.gif)\n\nIn the debug console you can see all log messages of the current run and navigate to the keyword the message was written by.\n\n### Multi-root Workspace folders\n\nRobotCodes support for [Multi-root Workspaces](https://code.visualstudio.com/docs/editor/multi-root-workspaces), enables loading and editing different Robotframework projects/folders with different RobotFramework/Python environments and settings at the same time or you can share the same RobotFramework/Python environment and settings for all folders in the workspace.\n\n\n## Quick start\n\n1. [Install a supported version of Python on your system](https://code.visualstudio.com/docs/python/python-tutorial#_prerequisites)\n(note: only Python 3.8 and above are supported)\n\n2. [Install a supported version of RobotFramwork on your system](https://github.com/robotframework/robotframework/blob/master/INSTALL.rst) (note: only RobotFramework 4.0 and above are supported)\n\n3. [Install the RobotCode extension for Visual Studio Code](https://code.visualstudio.com/docs/editor/extension-gallery).\n4. Open or create a robot file and start coding! 😉\n\n\n## Setting up your environment\n\nYou can alway use your local python environment, just select the correct python interpreter in Visual Studio Code.\n\n### With pipenv\n\nThis is the simpliest way to create an running environment.\n\n- As a prerequisite you need to install [pipenv](https://pipenv.pypa.io/) like this:\n\n    ```bash\n    python -m pip install pipenv\n    ```\n\n\n- Create your project directory (robottest is just an example)\n    ```bash\n    mkdir robottest\n    cd robottest\n    ```\n- Install robotframework\n    ```bash\n    python -m pipenv install robotframework\n    ```\n- Open project in VSCode\n- Set the python interpreter to the created virtual environment\n\n\n## Customization\n\n### Editor Style\n\nYou can change some stylings for RobotFramework files in VSCode editor, independently of the current theme. (see [Customizing a Color Theme](https://code.visualstudio.com/docs/getstarted/themes#_customizing-a-color-theme))\n\nSee the difference:\n\n| Before                                                           | After                                                      |\n| ---------------------------------------------------------------- | ---------------------------------------------------------- |\n| ![Without customization](https://raw.githubusercontent.com/d-biehl/robotcode/v0.7.9/doc/images/without_customization.gif) | ![With customization](https://raw.githubusercontent.com/d-biehl/robotcode/v0.7.9/doc/images/with_customization.gif) |\n\n\nAs a template you can put the following code to your user settings of VSCode.\n\nOpen the user `settings.json` like this:\n\n<kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>P</kbd> or <kbd>F1</kbd> or <kbd>CMD</kbd> + <kbd>Shift</kbd> + <kbd>P</kbd>\n\nand then type:\n\n`Preferences: Open Settings (JSON)`\n\nput this to the `settings.json`\n\n```jsonc\n"editor.tokenColorCustomizations": {\n    "textMateRules": [\n        {\n            "scope": "variable.function.keyword-call.inner.robotframework",\n            "settings": {\n                "fontStyle": "italic"\n            }\n        },\n        {\n            "scope": "variable.function.keyword-call.robotframework",\n            "settings": {\n                //"fontStyle": "bold"\n            }\n        },\n        {\n            "scope": "entity.name.function.testcase.name.robotframework",\n            "settings": {\n                "fontStyle": "bold underline"\n            }\n        },\n        {\n            "scope": "entity.name.function.keyword.name.robotframework",\n            "settings": {\n                "fontStyle": "bold italic"\n            }\n        },\n        {\n            "scope": "variable.other.readwrite.robotframework",\n            "settings": {\n                //"fontStyle": "italic",\n            }\n        },\n        {\n            "scope": "keyword.control.import.robotframework",\n            "settings": {\n                "fontStyle": "italic"\n            }\n        },\n        {\n            "scope": "keyword.other.header.setting.robotframework",\n            "settings": {\n                "fontStyle": "bold underline"\n            }\n        },\n        {\n            "scope": "keyword.other.header.variable.robotframework",\n            "settings": {\n                "fontStyle": "bold underline"\n            }\n        },\n        {\n            "scope": "keyword.other.header.testcase.robotframework",\n            "settings": {\n                "fontStyle": "bold underline"\n            }\n        },\n        {\n            "scope": "keyword.other.header.keyword.robotframework",\n            "settings": {\n                "fontStyle": "bold underline"\n            }\n        },\n        {\n            "scope": "keyword.other.header.setting.robotframework",\n            "settings": {\n                "fontStyle": "bold underline"\n            }\n        },\n        {\n            "scope": "keyword.other.header.comment.robotframework",\n            "settings": {\n                "fontStyle": "bold italic underline"\n            }\n        },\n        {\n            "scope": "constant.character.escape.robotframework",\n            "settings": {\n                //"foreground": "#FF0000",\n            }\n        }\n    ]\n}\n\n"editor.semanticTokenColorCustomizations": {\n    "rules": {\n        "*.documentation:robotframework": {\n            "fontStyle": "italic",\n            //"foreground": "#aaaaaa"\n        }\n    }\n}\n\n```',
    'author': 'Daniel Biehl',
    'author_email': 'daniel.biehl@imbus.de',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/d-biehl/robotcode',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
