# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['random_time_with_intervals']

package_data = \
{'': ['*']}

install_requires = \
['XlsxWriter>=3.0.3,<4.0.0']

setup_kwargs = {
    'name': 'random-time-with-intervals',
    'version': '0.1.0',
    'description': '',
    'long_description': None,
    'author': 'Your Name',
    'author_email': 'you@example.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
