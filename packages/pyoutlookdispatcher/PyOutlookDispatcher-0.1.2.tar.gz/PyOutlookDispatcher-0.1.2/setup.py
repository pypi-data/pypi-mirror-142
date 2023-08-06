# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pyoutlookdispatcher']

package_data = \
{'': ['*']}

install_requires = \
['pywin32>=303,<304']

setup_kwargs = {
    'name': 'pyoutlookdispatcher',
    'version': '0.1.2',
    'description': 'A Simple Email Dispatcher based on top of win32Api',
    'long_description': None,
    'author': 'Rafael Tedesco',
    'author_email': 'dev.rafaeltedesco@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
