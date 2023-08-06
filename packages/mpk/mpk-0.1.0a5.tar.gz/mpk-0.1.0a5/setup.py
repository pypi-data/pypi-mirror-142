# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['mpk']

package_data = \
{'': ['*']}

install_requires = \
['essentia',
 'librosa>=0.9.1,<0.10.0',
 'llvmlite>=0.38.0,<0.39.0',
 'numpy>=1.21,<2.0']

entry_points = \
{'console_scripts': ['main = mpk_extract:run']}

setup_kwargs = {
    'name': 'mpk',
    'version': '0.1.0a5',
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
    'python_requires': '>=3.7,<3.11',
}


setup(**setup_kwargs)
