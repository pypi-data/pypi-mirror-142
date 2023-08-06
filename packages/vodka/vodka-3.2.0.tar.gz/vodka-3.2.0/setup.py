# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['vodka',
 'vodka.config',
 'vodka.data',
 'vodka.plugins',
 'vodka.resources.blank_app',
 'vodka.resources.blank_app.plugins',
 'vodka.runners']

package_data = \
{'': ['*']}

install_requires = \
['click', 'munge>=1,<2', 'pluginmgr>=1,<2', 'tmpl>=1,<2']

entry_points = \
{'console_scripts': ['bartender = vodka.bartender:bartender']}

setup_kwargs = {
    'name': 'vodka',
    'version': '3.2.0',
    'description': 'plugin based real-time web service daemon',
    'long_description': '# vodka\n\n[![PyPI](https://img.shields.io/pypi/v/vodka.svg?maxAge=600)](https://pypi.python.org/pypi/vodka)\n[![Tests](https://github.com/20c/vodka/workflows/tests/badge.svg)](https://github.com/20c/vodka)\n[![Codecov](https://img.shields.io/codecov/c/github/20c/vodka/master.svg?maxAge=600)](https://codecov.io/github/20c/vodka)\n\nvodka is a plugin based real-time web service daemon.\n\n### Install\n\n```sh\npip install vodka\n```\n\n### Documentation (work in progress)\n\nhttp://vodka.readthedocs.io/\n\n### License\n\nCopyright 2016-2019 20C, LLC\n\nLicensed under the Apache License, Version 2.0 (the "License");\nyou may not use this software except in compliance with the License.\nYou may obtain a copy of the License at\n\n   http://www.apache.org/licenses/LICENSE-2.0\n\nUnless required by applicable law or agreed to in writing, software\ndistributed under the License is distributed on an "AS IS" BASIS,\nWITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\nSee the License for the specific language governing permissions and\nlimitations under the License.\n',
    'author': '20C',
    'author_email': 'code@20c.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/20c/vodka',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
