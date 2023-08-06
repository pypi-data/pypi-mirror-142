# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['boeah',
 'boeah.commands',
 'boeah.db',
 'boeah.db.drivers',
 'boeah.db.model',
 'boeah.http']

package_data = \
{'': ['*']}

install_requires = \
['Werkzeug>=2.0.3,<3.0.0',
 'ipython>=7.32,<8.0',
 'python-dotenv>=0.19.2,<0.20.0',
 'rich>=11.2.0,<12.0.0']

setup_kwargs = {
    'name': 'boeah',
    'version': '0.1.3',
    'description': 'Boeah Framework',
    'long_description': None,
    'author': 'Fathur',
    'author_email': 'hi.fathur.rohman@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
