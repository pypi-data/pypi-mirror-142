# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['bolt1']

package_data = \
{'': ['*']}

install_requires = \
['pyln-proto>=0.10.2,<0.11.0']

setup_kwargs = {
    'name': 'pyln-bolt1',
    'version': '1.0.1.187',
    'description': '',
    'long_description': None,
    'author': 'Rusty Russell',
    'author_email': 'rusty@blockstream.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
