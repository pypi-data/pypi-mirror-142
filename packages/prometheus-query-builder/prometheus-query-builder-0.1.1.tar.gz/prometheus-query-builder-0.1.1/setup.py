# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['prometheus_query_builder']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'prometheus-query-builder',
    'version': '0.1.1',
    'description': 'Package for generation Prometheus Query Language queries.',
    'long_description': None,
    'author': 'Michail Tsyganov',
    'author_email': 'tsyganov.michail@yandex.ru',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/m-chrome/prometheus-query-builder',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
