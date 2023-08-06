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
    'version': '3.0.2',
    'description': 'Simple django cart manager for your django projects.',
    'long_description': '# dj-shop-cart\n\nA simple and flexible cart manager for your django projects.\n\n[![pypi](https://badge.fury.io/py/dj-shop-cart.svg)](https://pypi.org/project/dj-shop-cart/)\n[![python](https://img.shields.io/pypi/pyversions/dj-shop-cart)](https://github.com/Tobi-De/dj-shop-cart)\n[![MIT License](https://img.shields.io/apm/l/atomic-design-ui.svg?)](https://github.com/Tobi-De/dj-shop-cart/blob/master/LICENSE)\n\n**This is a work in progress, expect api breaking changes, pin the exact version you are using**\n\n## Features\n\n- Add, remove, decrement and clear items from cart\n- Authenticated users cart can be saved to database\n- Write custom methods to easily hook into the items add / remove flow\n- Custom **get_price** method to ensure that the cart always have an up-to-date products price\n- Access to your django database **Product** instance from the cart items\n- Metadata data can be attached to cart items\n- Supports specification of product variation details\n- Available context processor for easy access to the user cart in all your django templates\n\n\n## Installation\n\nInstall **dj-shop-cart** with pip or poetry.\n\n```bash\n  pip install dj-shop-cart\n```\n\n## Usage/Examples\n\n```python3\n\n# settings.py\n\nINSTALLED_APPS = [\n    ...,\n    "dj_shop_cart", # If you want the cart to be stored in the database when users are authenticated\n    ...,\n]\n\nTEMPLATES = [\n    {\n        "OPTIONS": {\n            "context_processors": [\n                ...,\n                "dj_shop_cart.context_processors.cart", # If you want access to the cart instance in all templates\n            ],\n        },\n    }\n]\n\n# views.py\n\nfrom dj_shop_cart.cart import get_cart_manager_class\nfrom django.http import HttpRequest\nfrom django.views.decorators.http import require_POST\n\nfrom .helpers import collect_params\n\nCart = get_cart_manager_class()\n\n\n@require_POST\ndef add_product(request: HttpRequest):\n    product, quantity = collect_params(request)\n    cart = Cart.new(request)\n    cart.add(product, quantity=quantity)\n    ...\n\n\n@require_POST\ndef remove_product(request: HttpRequest):\n    product, quantity = collect_params(request)\n    cart = Cart.new(request)\n    cart.remove(product, quantity=quantity)\n    ...\n\n\n@require_POST\ndef empty_cart(request: HttpRequest):\n    Cart.new(request).empty()\n    ...\n\n```\n\n\n\n## Feedback\n\nIf you have any feedback, please reach out to me at degnonfrancis@gmail.com\n\n## Todos\n\n- More examples\n- Add api reference\n- Add Used by section to readme\n- Write more tests\n- Add local dev section to readme\n',
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
