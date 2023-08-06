# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['jrpytorch', 'jrpytorch.datasets']

package_data = \
{'': ['*'], 'jrpytorch': ['vignettes/*'], 'jrpytorch.datasets': ['data/*']}

install_requires = \
['matplotlib>=3.0',
 'numpy>=1.15',
 'pandas>=1',
 'scikit-learn>=1.0.0',
 'torch>=1',
 'torchvision>=0.11',
 'visdom>=0.1.8']

setup_kwargs = {
    'name': 'jrpytorch',
    'version': '0.1.10',
    'description': 'Jumping Rivers: PyTorch with Python',
    'long_description': None,
    'author': 'Jamie',
    'author_email': 'jamie@jumpingrivers.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
