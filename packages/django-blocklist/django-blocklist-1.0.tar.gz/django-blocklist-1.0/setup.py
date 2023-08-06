# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['django_blocklist',
 'django_blocklist.management',
 'django_blocklist.management.commands',
 'django_blocklist.migrations',
 'django_blocklist.tests']

package_data = \
{'': ['*']}

install_requires = \
['Django==3.2']

setup_kwargs = {
    'name': 'django-blocklist',
    'version': '1.0',
    'description': 'A Django app that implements IP-based blocklisting.',
    'long_description': None,
    'author': 'Paul Bissex',
    'author_email': 'paul@bissex.net',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
