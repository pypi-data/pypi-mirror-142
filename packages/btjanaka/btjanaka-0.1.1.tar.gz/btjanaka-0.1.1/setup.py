# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['btjanaka']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'btjanaka',
    'version': '0.1.1',
    'description': 'Bryon Tjanaka in a Python package!',
    'long_description': '# btjanaka\n\nBryon Tjanaka in a Python package!\n\n|                       Source                        |                                                    PyPI                                                    |                                                                                                    CI/CD                                                                                                    |\n| :-------------------------------------------------: | :--------------------------------------------------------------------------------------------------------: | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: |\n| [GitHub](https://github.com/btjanaka/btjanaka-pypi) | [![PyPI](https://img.shields.io/pypi/v/btjanaka?style=flat&color=blue)](https://pypi.org/project/btjanaka) | [![Test and Deploy](https://github.com/btjanaka/btjanaka-pypi/workflows/Test%20and%20Deploy/badge.svg?branch=master)](https://github.com/btjanaka/btjanaka-pypi/actions?query=workflow%3A"Test+and+Deploy") |\n\n## Installation\n\nTo install from PyPI, run:\n\n```bash\npip install btjanaka\n```\n\nTo install from source, clone this repo, cd into it, and run:\n\n```bash\npip install .\n```\n\n`btjanaka` is tested on Python 3.7+. Earlier Python versions may work but are\nnot guaranteed.\n\n## Usage\n\n```python\nimport btjanaka\n\nbtjanaka.name()  # "Bryon Tjanaka"\nbtjanaka.yell()  # "BRYON TJANAKA"\nbtjanaka.website()  # "https://btjanaka.net"\nbtjanaka.website(browser=True)  # Opens the website in a browser.\n```\n',
    'author': 'Bryon Tjanaka',
    'author_email': 'bryon@btjanaka.net',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://btjanaka.net',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
