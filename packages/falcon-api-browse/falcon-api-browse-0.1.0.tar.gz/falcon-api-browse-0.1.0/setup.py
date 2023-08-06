# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['falcon_api_browse']

package_data = \
{'': ['*'], 'falcon_api_browse': ['templates/*']}

install_requires = \
['Jinja2>=2.0.0', 'falcon>=2.0.0']

setup_kwargs = {
    'name': 'falcon-api-browse',
    'version': '0.1.0',
    'description': 'Middleware for Falcon web framework to browse JSON API in HTML',
    'long_description': None,
    'author': 'Abhilash Raj',
    'author_email': 'raj.abhilash1@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7',
}


setup(**setup_kwargs)
