# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['soft', 'soft.client', 'soft.server']

package_data = \
{'': ['*']}

install_requires = \
['PyNaCl>=1.5.0,<2.0.0', 'loguru>=0.6.0,<0.7.0']

setup_kwargs = {
    'name': 'soft-files',
    'version': '0.2.0',
    'description': 'A homegrown file transfer protocol.',
    'long_description': None,
    'author': 'Kronifer',
    'author_email': '44979306+Kronifer@users.noreply.github.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
