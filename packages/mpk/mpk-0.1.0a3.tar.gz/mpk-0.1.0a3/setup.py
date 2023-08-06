# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['mpk']

package_data = \
{'': ['*']}

install_requires = \
['essentia==2.1b6', 'librosa>=0.9.1', 'numpy>=1.21']

entry_points = \
{'console_scripts': ['main = mpk_extract:run']}

setup_kwargs = {
    'name': 'mpk',
    'version': '0.1.0a3',
    'description': 'Media Programming Kit Python bindings',
    'long_description': None,
    'author': 'ellis',
    'author_email': 'ellis@rwest.io',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://hg.rwest.io/mpk',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<3.10',
}


setup(**setup_kwargs)
