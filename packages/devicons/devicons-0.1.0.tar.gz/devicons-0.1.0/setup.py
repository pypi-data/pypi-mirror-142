# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['devicons']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'devicons',
    'version': '0.1.0',
    'description': 'A set of icons representing programming languages, designing & development tools.',
    'long_description': '# devicons\n\ntodo\n\nhttps://github.com/ryanoasis/vim-devicons/blob/master/plugin/webdevicons.vim\n',
    'author': 'Eliaz Bobadilla',
    'author_email': 'eliaz.bobadilladev@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/UltiRequiem/devicons-python',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
