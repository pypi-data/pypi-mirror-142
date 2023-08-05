# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['first_step']

package_data = \
{'': ['*']}

install_requires = \
['click>=8.0.4,<9.0.0']

entry_points = \
{'console_scripts': ['inc = first_step.cli:cli']}

setup_kwargs = {
    'name': 'first-step',
    'version': '0.1.0',
    'description': '',
    'long_description': None,
    'author': 'jasjung',
    'author_email': 'insikjung2017@u.northwestern.edu',
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
