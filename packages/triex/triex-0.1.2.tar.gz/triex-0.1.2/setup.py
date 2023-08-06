# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['triex']

package_data = \
{'': ['*']}

install_requires = \
['click>=8.0.4,<9.0.0', 'requests>=2.27.1,<3.0.0']

entry_points = \
{'console_scripts': ['triex = triex.triex:triex']}

setup_kwargs = {
    'name': 'triex',
    'version': '0.1.2',
    'description': 'An Interactive Trie CLI',
    'long_description': '# CLI Server',
    'author': 'Ashwin Sriram',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
