# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['watchfiles']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'watchfiles',
    'version': '0.0.0a1',
    'description': 'Placeholder until I rename watchgod to use this name.',
    'long_description': '# watchfiles\n\nPlaceholder until I rename [watchgod](https://pypi.org/project/watchgod/) to use this name.\n',
    'author': 'Samuel Colvin',
    'author_email': 's@muelcolvin.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
