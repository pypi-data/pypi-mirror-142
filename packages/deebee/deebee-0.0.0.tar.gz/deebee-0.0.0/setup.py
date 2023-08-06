# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['deebee']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'deebee',
    'version': '0.0.0',
    'description': 'A database funcions helper.',
    'long_description': '# deebee\nA asynchronous database helper lib.\n',
    'author': 'Manasses Lima',
    'author_email': 'manasseslima@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
