# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['thunderstruck']

package_data = \
{'': ['*']}

install_requires = \
['ray>=1.11.0,<2.0.0']

setup_kwargs = {
    'name': 'thunderstruck',
    'version': '0.0.1',
    'description': 'CDP based on ray.io',
    'long_description': '# Thunderstruck\n\n![deploy](https://github.com/afranzi/thunderstruck/actions/workflows/ci-deploy.yml/badge.svg?branch=main)\n![standard-checks](https://github.com/afranzi/thunderstruck/actions/workflows/ci-standard-checks.yml/badge.svg?branch=main)\n![tests](https://github.com/afranzi/thunderstruck/actions/workflows/ci-test.yml/badge.svg?branch=main)\n\n> `Thunderstruck` aims to simplify the CDP development by providing a modular approach to forward events into different \n> destinations.\n\n## Roadmap\n\n- [x] : Prepare skeleton & workflows.\n- [ ] : Event ingest server\n- [ ] : Event persistence in Postgres DB\n- [ ] : K8s Helm.\n- [ ] : Event Transformation + Forwarding with modules.',
    'author': 'Data Platform',
    'author_email': 'data.platform@typeform.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/afranzi/thunderstruck',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
