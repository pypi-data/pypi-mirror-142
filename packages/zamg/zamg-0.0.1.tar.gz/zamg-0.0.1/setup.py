# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['zamg', 'zamg.examples']

package_data = \
{'': ['*']}

install_requires = \
['aiohttp>=3.8.0', 'backoff>=1.11.0', 'cachetools>=5.0.0', 'yarl>=1.7.2']

setup_kwargs = {
    'name': 'zamg',
    'version': '0.0.1',
    'description': 'Asynchronous Python client for ZAMG weather data.',
    'long_description': '# python-zamg\nPython library to read hourly weather data from ZAMG\n',
    'author': 'Daniel Gangl',
    'author_email': 'killer007@gmx.at',
    'maintainer': 'Daniel Gangl',
    'maintainer_email': 'killer007@gmx.at',
    'url': 'https://github.com/killer0071234/python-zamg',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
