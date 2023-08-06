# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['hbsc_utils']

package_data = \
{'': ['*']}

install_requires = \
['chia-blockchain==1.3.0', 'requests>=2.27.1,<3.0.0']

setup_kwargs = {
    'name': 'hbsc-utils',
    'version': '0.2.1',
    'description': 'HBSC Python utils',
    'long_description': None,
    'author': 'Hairy Bear Social Club',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
