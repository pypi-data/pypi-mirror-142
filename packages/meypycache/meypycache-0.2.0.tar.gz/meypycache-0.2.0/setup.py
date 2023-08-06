# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['meypycache', 'meypycache.caches', 'meypycache.core']

package_data = \
{'': ['*']}

install_requires = \
['PyYAML>=6.0,<7.0',
 'loguru>=0.6.0,<0.7.0',
 'pytest-lazy-fixture>=0.6.3,<0.7.0',
 'pytest>=7.0.1,<8.0.0']

setup_kwargs = {
    'name': 'meypycache',
    'version': '0.2.0',
    'description': '',
    'long_description': None,
    'author': 'Your Name',
    'author_email': 'you@example.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
