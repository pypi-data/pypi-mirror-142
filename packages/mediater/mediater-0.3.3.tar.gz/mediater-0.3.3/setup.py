# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['mediater']

package_data = \
{'': ['*']}

entry_points = \
{'console_scripts': ['mediater = mediater.console:run']}

setup_kwargs = {
    'name': 'mediater',
    'version': '0.3.3',
    'description': '',
    'long_description': None,
    'author': 'zenwalk',
    'author_email': 'zenwalk@example.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
