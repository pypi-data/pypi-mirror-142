# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['agcounts']

package_data = \
{'': ['*']}

install_requires = \
['numpy>=1.22.0,<2.0.0', 'pandas>=1.3.5,<2.0.0', 'scipy>=1.8.0,<2.0.0']

setup_kwargs = {
    'name': 'agcounts',
    'version': '0.1.1',
    'description': 'This project contains code to generate activity counts from accelerometer data.',
    'long_description': '# agcounts\n![Tests](https://github.com/actigraph/agcounts/actions/workflows/tests.yml/badge.svg)\n\nA python package for extracting actigraphy counts from accelerometer data. \n',
    'author': 'Actigraph LLC',
    'author_email': 'data.science@theactigraph.com',
    'maintainer': 'Ali Neishabouri',
    'maintainer_email': 'ali.neishabouri@theactigraph.com',
    'url': 'https://github.com/actigraph/agcounts',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<3.11',
}


setup(**setup_kwargs)
