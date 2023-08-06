# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['zeno']

package_data = \
{'': ['*'], 'zeno': ['frontend/*', 'frontend/build/*']}

install_requires = \
['fastapi>=0.75.0,<0.76.0',
 'modin>=0.13.2,<0.14.0',
 'pandas-stubs>=1.2.0,<2.0.0',
 'pandas>=1.4.0,<2.0.0',
 'pyarrow>=7.0.0,<8.0.0',
 'ray>=1.11.0,<2.0.0',
 'uvicorn>=0.17.5,<0.18.0',
 'watchdog>=2.1.6,<3.0.0',
 'websockets>=10.2,<11.0']

entry_points = \
{'console_scripts': ['zeno = zeno.runner:main']}

setup_kwargs = {
    'name': 'zenoml',
    'version': '0.0.1',
    'description': 'Behavioral Testing for Machine Learning',
    'long_description': '# Zeno - Behavioral testing of AI/ML\n\n![Github Actions CI tests](https://github.com/cabreraalex/zeno/actions/workflows/test.yml/badge.svg)\n[![code style black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)\n[![codecov](https://codecov.io/gh/cabreraalex/zeno/branch/main/graph/badge.svg?token=XPT8R98H8J)](https://codecov.io/gh/cabreraalex/zeno)\n\n## Quick Start\n\nInstall the Zeno package from PyPI:\n\n```\npip install zenoml\n```\n\n### [Follow the documentation to get started](https://cabreraalex.github.io/zeno/intro.html)\n\n## Development\n\n### Environment\n\nPlease install [`Poetry`](https://python-poetry.org/docs/master/#installing-with-the-official-installer) and use VSCode as your editor.\n\n### Install\n\nSuggest setting poetry to install the virtual env locally, which VSCode can use directly:\n\n`poetry config virtualenvs.in-project true`\n\n`poetry install`\n\n### Running\n\n`poetry run zeno`\n\n### Formatting and Linting\n\n`make`\n\n### Testing\n\n`make test`\n\n### Build Docs\n\n`make book`\n\n### Build\n\n`make build`\n\n### Publish\n\n`make publish`\n',
    'author': 'Ángel Alexander Cabrera',
    'author_email': 'alex.cabrera@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/cabreraalex/zeno',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
