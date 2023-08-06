# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pyroll',
 'pyroll.core',
 'pyroll.core.grooves',
 'pyroll.core.grooves.boxes',
 'pyroll.core.grooves.diamonds',
 'pyroll.core.grooves.ovals',
 'pyroll.core.grooves.rounds',
 'pyroll.core.profile',
 'pyroll.core.profile.base_plugins',
 'pyroll.core.roll_pass',
 'pyroll.core.roll_pass.base_plugins',
 'pyroll.core.transport',
 'pyroll.core.transport.base_plugins',
 'pyroll.ui',
 'pyroll.ui.cli',
 'pyroll.ui.cli.res',
 'pyroll.ui.exporter',
 'pyroll.ui.report',
 'pyroll.ui.report.base_plugins',
 'pyroll.utils']

package_data = \
{'': ['*']}

install_requires = \
['Jinja2>=3.0.3,<4.0.0',
 'PyYAML>=6.0,<7.0',
 'click>=8.0.0,<9.0.0',
 'lxml>=4.7.1,<5.0.0',
 'makefun>=1.13.1,<2.0.0',
 'matplotlib>=3.5.0,<4.0.0',
 'numpy>=1.21.4,<2.0.0',
 'pandas>=1.4.1,<2.0.0',
 'pluggy>=1.0.0,<2.0.0',
 'scipy>=1.7.2,<2.0.0']

entry_points = \
{'console_scripts': ['pyroll = pyroll.ui.cli:main']}

setup_kwargs = {
    'name': 'pyroll',
    'version': '0.5.1',
    'description': 'PyRoll rolling simulation framework - core library.',
    'long_description': None,
    'author': 'Matthias Schmidtchen',
    'author_email': 'matthias.schmidtchen@imf.tu-freiberg.de',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://pyroll-project.github.io/',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<3.11',
}


setup(**setup_kwargs)
