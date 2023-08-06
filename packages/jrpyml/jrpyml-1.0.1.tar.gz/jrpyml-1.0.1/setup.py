# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['jrpyml', 'jrpyml.datasets']

package_data = \
{'': ['*'], 'jrpyml.datasets': ['data/*']}

install_requires = \
['graphviz>=0.10',
 'matplotlib>=3.0',
 'numpy>=1.19',
 'pandas>=1',
 'scikit-learn>=1',
 'scipy>=1.2',
 'seaborn>=0.11']

setup_kwargs = {
    'name': 'jrpyml',
    'version': '1.0.1',
    'description': 'Jumping Rivers: Machine Learning with Python',
    'long_description': None,
    'author': 'Jumping Rivers',
    'author_email': 'info@jumpingrivers.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7',
}


setup(**setup_kwargs)
