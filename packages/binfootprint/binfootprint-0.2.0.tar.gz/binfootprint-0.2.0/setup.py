# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['binfootprint']

package_data = \
{'': ['*']}

install_requires = \
['numpy>=1.22.0,<2.0.0', 'pytest>=7.0.0,<8.0.0', 'scipy>=1.8.0,<2.0.0']

setup_kwargs = {
    'name': 'binfootprint',
    'version': '0.2.0',
    'description': 'serielize python objetcs in a deterministic way',
    'long_description': None,
    'author': 'Richard Hartmann',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<3.10',
}


setup(**setup_kwargs)
