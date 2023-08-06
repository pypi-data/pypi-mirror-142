# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['btjanaka']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'btjanaka',
    'version': '0.4.0',
    'description': 'Bryon Tjanaka in a Python package!',
    'long_description': '# btjanaka\n\nBryon Tjanaka in a Python package!\n\n|                       Source                        |                       Demo                       |                                                    PyPI                                                    |                                                                                                    CI/CD                                                                                                    |\n| :-------------------------------------------------: | :----------------------------------------------: | :--------------------------------------------------------------------------------------------------------: | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: |\n| [GitHub](https://github.com/btjanaka/btjanaka-pypi) | [Demo](https://pages.btjanaka.net/btjanaka-pypi) | [![PyPI](https://img.shields.io/pypi/v/btjanaka?style=flat&color=blue)](https://pypi.org/project/btjanaka) | [![Test and Deploy](https://github.com/btjanaka/btjanaka-pypi/workflows/Test%20and%20Deploy/badge.svg?branch=master)](https://github.com/btjanaka/btjanaka-pypi/actions?query=workflow%3A"Test+and+Deploy") |\n\n## Demo\n\nTo try the btjanaka package in the browser (courtesy of\n[Pyodide](https://pyodide.org/)), visit\n[this page](https://pages.btjanaka.net/btjanaka-pypi)\n\n## Installation\n\nTo install from PyPI, run:\n\n```bash\npip install btjanaka\n```\n\nTo install from source, clone this repo, cd into it, and run:\n\n```bash\npip install .\n```\n\n`btjanaka` is tested on Python 3.7+. Earlier Python versions may work but are\nnot guaranteed.\n\n## Usage\n\n```python\nimport btjanaka\n```\n\n### Basics\n\n```python\nbtjanaka.firstname()  # "Bryon"\nbtjanaka.lastname()  # "Tjanaka"\nbtjanaka.name()  # "Bryon Tjanaka"\nbtjanaka.yell()  # "BRYON TJANAKA"\n```\n\n### Info\n\n```python\nbtjanaka.email()  # "bryon@tjanaka.net"\nbtjanaka.github()  # "btjanaka"\nbtjanaka.linkedin()  # "btjanaka"\nbtjanaka.twitter()  # "btjanaka"\nbtjanaka.webdemo()  # "https://pages.btjanaka.net/btjanaka-pypi"\nbtjanaka.webdemo(browser=True)  # Opens the web demo in a browser.\nbtjanaka.website()  # "https://btjanaka.net"\nbtjanaka.website(browser=True)  # Opens the website in a browser.\n```\n\n### Internationalization\n\n```python\nbtjanaka.british()  # "oi Bryon!"\nbtjanaka.canadian()  # "Bryon Tjanaka eh"\nbtjanaka.chinese()  # "张学龙"\n```\n\n### Counting\n\n```python\nlen(btjanaka.name()) - len(btjanaka.yell())  # 0\nlen(btjanaka.name()) // len(btjanaka.yell())  # 1\nbtjanaka.firstname().count("o") + len(btjanaka.name()[0])  # 2\nbtjanaka.lastname().count("a")  # 3\nbtjanaka.website().count("/") + btjanaka.website().count("n")  # 4\nlen(btjanaka.firstname())  # 5\nbtjanaka.name().count("n") * btjanaka.email().count("n")  # 6\nlen(btjanaka.lastname())  # 7\nbtjanaka.canadian().index("y")**len(btjanaka.chinese())  # 8\nlen(btjanaka.british())  # 9\nlen(btjanaka.email().replace(".", "").split("@")[1])  # 10\n```\n\n## Credits\n\nInspired by [five](https://pypi.org/project/five/).\n',
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
