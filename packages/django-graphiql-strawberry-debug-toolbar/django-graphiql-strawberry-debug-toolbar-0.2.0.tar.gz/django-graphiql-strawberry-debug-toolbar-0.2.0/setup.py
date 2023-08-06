# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['graphiql_strawberry_debug_toolbar']

package_data = \
{'': ['*'],
 'graphiql_strawberry_debug_toolbar': ['static/graphiql_strawberry_debug_toolbar/js/*',
                                       'templates/graphiql_strawberry_debug_toolbar/*']}

install_requires = \
['Django>=2.2', 'django-debug-toolbar>=3.1', 'strawberry-graphql>=0.15.1']

setup_kwargs = {
    'name': 'django-graphiql-strawberry-debug-toolbar',
    'version': '0.2.0',
    'description': 'Django Debug Toolbar for GraphiQL IDE in Strawberry.',
    'long_description': "# Django GraphiQL Strawberry Debug Toolbar\n\n[![Tests](https://github.com/przemub/django-graphiql-strawberry-debug-toolbar/actions/workflows/test-suite.yml/badge.svg)](https://github.com/flavprzemub/django-graphiql-strawberry-debug-toolbarar/actions)\n[![Package version](https://img.shields.io/pypi/v/django-graphiql-strawberry-debug-toolbar.svg)](https://pypi.python.org/pypi/django-graphiql-strawberry-debug-toolbar)\n\n[Django Debug Toolbar](https://github.com/jazzband/django-debug-toolbar) for [GraphiQL](https://github.com/graphql/graphiql) IDE and [https://strawberry.rocks/](Strawberry) GraphQL server.\n\n![Graphiql Debug Toolbar](https://user-images.githubusercontent.com/5514990/36340937-1937ee68-1419-11e8-8477-40622e98c312.gif)\n\n## Dependencies\n\n* Python ≥ 3.6\n* Django ≥ 2.2\n* Strawberry ≥ 0.15.1\n\n## Installation\n\nInstall the last stable version from PyPI.\n\n```sh\npip install django-graphiql-strawberry-debug-toolbar\n````\n\nSee the [documentation](https://django-debug-toolbar.readthedocs.io/en/stable/installation.html) for further guidance on setting *Django Debug Toolbar*.\n\nAdd `graphiql_strawberry_debug_toolbar` to your *INSTALLED_APPS* settings:\n\n```py\nINSTALLED_APPS = [\n    'debug_toolbar',\n    'graphiql_strawberry_debug_toolbar',\n]\n```\n\n**Replace** the Django Debug Toolbar **middleware** with the GraphiQL Debug Toolbar one. \n\n```py\nMIDDLEWARE = [\n    # 'debug_toolbar.middleware.DebugToolbarMiddleware',\n    'graphiql_strawberry_debug_toolbar.middleware.DebugToolbarMiddleware',\n]\n```\n\nCredits to [@jazzband](https://jazzband.co) / [django-debug-toolbar](https://github.com/jazzband/django-debug-toolbar)\n and [@mongkok](https://github.com/mongkok), the author of [the orignal tool](https://github.com/flavors/django-graphiql-debug-toolbar) for graphene.\n\n",
    'author': 'mongkok',
    'author_email': 'dani@domake.io',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/przemub/django-graphiql-strawberry-debug-toolbar',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
