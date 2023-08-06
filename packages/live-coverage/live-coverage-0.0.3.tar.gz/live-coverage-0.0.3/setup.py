# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['live_coverage']

package_data = \
{'': ['*']}

install_requires = \
['coverage>=6.3.2,<7.0.0']

entry_points = \
{'console_scripts': ['live-coverage = live_coverage.live_coverage:main']}

setup_kwargs = {
    'name': 'live-coverage',
    'version': '0.0.3',
    'description': 'Live Code Coverage for Python',
    'long_description': '# live-coverage\nLive Code Coverage for Python\n',
    'author': 'Defelo',
    'author_email': 'elodef42@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/Defelo/live-coverage',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<4.0',
}
from _build import *
build(setup_kwargs)

setup(**setup_kwargs)
