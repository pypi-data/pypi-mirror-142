# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['dataart_python']

package_data = \
{'': ['*']}

install_requires = \
['requests==2.27.1']

setup_kwargs = {
    'name': 'dataart-python',
    'version': '0.1.0',
    'description': '',
    'long_description': None,
    'author': 'sadra khamoshi',
    'author_email': 'sadrakhamoshi7@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
