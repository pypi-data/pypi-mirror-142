# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['schema', 'schema.legacy']

package_data = \
{'': ['*']}

install_requires = \
['fhir.resources>=6.0,<7.0']

setup_kwargs = {
    'name': 'insight-engine-schema-python',
    'version': '0.3.20',
    'description': 'Rialtic insight engine schema in Python',
    'long_description': '# Rialtic insight engine schema in Python\n\nThis repo contains translation of InsightEngine Request/Response schema to Python.\nIt uses `fhir.resources` internally (see https://pypi.org/project/fhir.resources/).\n\n## Release to Nexus\n\nA GitHub workflow called `do_release_nexus` is also provided for this task. \n\nOn a local machine, you can do:\n\n1. Merge the `develop` branch into master\n2. Set environment variables\n\n```shell\nexport NEXUS_USERNAME=...\nexport NEXUS_PASSWORD=...\nexport RIALTIC_PRE_RELEASE=1\nexport NEXUS_LIBRARIES_PRE_RELEASE_UPSTREAM=https://artifacts.services.rialtic.dev/repository/internal-snapshot-python/\nexport NEXUS_LIBRARIES_UPSTREAM=https://artifacts.services.rialtic.dev/repository/libraries-python/\nexport NEXUS_DOWNSTREAM=https://artifacts.services.rialtic.dev/repository/libraries-group-python/simple/\n```\n\n3. Make sure you have configured the Nexus repositories in `poetry`:\n\n```shell\npoetry config repositories.nexus_libraries_upstream ${NEXUS_LIBRARIES_UPSTREAM}\npoetry config repositories.nexus_libraries_pre_release_upstream ${NEXUS_LIBRARIES_PRE_RELEASE_UPSTREAM}\npoetry config repositories.nexus_downstream ${NEXUS_DOWNSTREAM}\npoetry config http-basic.nexus_downstream ${NEXUS_USERNAME} ${NEXUS_PASSWORD}\n```\n\n(This step only needs to be done once for all repositories.)\n\n4. If you want to do a pre-release first, then run `make release`, \n   and it will release to repository `internal-snapshot-python` instead of `libraries-python`.\n5. Otherwise, run `RIALTIC_PRE_RELEASE=0 make release`\n',
    'author': 'Rialtic',
    'author_email': 'engines.data@rialtic.io',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://rialtic.io',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
