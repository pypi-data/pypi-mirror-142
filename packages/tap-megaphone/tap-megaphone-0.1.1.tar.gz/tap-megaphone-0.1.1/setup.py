# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['tap_megaphone', 'tap_megaphone.tests']

package_data = \
{'': ['*'], 'tap_megaphone': ['schemas/*']}

install_requires = \
['pendulum>=2.1.2,<3.0.0',
 'requests>=2.25.1,<3.0.0',
 'singer-sdk>=0.4.1,<0.5.0']

entry_points = \
{'console_scripts': ['tap-instagram = tap_megaphone.tap:TapMegaphone.cli']}

setup_kwargs = {
    'name': 'tap-megaphone',
    'version': '0.1.1',
    'description': '`tap-megaphone` is a Singer tap for Megaphone, built with the Meltano SDK for Singer Taps.',
    'long_description': None,
    'author': 'Joy Yu',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6.2,<3.11',
}


setup(**setup_kwargs)
