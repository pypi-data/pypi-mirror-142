# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['django_odoo_orm']

package_data = \
{'': ['*']}

install_requires = \
['Django>=4.0,<5.0', 'odoo-orm>=2.0.0,<3.0.0']

setup_kwargs = {
    'name': 'django-odoo-orm',
    'version': '3.0.1',
    'description': 'A kind of Python ORM for Odoo XML-RPC API inspired by Django ORM.',
    'long_description': 'Django Odoo ORM\n===============\n\nDjango Odoo ORM is a Django app to provide a fully setup ORM to Odoo in any Django project. This project adds nothing\nbut an app that sets the connection up at startup.\n\nQuick start\n-----------\n\n1. Add "django_odoo_orm" to your INSTALLED_APPS setting like this:\n\n```python\nINSTALLED_APPS = [\n    # ...\n    \'django_odoo_orm\',\n]\n```\n\n2. Add "django_odoo_orm.context_processors.odoo_connection" to your TEMPLATES setting like this:\n\n```python\nTEMPLATES = [\n    {\n        # ...\n        \'OPTIONS\': {\n            \'context_processors\': [\n                # ...\n                \'django_odoo_orm.context_processors.odoo_connection\',\n            ],\n        },\n    },\n]\n``\n',
    'author': 'mistiru',
    'author_email': 'dev@mistiru.me',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/mistiru/django-odoo-orm',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
