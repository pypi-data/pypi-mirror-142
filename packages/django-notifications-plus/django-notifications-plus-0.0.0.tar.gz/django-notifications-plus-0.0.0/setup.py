# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['notifications_plus']

package_data = \
{'': ['*']}

install_requires = \
['django-filter>=21.1,<22.0', 'djangorestframework>=3.13.1,<4.0.0']

setup_kwargs = {
    'name': 'django-notifications-plus',
    'version': '0.0.0',
    'description': '',
    'long_description': '# django-notifications-plus',
    'author': 'jukanntenn',
    'author_email': 'jukanntenn@outlook.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/DjangoStudyTeam/django-notifications-plus',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
