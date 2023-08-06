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
    'version': '0.1.3',
    'description': 'A Simple Email Dispatcher based on top of win32Api',
    'long_description': '# Outlook Email Dispatcher\n\n### A Simple Email Dispatcher based on top of win32Api\n\n## Example of Usage: \n\n\n### Create a new Mail\n\nCC and Attachments are Optional\n\n```\nFILES_TO_ATTACH_FOLDER = os.path.join(os.getcwd(), \'files_to_attach\')\nATTACHMENTS = [os.path.join(FILES_TO_ATTACH_FOLDER, f) for f in os.listdir(FILES_TO_ATTACH_FOLDER)]\n\nmail = Mail(\n     Subject="Your Subject Here",\n    To="example@example.com",\n    HTMLBody="<h1>Your message Here</h1>",\n    CC="example@example.com",\n    Attachments=ATTACHMENTS,\n)\n```\n\n### Initialize Outlook\n\nInstanciate an Object from Outlook Class\n\n\n```\noutlook = Outlook()\n```\n\n### Preview Mail:\n```\noutlook.preview(mail)\n```\n\n### Send Mail:\n```\noutlook.send(mail)\n```\n\n\n',
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
