# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['mtgbinderspine']

package_data = \
{'': ['*']}

install_requires = \
['CairoSVG>=2.5.2,<3.0.0',
 'Pillow>=9.0.1,<10.0.0',
 'click>=8.0.4,<9.0.0',
 'diskcache>=5.4.0,<6.0.0',
 'reportlab>=3.6.8,<4.0.0',
 'requests>=2.27.1,<3.0.0',
 'svglib>=1.2.1,<2.0.0']

entry_points = \
{'console_scripts': ['mtgbinderspine = '
                     'mtgbinderspine.main:render_spine_command']}

setup_kwargs = {
    'name': 'mtgbinderspine',
    'version': '0.1.1',
    'description': 'A tool to generate printable labels for binders of Magic: The Gathering cards',
    'long_description': '# MTG Binder Spine Generator\n\nGenerates an image that can be printed and inserted into the spine of a binder.\n\n## Setup\n\n`poetry install`\n\n## Usage\n\nGenerate an image with spines for Throne of Eldraine and Kaladesh:\n\n`poetry run mtgbinderspine eld kld`\n',
    'author': 'Dan Winkler',
    'author_email': 'dan@danwink.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/danwinkler/mtgbinderspine',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
