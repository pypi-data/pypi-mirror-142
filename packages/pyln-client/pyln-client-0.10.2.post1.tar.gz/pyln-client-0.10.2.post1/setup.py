# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['client']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'pyln-client',
    'version': '0.10.2.post1',
    'description': 'Client library and plugin library for c-lightning',
    'long_description': None,
    'author': 'Christian Decker',
    'author_email': 'decker.christian@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
