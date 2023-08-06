# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['ppdl']

package_data = \
{'': ['*'], 'ppdl': ['bin/*']}

install_requires = \
['matplotlib>=3.5.1,<4.0.0',
 'numpy>=1.22.2,<2.0.0',
 'pandas>=1.4.0,<2.0.0',
 'progressbar2>=4.0.0,<5.0.0',
 'rlxutils>=0.1.7,<0.2.0',
 'sympy>=1.9,<2.0',
 'tensorflow==2.7.0']

setup_kwargs = {
    'name': 'ppdl',
    'version': '0.1.6',
    'description': 'Source code for probabilistic deep learning course.',
    'long_description': None,
    'author': 'Juan Lara',
    'author_email': 'julara@unal.edu.co',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<3.11',
}


setup(**setup_kwargs)
