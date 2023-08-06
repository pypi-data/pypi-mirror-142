# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['echo1_coco_preview']

package_data = \
{'': ['*']}

install_requires = \
['bbox-visualizer>=0.1.0,<0.2.0',
 'loguru>=0.6.0,<0.7.0',
 'opencv-python>=4.5.5,<5.0.0',
 'pydash>=5.1.0,<6.0.0']

entry_points = \
{'console_scripts': ['coco-preview = '
                     'echo1_coco_preview.echo1_coco_preview:app']}

setup_kwargs = {
    'name': 'echo1-coco-preview',
    'version': '0.1.0',
    'description': '',
    'long_description': '# echo1-coco-preview',
    'author': 'Michael Mohamed',
    'author_email': 'michael.mohamed@echo1.io',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/e1-io/echo1-coco-preview',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
