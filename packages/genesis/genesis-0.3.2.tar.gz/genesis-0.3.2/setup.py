# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['genesis']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'genesis',
    'version': '0.3.2',
    'description': 'Implementation of FreeSWITCH Event Socket protocol with asyncio',
    'long_description': None,
    'author': 'Vitor Hugo',
    'author_email': 'vitor.hov@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/Otoru/Genesis',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
