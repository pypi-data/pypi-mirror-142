# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['telepay']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'telepay',
    'version': '0.0.1',
    'description': 'Python SDK for the TelePay API',
    'long_description': '# telepay-python\n\nPython SDK for the TelePay API\n',
    'author': 'Carlos Lugones',
    'author_email': 'contact@lugodev.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/TelePay-cash/telepay-python',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
