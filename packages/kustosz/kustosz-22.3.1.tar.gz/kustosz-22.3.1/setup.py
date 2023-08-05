# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['kustosz',
 'kustosz.cli',
 'kustosz.fetchers',
 'kustosz.forms',
 'kustosz.management',
 'kustosz.management.commands',
 'kustosz.migrations',
 'kustosz.tasks',
 'kustosz.third_party',
 'kustosz.third_party.taggit_serializer',
 'kustosz.utils']

package_data = \
{'': ['*']}

install_requires = \
['Django>=3.2.12,<4.0.0',
 'Unalix>=0.9,<0.10',
 'celery>=5.2.3,<6.0.0',
 'django-celery-beat>=2.2.1,<3.0.0',
 'django-celery-results>=2.2.0,<3.0.0',
 'django-cors-headers>=3.11.0,<4.0.0',
 'django-extensions>=3.1.5,<4.0.0',
 'django-filter>=21.1,<22.0',
 'django-taggit-serializer>=0.1.7,<0.2.0',
 'django-taggit>=2.1.0,<3.0.0',
 'djangorestframework>=3.13.1,<4.0.0',
 'dynaconf[yaml]>=3.1.7,<4.0.0',
 'hyperlink>=21.0.0,<22.0.0',
 'listparser>=0.18,<0.19',
 'readability-lxml>=0.8.1,<0.9.0',
 'reader>=2.8,<3.0',
 'requests-cache>=0.9.1,<0.10.0']

extras_require = \
{'container': ['gunicorn>=20.1.0,<21.0.0',
               'psycopg2>=2.9.3,<3.0.0',
               'redis>=4.1.4,<5.0.0',
               'whitenoise>=6.0.0,<7.0.0'],
 'redis': ['redis>=4.1.4,<5.0.0']}

entry_points = \
{'console_scripts': ['kustosz-manager = kustosz.cli.manage:main']}

setup_kwargs = {
    'name': 'kustosz',
    'version': '22.3.1',
    'description': 'Focus on the worthwhile content with Kustosz, open source self-hosted web application. This package contains backend server.',
    'long_description': '# Kustosz - backend server repository\n\nFocus on the worthwhile content with Kustosz, open source self-hosted web application.\n\nThis repository contains backend server.\n\n## Installation\n\n```\npython manage.py makemigrations kustosz\npython manage.py migrate\npython manage.py createcachetable\npython manage.py createsuperuser --username admin --email admin@example.invalid\n```\n\n## License\n\nKustosz is distributed under terms of [European Union Public Licence](https://joinup.ec.europa.eu/collection/eupl/eupl-text-eupl-12)\n',
    'author': 'Mirek Długosz',
    'author_email': 'mirek@mirekdlugosz.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/KustoszApp/server/',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
