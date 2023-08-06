# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['codecraftoj', 'codecraftoj.server']

package_data = \
{'': ['*']}

install_requires = \
['Flask>=2.0.3,<3.0.0']

entry_points = \
{'console_scripts': ['CodeCraftOJ = CodeCraftOJ.cli:entry']}

setup_kwargs = {
    'name': 'codecraftoj',
    'version': '0.1.0',
    'description': '',
    'long_description': None,
    'author': 'InEase',
    'author_email': 'InEase28@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
