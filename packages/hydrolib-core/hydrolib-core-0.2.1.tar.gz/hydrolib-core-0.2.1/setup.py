# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['hydrolib',
 'hydrolib.core',
 'hydrolib.core.io',
 'hydrolib.core.io.bc',
 'hydrolib.core.io.bui',
 'hydrolib.core.io.crosssection',
 'hydrolib.core.io.dimr',
 'hydrolib.core.io.ext',
 'hydrolib.core.io.fnm',
 'hydrolib.core.io.friction',
 'hydrolib.core.io.ini',
 'hydrolib.core.io.inifield',
 'hydrolib.core.io.mdu',
 'hydrolib.core.io.net',
 'hydrolib.core.io.onedfield',
 'hydrolib.core.io.polyfile',
 'hydrolib.core.io.rr.topology',
 'hydrolib.core.io.storagenode',
 'hydrolib.core.io.structure',
 'hydrolib.core.io.xyz']

package_data = \
{'': ['*']}

install_requires = \
['lxml>=4.6,<5.0',
 'meshkernel>=1.0.0,<2.0.0',
 'mkdocs-macros-plugin>=0.6.3,<0.7.0',
 'netCDF4==1.5.7',
 'numpy>=1.21,<2.0',
 'pydantic[dotenv]>=1.8,<1.9']

setup_kwargs = {
    'name': 'hydrolib-core',
    'version': '0.2.1',
    'description': 'Python wrappers around D-HYDRO Suite.',
    'long_description': None,
    'author': 'Deltares',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
