# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['crossplain']

package_data = \
{'': ['*']}

install_requires = \
['crossplane>=0.5.7,<0.6.0']

setup_kwargs = {
    'name': 'crossplain',
    'version': '0.1.0',
    'description': 'Small layer on top of crossplane that uses plain Python objects instead of dicts. Includes intuitive ways to modify the config.',
    'long_description': None,
    'author': 'Ewen Le Bihan',
    'author_email': 'hey@ewen.works',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
