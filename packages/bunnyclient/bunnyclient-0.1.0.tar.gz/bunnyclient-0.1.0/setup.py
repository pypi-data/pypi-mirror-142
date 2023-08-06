# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['bunnyclient', 'bunnyclient.config', 'bunnyclient.handlers']

package_data = \
{'': ['*']}

install_requires = \
['pika>=1.2.0,<2.0.0', 'prettyconf>=2.2.1,<3.0.0', 'pydantic>=1.9.0,<2.0.0']

setup_kwargs = {
    'name': 'bunnyclient',
    'version': '0.1.0',
    'description': '',
    'long_description': '',
    'author': 'Ramon Rodrigues',
    'author_email': 'ramon.srodrigues01@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
