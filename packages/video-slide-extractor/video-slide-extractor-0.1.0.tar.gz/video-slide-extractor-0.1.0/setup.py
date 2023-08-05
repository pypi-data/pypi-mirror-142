# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['video_slide_extractor']

package_data = \
{'': ['*']}

install_requires = \
['docopt>=0.6.2,<0.7.0',
 'more-itertools>=8.12.0,<9.0.0',
 'opencv-python>=4.5.5,<5.0.0',
 'single-source>=0.3.0,<0.4.0',
 'tqdm>=4.63.0,<5.0.0']

extras_require = \
{'debug': ['ipdb>=0.13.9,<0.14.0']}

entry_points = \
{'console_scripts': ['slide-extractor = video_slide_extractor:cli.main']}

setup_kwargs = {
    'name': 'video-slide-extractor',
    'version': '0.1.0',
    'description': '',
    'long_description': None,
    'author': 'Tim Vergenz',
    'author_email': 'vergenzt@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
