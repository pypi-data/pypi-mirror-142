# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['aws_browser']

package_data = \
{'': ['*']}

install_requires = \
['boto3>=1.21.1,<2.0.0', 'requests>=2.27.1,<3.0.0']

entry_points = \
{'console_scripts': ['aws-browser = aws_browser.cli:run']}

setup_kwargs = {
    'name': 'aws-browser',
    'version': '0.1.3',
    'description': '',
    'long_description': None,
    'author': 'Ben Bridts',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
