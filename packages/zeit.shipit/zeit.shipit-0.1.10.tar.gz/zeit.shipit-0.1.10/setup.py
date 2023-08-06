# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['zeit', 'zeit.shipit', 'zeit.shipit.tests']

package_data = \
{'': ['*'], 'zeit.shipit.tests': ['mypackage/*', 'mypackage/k8s/*']}

install_requires = \
['click', 'tomli>=1.2.2,<2.0.0', 'towncrier']

setup_kwargs = {
    'name': 'zeit.shipit',
    'version': '0.1.10',
    'description': 'Python API for releasing and deploying software to containers',
    'long_description': 'None',
    'author': 'ZEIT Online',
    'author_email': 'zon-backend@zeit.de',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/ZeitOnline/zeit.shipit',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
