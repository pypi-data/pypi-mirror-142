# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pyroll_integral_thermal']

package_data = \
{'': ['*']}

install_requires = \
['pyroll>=0.5.0,<0.6.0']

setup_kwargs = {
    'name': 'pyroll-integral-thermal',
    'version': '0.2.3',
    'description': 'Plugin for PyRoll providing an integral approach for thermal modelling.',
    'long_description': None,
    'author': 'Max Weiner',
    'author_email': 'max.weiner@imf.tu-freiberg.de',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://pyroll-project.github.io/',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<3.11',
}


setup(**setup_kwargs)
