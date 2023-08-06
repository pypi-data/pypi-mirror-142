# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['funppy', 'funppy.examples']

package_data = \
{'': ['*']}

install_requires = \
['grpcio-tools>=1.44.0,<2.0.0', 'grpcio>=1.44.0,<2.0.0']

setup_kwargs = {
    'name': 'funppy',
    'version': '0.3.0',
    'description': 'Python plugin over gRPC for funplugin',
    'long_description': None,
    'author': 'debugtalk',
    'author_email': 'mail@debugtalk.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/httprunner/funplugin',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
