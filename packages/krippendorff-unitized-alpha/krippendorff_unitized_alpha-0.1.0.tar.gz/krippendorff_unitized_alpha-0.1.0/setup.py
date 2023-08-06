# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['krippendorff_unitized_alpha']

package_data = \
{'': ['*']}

install_requires = \
['numpy>=1.22.3,<2.0.0', 'pytest>=7.1.0,<8.0.0']

setup_kwargs = {
    'name': 'krippendorff-unitized-alpha',
    'version': '0.1.0',
    'description': '',
    'long_description': None,
    'author': 'Zeljko Bekcic',
    'author_email': 'zeljko.bekcic@posteo.net',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
