# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['project_done']

package_data = \
{'': ['*']}

install_requires = \
['ipython>=8.1.1,<9.0.0']

setup_kwargs = {
    'name': 'project-done',
    'version': '0.1.0',
    'description': '',
    'long_description': None,
    'author': None,
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
