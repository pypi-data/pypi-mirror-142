# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['kvom']

package_data = \
{'': ['*']}

install_requires = \
['pydantic>=1.9.0,<2.0.0', 'pymongo>=4.0.1,<5.0.0', 'redis>=4.1.3,<5.0.0']

setup_kwargs = {
    'name': 'kvom',
    'version': '0.2.0',
    'description': 'key-value store object mapping',
    'long_description': None,
    'author': 'ischaojie',
    'author_email': 'zhuzhezhe95@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
