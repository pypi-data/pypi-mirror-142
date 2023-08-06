# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['fastapi_plugins_pika',
 'fastapi_plugins_pika.schema',
 'fastapi_plugins_pika.service',
 'fastapi_plugins_pika.service.rtcServiceImpl']

package_data = \
{'': ['*']}

install_requires = \
['fastapi>=0.75.0,<0.76.0']

setup_kwargs = {
    'name': 'fastapi-plugins-pika',
    'version': '0.1.0',
    'description': '',
    'long_description': None,
    'author': 'chuhy',
    'author_email': 'chu-hy@foxmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
