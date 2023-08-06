# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['rescrap']

package_data = \
{'': ['*']}

install_requires = \
['PyPDF2>=1.26.0,<2.0.0',
 'regex>=2021.11.10,<2022.0.0',
 'requests>=2.27.1,<3.0.0']

setup_kwargs = {
    'name': 'rescrap',
    'version': '0.1.1',
    'description': 'Regex Scraper',
    'long_description': None,
    'author': 'LouMa',
    'author_email': 'louma.pypi@protonmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
