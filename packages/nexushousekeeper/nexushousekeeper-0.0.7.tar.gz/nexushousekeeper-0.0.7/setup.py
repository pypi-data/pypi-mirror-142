# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': '.'}

packages = \
['nexushousekeeper']

package_data = \
{'': ['*']}

install_requires = \
['hurry.filesize==0.9',
 'requests==2.25.0',
 'requests_futures==1.0.0',
 'rich>=9.4.0,<10.0.0']

entry_points = \
{'console_scripts': ['nexushousekeeper = '
                     'nexushousekeeper.nexushousekeeper:main']}

setup_kwargs = {
    'name': 'nexushousekeeper',
    'version': '0.0.7',
    'description': 'A module to keep a nexus directory clean',
    'long_description': "# Nexus House Keeper\n\nThis project helps nexus users to clean their repository deleting old or unused component\n\n## Requirements:\n* Python 3\n\n## Installation\nNexus House Keeper can be downloaded from pypi\n\n``\npip install nexushousekeeper\n``\n\n### Print help :\n```\nnexushousekeeper -h\n```\n\n### Remove all components with versions matching a pattern\n\n``\nnexushousekeeper -u NEXUS_USER -p NEXUS_PASSWORD -r REPOSITORY --nexus-url NEXUS_URL --version-match 1.1.*\n``\n\nThis command remove all versions beginning with 1.1\n\n### Remove all components with the exact version\n\n``\nnexushousekeeper -u NEXUS_USER -p NEXUS_PASSWORD -r REPOSITORY --nexus-url NEXUS_URL --version 1.1-SNAPSHOT\n``\n\nThis command remove all components with version 1.1-SNAPSHOT\n\n### dry run\nDon't perform deletion but display which element should be deleted\n``\nnexushousekeeper -u NEXUS_USER -p NEXUS_PASSWORD -r REPOSITORY --nexus-url NEXUS_URL --version-match 1.1.* --dryrun\n``\n\n### display each version for each component\n\n``\nnexushousekeeper -u NEXUS_USER -p NEXUS_PASSWORD -r REPOSITORY --nexus-url NEXUS_URL -s\n``\n\n## Contributing\n\n## Install\n\n``\npoetry install\n``\n\n## Run tests\n\n``\npoetry run pytest\n``\n\n## Build Project\n\n``\npoetry build\n``\n\n## Deploy to pypi\n* testpypi\n\n``\npoetry publish -r testpypi \n``",
    'author': 'Benjamin Raimondi',
    'author_email': 'benjamin.raimondi@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/benDeMtp/NexusHouseKeeper',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
