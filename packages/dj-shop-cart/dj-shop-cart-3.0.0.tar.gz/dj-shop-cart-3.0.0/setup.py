# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['dj_shop_cart', 'dj_shop_cart.migrations', 'migrations']

package_data = \
{'': ['*']}

install_requires = \
['Django>=3', 'attrs>=21.4.0,<22.0.0']

setup_kwargs = {
    'name': 'dj-shop-cart',
    'version': '3.0.0',
    'description': 'Simple django cart manager for your django projects.',
    'long_description': None,
    'author': 'Tobi DEGNON',
    'author_email': 'tobidegnon@protonmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/Tobi-De/dj-shop-cart',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
