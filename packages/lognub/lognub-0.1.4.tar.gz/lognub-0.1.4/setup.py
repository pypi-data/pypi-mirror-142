# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['lognub', 'lognub.captures', 'lognub.handles', 'lognub.patchers']

package_data = \
{'': ['*']}

install_requires = \
['loguru>=0.5.3,<0.6.0']

setup_kwargs = {
    'name': 'lognub',
    'version': '0.1.4',
    'description': 'Dumb Log Utlity for personal use',
    'long_description': '# LogNub\n\n[![BuildAndTest](https://github.com/ChethanUK/lognub/actions/workflows/build_test.yml/badge.svg)](https://github.com/ChethanUK/lognub/actions/workflows/build_test.yml) [![PreCommitChecks](https://github.com/ChethanUK/lognub/actions/workflows/code_quality_lint_checkers.yml/badge.svg)](https://github.com/ChethanUK/lognub/actions/workflows/code_quality_lint_checkers.yml) [![CodeQL](https://github.com/ChethanUK/lognub/actions/workflows/codeql-analysis.yml/badge.svg)](https://github.com/ChethanUK/lognub/actions/workflows/codeql-analysis.yml) [![codecov](https://codecov.io/gh/ChethanUK/lognub/branch/master/graph/badge.svg?token=HRI9hoE5ru)](https://codecov.io/gh/ChethanUK/lognub)\n\nLoguru utility package\n\n## TODO\n\n1. Move logwrap [on top of loguru] extension out as a seperate package.\n1. Add Test containers for [amundsen](https://www.amundsen.io/amundsen/), etc..\n\n## Getting Started\n\n1. Setup [SDKMAN](#setup-sdkman)\n1. Setup [Java](#setup-java)\n1. Setup [Apache Spark](#setup-apache-spark)\n1. Install [Poetry](#poetry)\n1. Install Pre-commit and [follow instruction in here](PreCommit.MD)\n1. Run [tests locally](#running-tests-locally)\n\n### Setup SDKMAN\n\nSDKMAN is a tool for managing parallel Versions of multiple Software Development Kits on any Unix based\nsystem. It provides a convenient command line interface for installing, switching, removing and listing\nCandidates. SDKMAN! installs smoothly on Mac OSX, Linux, WSL, Cygwin, etc... Support Bash and ZSH shells. See\ndocumentation on the [SDKMAN! website](https://sdkman.io).\n\nOpen your favourite terminal and enter the following:\n\n```bash\n$ curl -s https://get.sdkman.io | bash\nIf the environment needs tweaking for SDKMAN to be installed,\nthe installer will prompt you accordingly and ask you to restart.\n\nNext, open a new terminal or enter:\n\n$ source "$HOME/.sdkman/bin/sdkman-init.sh"\n\nLastly, run the following code snippet to ensure that installation succeeded:\n\n$ sdk version\n```\n\n### Setup Java\n\nInstall Java Now open favourite terminal and enter the following:\n\n```bash\nList the AdoptOpenJDK OpenJDK versions\n$ sdk list java\n\nInstall the Java 8:\n$ sdk install java 8.0.292.hs-adpt\n\nSet Java 8 as default Java Version:\n$ sdk default java 8.0.292.hs-adpt\n\nOR \n\nTo install For Java 11\n$ sdk install java 11.0.10.hs-adpt\n```\n\n### Setup Apache Spark\n\nInstall Java Now open favourite terminal and enter the following:\n\n```bash\nList the Apache Spark versions:\n$ sdk list spark\n\nTo install For Spark 3\n$ sdk install spark 3.0.2\n\nTo install For Spark 3.1\n$ sdk install spark 3.0.2\n```\n\n## Install PyEnv and Python 3.8\n\nEither install pyenv via brew or github:\n```bash\nbrew install pyenv\n\nThen setup in zshrc:\necho \'eval "$(pyenv init --path)"\' >> ~/.zprofile\n\necho \'eval "$(pyenv init -)"\' >> ~/.zshrc\n```\n\nThen Install Python 3.8:\n\n```bash\npyenv install 3.8.11\n```\n\ncd allocator project directory:\n```bash\n# Checkout git repo of iAllocator\ncd dse-iAllocator \ncd customer/allocator\n# Now set default python version as 3.8.11\npyenv local 3.8.11\n# Verify python version\npython -V\nPython 3.8.11\n```\n\n## Create VirtualENV\n\nCreate local venv inside allocator project:\n```bash\ncd dse-iAllocator [Repo directory] \ncd customer/allocator\n# Create virtualenv locally \npython -m venv .venv\n# Verify activate file exists \nls -G .venv/bin\n# Activate virtual env python\nsource .venv/bin/activate\n```\n\nVerify virtual env and python is working and .venv is activated:\n\n```bash\nwhich python\n# should end with {$ROOT_DIR}.venv/bin/python\nwhich pip\n# should end with {$ROOT_DIR}.venv/bin/pip\n```\n\n### Poetry\n\nPoetry [Commands](https://python-poetry.org/docs/cli/#search) - Python package management tool\n\nInstall Poetry:\n\nInstall poetry using brew\n```bash\nbrew install poetry\n```\n\nOR\n\nFollow instructions for Linux: [here](https://python-poetry.org/docs/#osx--linux--bashonwindows-install-instructions)\n\n```bash\n# For osx / linux / bash on windows install:\ncurl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -\n```\n\nInstall the dep packages:\n\nNOTE: Make sure you are connected to OpenVPN[since some are internal packages - catalog_client] \n```bash\nInstall psycopg2 binary via PIP:\n$ pip install psycopg2-binary==2.9.1\n\nInstall rest of packages via Poetry:\n\n$ poetry install\n\n# --tree: List the dependencies as a tree.\n# --latest (-l): Show the latest version.\n# --outdated (-o): Show the latest version but only for packages that are outdated.\npoetry show -o\n\nTo update any package:\n#$ poetry update pandas\n```\n\n## Running Tests Locally\n\nTake a look at tests in `tests/dataquality` and `tests/jobs`\n\n```bash\n$ poetry run pytest\nRan 95 tests in 96.95s\n```\n\nThats it, ENV is setup\n\nNOTE: Loguru Wrap Package extracted from different internal package\nNOTE: It\'s just curated stuff, Created for personal usage.',
    'author': 'ChethanUK',
    'author_email': 'chethanuk@outlook.com',
    'maintainer': 'ChethanUK',
    'maintainer_email': 'chethanuk@outlook.com',
    'url': 'https://github.com/ChethanUK/',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6.2,<4.0',
}


setup(**setup_kwargs)
