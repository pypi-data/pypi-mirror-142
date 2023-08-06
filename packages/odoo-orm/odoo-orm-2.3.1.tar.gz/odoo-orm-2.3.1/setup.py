# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['odoo_orm']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'odoo-orm',
    'version': '2.3.1',
    'description': 'A kind of Python ORM for Odoo XML-RPC API inspired by Django ORM.',
    'long_description': '# odoo-orm\nA kind of Python ORM for Odoo XML-RPC API inspired by Django ORM.\n',
    'author': 'mistiru',
    'author_email': 'dev@mistiru.me',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/mistiru/odoo-orm',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
