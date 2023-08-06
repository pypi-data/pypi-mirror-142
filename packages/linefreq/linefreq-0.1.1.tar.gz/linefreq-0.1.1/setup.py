# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['fq']

package_data = \
{'': ['*']}

install_requires = \
['rich>=12.0.0,<13.0.0']

entry_points = \
{'console_scripts': ['fq = fq.cli:run']}

setup_kwargs = {
    'name': 'linefreq',
    'version': '0.1.1',
    'description': 'a real time line frequency utility',
    'long_description': None,
    'author': 'redraw',
    'author_email': 'redraw@sdf.org',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/redraw/fq',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6.2,<4.0',
}


setup(**setup_kwargs)
