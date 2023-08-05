# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['sklearn_transformer_extensions']

package_data = \
{'': ['*']}

install_requires = \
['pandas>=1.4.1,<2.0.0', 'scikit-learn>=1.0.2,<2.0.0']

setup_kwargs = {
    'name': 'sklearn-transformer-extensions',
    'version': '0.1.8',
    'description': 'Some scikit-learn transformer extensions to make using pandas dataframes in scikit-learn pipelines easier.',
    'long_description': None,
    'author': 'Random Geek',
    'author_email': 'randomgeek78@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
