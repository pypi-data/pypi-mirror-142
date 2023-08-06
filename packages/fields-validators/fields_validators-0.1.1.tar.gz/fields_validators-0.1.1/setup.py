# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['fields_validators', 'fields_validators.exceptions']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'fields-validators',
    'version': '0.1.1',
    'description': '',
    'long_description': None,
    'author': 'guilherme',
    'author_email': 'guilherme.1995lemes@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
