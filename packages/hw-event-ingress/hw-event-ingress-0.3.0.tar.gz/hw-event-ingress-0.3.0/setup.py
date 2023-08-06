# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['hw_event_ingress']

package_data = \
{'': ['*']}

install_requires = \
['aio-pika>=7.1,<8.0', 'mypy>=0.910,<0.911']

setup_kwargs = {
    'name': 'hw-event-ingress',
    'version': '0.3.0',
    'description': '',
    'long_description': None,
    'author': 'Skyler Lewis',
    'author_email': 'skyler@hivewire.co',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
