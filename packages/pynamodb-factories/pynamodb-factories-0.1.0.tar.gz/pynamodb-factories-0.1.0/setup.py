# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pynamodb_factories']

package_data = \
{'': ['*']}

install_requires = \
['Faker>=13.3.1,<14.0.0', 'pynamodb>=5.2.1,<6.0.0']

setup_kwargs = {
    'name': 'pynamodb-factories',
    'version': '0.1.0',
    'description': 'Fakers for Pynamo models, based on the very helpful pydantic-factories.',
    'long_description': None,
    'author': 'Jennifer Moore',
    'author_email': 'jenniferplusplus@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/jenniferplusplus/pynamo-factories',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
