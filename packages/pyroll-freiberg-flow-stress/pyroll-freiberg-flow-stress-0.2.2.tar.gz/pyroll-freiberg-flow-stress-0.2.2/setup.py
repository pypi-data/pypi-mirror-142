# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pyroll_freiberg_flow_stress', 'pyroll_freiberg_flow_stress.materials']

package_data = \
{'': ['*']}

install_requires = \
['numpy>=1.22.2,<2.0.0', 'pyroll>=0.5.0,<0.6.0']

setup_kwargs = {
    'name': 'pyroll-freiberg-flow-stress',
    'version': '0.2.2',
    'description': 'Plugin for PyRoll providing Freiberg flow stress approach and material database.',
    'long_description': None,
    'author': 'Max Weiner',
    'author_email': 'max.weiner@imf.tu-freiberg.de',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<3.11',
}


setup(**setup_kwargs)
