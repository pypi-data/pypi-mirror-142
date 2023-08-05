# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['convert_shp_to_csv']

package_data = \
{'': ['*']}

install_requires = \
['Shapely>=1.8.1,<2.0.0',
 'geopandas>=0.10.2,<0.11.0',
 'numpy>=1.22.3,<2.0.0',
 'pygeos>=0.12.0,<0.13.0']

entry_points = \
{'console_scripts': ['convert-shp-to-csv = convert_shp_to_csv.main:main']}

setup_kwargs = {
    'name': 'convert-shp-to-csv',
    'version': '0.1.0',
    'description': 'Converts shape files (.shp) to a gridded csv file',
    'long_description': None,
    'author': 'Brandon Rose',
    'author_email': 'brandon@jataware.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
