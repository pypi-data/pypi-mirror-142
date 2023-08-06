# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['jrpytensorflow', 'jrpytensorflow.datasets']

package_data = \
{'': ['*'], 'jrpytensorflow.datasets': ['data/*']}

install_requires = \
['PyYAML>=6.0,<7.0',
 'matplotlib>=3.5.1,<4.0.0',
 'pandas>=1.4.1,<2.0.0',
 'scikit-learn>=1.0.2,<2.0.0',
 'tensorboard>=2.8.0,<3.0.0',
 'tensorflow-datasets>=4.5.2,<5.0.0',
 'tensorflow>=2.8.0,<3.0.0']

setup_kwargs = {
    'name': 'jrpytensorflow',
    'version': '0.1.11',
    'description': 'Jumping Rivers: Python and Tensorflow',
    'long_description': None,
    'author': 'Jamie',
    'author_email': 'jamie@jumpingrivers.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<3.11',
}


setup(**setup_kwargs)
