# -*- coding: utf-8 -*-
from distutils.core import setup

packages = \
['pyuque', 'pyuque.toolkit', 'pyuque.util']

package_data = \
{'': ['*']}

install_requires = \
['Markdown>=3.2.2,<4.0.0', 'bs4>=0.0.1,<0.0.2', 'requests>=2.22.0,<3.0.0']

entry_points = \
{'console_scripts': ['pyuque = pyuque.cli:main']}

setup_kwargs = {
    'name': 'pyuque',
    'version': '0.3.0',
    'description': 'A Python client/toolkit for yuque.',
    'long_description': None,
    'author': 'lichun',
    'author_email': None,
    'url': 'https://github.com/socrateslee/pyuque',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.5,<4.0',
}


setup(**setup_kwargs)
