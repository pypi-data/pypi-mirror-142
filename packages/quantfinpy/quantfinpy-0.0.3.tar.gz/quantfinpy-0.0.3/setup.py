# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['quantfinpy',
 'quantfinpy.data',
 'quantfinpy.data.cashflow',
 'quantfinpy.data.ir',
 'quantfinpy.enum',
 'quantfinpy.instrument',
 'quantfinpy.instrument.credit',
 'quantfinpy.instrument.equity',
 'quantfinpy.instrument.fx',
 'quantfinpy.instrument.ir',
 'quantfinpy.instrument.ir.cashflow',
 'quantfinpy.instrument.ir.swap',
 'quantfinpy.order',
 'quantfinpy.utils']

package_data = \
{'': ['*']}

install_requires = \
['attrs>=21.4.0,<22.0.0',
 'cytoolz>=0.11.2,<0.12.0',
 'pandas-stubs>=1.2.0,<2.0.0',
 'pandas>=1.4.1,<2.0.0',
 'typing-extensions>=4.1.1,<5.0.0']

setup_kwargs = {
    'name': 'quantfinpy',
    'version': '0.0.3',
    'description': 'Quantitative finance in python.',
    'long_description': None,
    'author': 'TradingPy',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
