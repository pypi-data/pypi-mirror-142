# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pynamodb_factories']

package_data = \
{'': ['*']}

install_requires = \
['Faker>=13.3.1,<14.0.0', 'pynamodb>=4.3.0']

setup_kwargs = {
    'name': 'pynamodb-factories',
    'version': '0.1.3',
    'description': 'Fakers for Pynamo models, based on the very helpful pydantic-factories.',
    'long_description': '# Usage\n\n```python\nfrom pynamodb import Model\nfrom pynamodb_factories import PynamoModelFactory\n\nclass SomePynamoModel(Model):\n    ...\n    pass\n\nclass SomeModelFactory(PynamoModelFactory):\n    __model__ = SomePynamoModel\n    pass\n\nfake_model = SomeModelFactory.build()\n```',
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
