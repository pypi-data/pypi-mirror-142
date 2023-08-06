# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['nnrl',
 'nnrl.distributions',
 'nnrl.nn',
 'nnrl.nn.actor',
 'nnrl.nn.actor.policy',
 'nnrl.nn.critic',
 'nnrl.nn.distributions',
 'nnrl.nn.distributions.flows',
 'nnrl.nn.model',
 'nnrl.nn.model.stochastic',
 'nnrl.nn.modules',
 'nnrl.nn.networks',
 'nnrl.optim',
 'tests',
 'tests.nn',
 'tests.nn.actor',
 'tests.nn.actor.policy',
 'tests.nn.critic',
 'tests.nn.distributions',
 'tests.nn.distributions.flows',
 'tests.nn.model',
 'tests.nn.model.stochastic',
 'tests.nn.modules',
 'tests.nn.networks',
 'tests.optim']

package_data = \
{'': ['*']}

install_requires = \
['dataclasses-json>=0.5.4,<0.6.0', 'gym>=0.23.0,<0.24.0', 'torch>=1.9.0,<2.0.0']

setup_kwargs = {
    'name': 'nnrl',
    'version': '0.1.1',
    'description': 'Top-level package for NN RL.',
    'long_description': '=====\nNN RL\n=====\n\n\n.. image:: https://img.shields.io/pypi/v/nnrl.svg\n        :target: https://pypi.python.org/pypi/nnrl\n\n.. image:: https://img.shields.io/travis/angelolovatto/nnrl.svg\n        :target: https://travis-ci.com/angelolovatto/nnrl\n\n.. image:: https://readthedocs.org/projects/nnrl/badge/?version=latest\n        :target: https://nnrl.readthedocs.io/en/latest/?badge=latest\n        :alt: Documentation Status\n\n\nNeural Networks and utilities for Reinforcement Learning in PyTorch\n\n\n* Free software: MIT\n* Documentation: https://nnrl.readthedocs.io.\n\n\nFeatures\n--------\n\n* TODO\n\nCredits\n-------\n\nThis package was created with Cookiecutter_ and the `briggySmalls/cookiecutter-pypackage`_ project template.\n\n.. _Cookiecutter: https://github.com/audreyr/cookiecutter\n.. _`briggySmalls/cookiecutter-pypackage`: https://github.com/briggySmalls/cookiecutter-pypackage\n',
    'author': 'Ângelo Gregório Lovatto',
    'author_email': 'angelolovatto@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/angelolovatto/nnrl',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7',
}


setup(**setup_kwargs)
