# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['rics',
 'rics._internal_support',
 'rics.cardinality',
 'rics.mapping',
 'rics.translation',
 'rics.translation.dio',
 'rics.translation.fetching',
 'rics.translation.offline',
 'rics.utility']

package_data = \
{'': ['*']}

install_requires = \
['pandas>=1.1', 'pyyaml>=5.3']

entry_points = \
{'console_scripts': ['rics = rics.cli:main']}

setup_kwargs = {
    'name': 'rics',
    'version': '0.1.0',
    'description': 'My personal little ML engineering library.',
    'long_description': '# Readme\n\n<div align="center">\n\n[![PyPI - Version](https://img.shields.io/pypi/v/rics.svg)](https://pypi.python.org/pypi/rics)\n[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/rics.svg)](https://pypi.python.org/pypi/rics)\n[![Tests](https://github.com/rsundqvist/rics/workflows/tests/badge.svg)](https://github.com/rsundqvist/rics/actions?workflow=tests)\n[![Codecov](https://codecov.io/gh/rsundqvist/rics/branch/main/graph/badge.svg)](https://codecov.io/gh/rsundqvist/rics)\n[![Read the Docs](https://readthedocs.org/projects/rics/badge/)](https://rics.readthedocs.io/)\n[![PyPI - License](https://img.shields.io/pypi/l/rics.svg)](https://pypi.python.org/pypi/rics)\n\n[![Black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)\n[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)\n\n\n</div>\n\n\nMy personal little ML engineering library.\n\n* GitHub repo: <https://github.com/rsundqvist/rics.git>\n* Documentation: <https://rics.readthedocs.io>\n* Free software: MIT\n\n## Features\n\n* TODO\n\n## Quickstart for development\n\n### Notice\nThis project uses groups for extras dependencies, which is currently a **PRERELEASE** feature (slated for `1.2`). Assuming\npoetry was installed the recommended way (see below), this can be done using:\n```bash\ncurl -sSL https://install.python-poetry.org/ | python -\npoetry self update --preview 1.2.0a2\n```\n\n### Setting up for local development\nAssumes a "modern" version of Ubuntu (guide written under `Ubuntu 20.04.2 LTS`) with basic dev dependencies installed.\nTo get started, run the following commands:\n\nInstalling the latest version of Poetry\n```bash\ncurl -sSL https://install.python-poetry.org/ | python -\n```\nThis is the way recommended by the Poetry project.\n\n```bash\ngit clone git@github.com:rsundqvist/rics.git\ncd rics\npoetry install\ninv install-hooks\n```\nThis project uses groups for extras dependencies. If installation fails, make sure that output from\n`poetry --version` is `1.2.0` or greater.\n\n### Registering the project on Codecov\n\nProbably only for forking?\n```bash\ncurl -Os https://uploader.codecov.io/latest/linux/codecov\nchmod +x codecov\n```\n\nVisit https://app.codecov.io and log in, follow instructions to link the repo and get a token for private repos.\n```bash\nCODECOV_TOKEN="<from-the-website>"\ninv coverage --fmt=xml\n./codecov -t ${CODECOV_TOKEN}\n```\n\n## Credits\n\nThis package was created with [Cookiecutter][cookiecutter] and\nthe [fedejaure/cookiecutter-modern-pypackage][cookiecutter-modern-pypackage] project template.\n\n[cookiecutter]: https://github.com/cookiecutter/cookiecutter\n\n[cookiecutter-modern-pypackage]: https://github.com/fedejaure/cookiecutter-modern-pypackage\n',
    'author': 'Richard Sundqvist',
    'author_email': 'richard.sundqvist@live.se',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/rsundqvist/rics',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<3.11',
}


setup(**setup_kwargs)
