# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['girder_pytest_pyppeteer']

package_data = \
{'': ['*']}

install_requires = \
['pytest>=7.0.1,<8.0.0']

extras_require = \
{'test-app': ['celery>=5.2.3,<6.0.0',
              'Django>=4.0.2,<5.0.0',
              'django-allauth>=0.48.0,<0.49.0',
              'django-configurations[database,email]>=2.3.2,<3.0.0',
              'django-extensions>=3.1.5,<4.0.0',
              'django-filter>=21.1,<22.0',
              'django-oauth-toolkit>=1.7.0,<2.0.0',
              'djangorestframework>=3.13.1,<4.0.0',
              'drf-yasg>=1.20.0,<2.0.0']}

entry_points = \
{'console_scripts': ['pytest-docker = '
                     'girder_pytest_pyppeteer.main:run_pytest_docker_compose'],
 'pytest11': ['pyppeteer = girder_pytest_pyppeteer.plugin']}

setup_kwargs = {
    'name': 'girder-pytest-pyppeteer',
    'version': '0.0.1',
    'description': 'Pytest plugin for using pyppeteer to test Girder 4 applications',
    'long_description': None,
    'author': 'Daniel Chiquito',
    'author_email': 'daniel.chiquito@kitware.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
