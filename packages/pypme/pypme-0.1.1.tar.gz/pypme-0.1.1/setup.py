# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pypme']

package_data = \
{'': ['*']}

install_requires = \
['numpy-financial>=1.0.0,<2.0.0', 'pandas>=1.4.1,<2.0.0', 'xirr>=0.1.8,<0.2.0']

setup_kwargs = {
    'name': 'pypme',
    'version': '0.1.1',
    'description': 'Python library for PME (Public Market Equivalent) calculation',
    'long_description': None,
    'author': 'ymyke',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/ymyke/pypme',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<3.10',
}


setup(**setup_kwargs)
