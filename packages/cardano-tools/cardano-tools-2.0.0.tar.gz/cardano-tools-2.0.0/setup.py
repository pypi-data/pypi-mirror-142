# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['cardano_tools', 'cardano_tools.utils']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'cardano-tools',
    'version': '2.0.0',
    'description': 'A collection of tools to enable development in the Cardano ecosystem using the Python programming language.',
    'long_description': None,
    'author': 'Viper Science LLC',
    'author_email': 'viperstakepool@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://gitlab.com/viper-staking/cardano-tools',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
