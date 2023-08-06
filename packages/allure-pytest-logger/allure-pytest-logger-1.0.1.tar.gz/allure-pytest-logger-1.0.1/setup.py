# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['allure_pytest_logger']

package_data = \
{'': ['*']}

install_requires = \
['allure-pytest>=2.9.45,<3.0.0', 'pytest>=6.2.5,<7.0.0']

entry_points = \
{'pytest11': ['allure_pytest_logger = allure_pytest_logger.plugin']}

setup_kwargs = {
    'name': 'allure-pytest-logger',
    'version': '1.0.1',
    'description': 'PyTest Allure Logging Plugin',
    'long_description': 'PyTest Allure Logging Plugin\n============================\n\nPyTest plugin that allows you to attach logs to allure-report for failures only\n',
    'author': 'Sergey Demenok',
    'author_email': 'sergey.demenok@gmail.com',
    'maintainer': 'Sergey Demenok',
    'maintainer_email': 'sergey.demenok@gmail.com',
    'url': 'https://github.com/efpato/allure-pytest-logger',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
