# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['pyprojectx', 'pyprojectx.initializer', 'pyprojectx.wrapper']

package_data = \
{'': ['*']}

install_requires = \
['tomli>=2.0.1,<3.0.0', 'userpath>=1.8.0,<2.0.0', 'virtualenv>=20.13.3,<21.0.0']

entry_points = \
{'console_scripts': ['pyprojectx = pyprojectx.cli:main']}

setup_kwargs = {
    'name': 'pyprojectx',
    'version': '0.9.9',
    'description': 'Execute scripts from pyproject.toml, installing tools on-the-fly',
    'long_description': '![pyprojectx](docs/docs/assets/px.png)\n\n# Pyprojectx: All-inclusive Python Projects\n\nExecute scripts from pyproject.toml, installing tools on-the-fly\n\n## [Full documentation](https://pyprojectx.github.io)\n\n## Introduction\nPyprojectx makes it easy to create all-inclusive Python projects; no need to install any tools upfront,\nnot even Pyprojectx itself!\n\n## Feature highlights\n* Reproducible builds by treating tools and utilities as (versioned) dev-dependencies\n* No global installs, everything is stored inside your project directory (like npm\'s _node_modules_)\n* Bootstrap your entire build process with a small wrapper script (like Gradle\'s _gradlew_ wrapper)\n* Configure shortcuts for routine tasks\n* Simple configuration in _pyproject.toml_\n\nProjects can be build/tested/used immediately without explicit installation nor initialization:\n```bash\ngit clone https://github.com/pyprojectx/px-demo.git\ncd px-demo\n./pw build\n```\n![Clone and Build](https://raw.githubusercontent.com/pyprojectx/pyprojectx/main/docs/docs/assets/build.png)\n\n## Installation\nOne of the key features is that there is no need to install anything explicitly (except a Python 3.7+ interpreter).\n\n`cd` into your project directory and download the\n[wrapper scripts](https://github.com/pyprojectx/pyprojectx/releases/latest/download/wrappers.zip):\n\n**Linux/Mac**\n```bash\ncurl -LO https://github.com/pyprojectx/pyprojectx/releases/latest/download/wrappers.zip && unzip wrappers.zip && rm -f wrappers.zip\n```\n\n**Windows**\n```powershell\n(Invoke-WebRequest https://github.com/pyprojectx/pyprojectx/releases/latest/download/wrappers.zip).Content | Expand-Archive -DestinationPath .\n```\n\n## Project initialization\nInitialize a new or existing project with the _--init_ option (on Windows, replace `./pw` with `pw`):\n* `./pw --init project`: add pyprojectx example sections to an existing or new _pyproject.toml_ in the current directory.\n* `./pw --init poetry`: initialize a [Poetry](https://python-poetry.org/) project and add pyprojectx example sections to _pyproject.toml_.\n* `./pw --init pdm`: initialize a [PDM](https://pdm.fming.dev/) project and add pyprojectx example sections to _pyproject.toml_.\n\n## Configuration\nAdd the _tool.pyprojectx_ section inside _pyproject.toml_ in your project\'s root directory.\n\nEach entry has the form `tool = "pip-requirements"`, where _pip-requirements_ adheres to the\n[requirements file format](https://pip.pypa.io/en/stable/reference/requirements-file-format/).\n\nExample:\n```toml\n[tool.pyprojectx]\n# require a specific poetry version\npoetry = "poetry==1.1.13"\n# use the latest black\nisort = "isort"\n# install flake8 in combination with plugins\nflake8 = ["flake8", "flake8-black"]\n```\n\nThe _tool.pyprojectx.aliases_ section can contain optional commandline aliases in the form\n\n`alias = [@tool_key:] command`\n\nExample:\n```toml\n[tool.pyprojectx.alias]\n# convenience shortcuts\nrun = "poetry run"\ntest = "poetry run pytest"\n\n# flake8-black also contains the black script\nblack = "@flake8: black"\n\n# simple shell commands\nclean = "rm -f .coverage .pytest_cache"\n\n# when running an alias from within another alias, prefix it with `pw@`\ncheck = "pw@flake8 && pw@test"\n```\n\n## Usage\nInstead of calling the commandline of a tool directly, prefix it with `path\\to\\pw`.\n\nExamples:\n```shell\n./pw poetry add -D pytest\ncd src\n../pw black *.py\n```\n\n... or on Windows:\n```shell\npw poetry add -D pytest\ncd src\n..\\pw black *.py\n```\n\nAliases can be invoked as is or with extra arguments:\n```shell\n./pw poetry run my-script --foo bar\n# same as above, but using the run alias\n./pw run my-script --foo bar\n```\n\n## Why yet another tool?\n* As Python noob I had hard times setting up a project and building existing projects\n* There is always someone in the team having issues with his setup, either with a specific tool, with Homebrew, pipx, ...\n* Using (Poetry) dev-dependencies to install tools, impacts your production dependencies and can even lead to dependency conflicts\n* Different projects often require different versions of the same tool\n\n## Example projects\n* This project (using Poetry)\n* [px-demo](https://github.com/pyprojectx/px-demo) (using PDM)\n\n## Development\n* Build/test:\n```shell\ngit clone https://github.com/pyprojectx/pyprojectx.git\ncd pyprojectx\n./pw build\n```\n\n* Set the path to pyprojectx in the _PYPROJECTX_PACKAGE_ environment variable\n  to use your local pyprojectx copy in another project.\n```shell\n# Linux, Mac\nexport PYPROJECTX_PACKAGE=path/to/pyprojectx\n# windows\nset PYPROJECTX_PACKAGE=path/to/pyprojectx\n```\n',
    'author': 'Houbie',
    'author_email': 'ivo@houbrechts-it.be',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/pyprojectx/pyprojectx',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7',
}


setup(**setup_kwargs)
