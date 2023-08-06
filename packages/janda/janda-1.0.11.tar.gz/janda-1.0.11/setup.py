# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['janda', 'janda.utils']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'janda',
    'version': '1.0.11',
    'description': '',
    'long_description': None,
    'author': 'sinkaroid',
    'author_email': 'anakmancasan@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
}


setup(**setup_kwargs)
