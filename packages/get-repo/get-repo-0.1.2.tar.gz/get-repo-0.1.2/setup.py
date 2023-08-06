# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['get_repo']

package_data = \
{'': ['*']}

install_requires = \
['git-url-parse>=1.2.2,<2.0.0', 'typer>=0.4.0,<0.5.0']

entry_points = \
{'console_scripts': ['get-repo = get_repo.cli:main']}

setup_kwargs = {
    'name': 'get-repo',
    'version': '0.1.2',
    'description': 'Small cli utility for cloning git repos in an orderly manner',
    'long_description': "# get-repo\n> A small cli utility for cloning git repositories in an orderly manner.\n\n`get-repo` clones git repositories into `$HOME/source/{host}/{owner}/{repository-name}`\n\n## Installation\n\nOS X & Linux & Windows:\n\n```sh\npip install get-repo\n```\n\n## Usage example\n\n```sh\ngit-get https://github.com/florian42/get-repo.git\n```\n\n## Development setup\n\n- Install Python 3.x\n- Install [Poetry](https://python-poetry.org/docs/)\n\n```sh\npoetry install\npoetry run pre-commit install\npoetry run pre-commit run --all-files\n```\n\n## Release History\n* 0.1.2\n    * Initial Release\n\n## Meta\n\nFlorian Aumeier – hey@flo.fish\n\nDistributed under the MIT license. See ``LICENSE`` for more information.\n\n[https://github.com/florian42/get-repo](https://github.com/florian42)\n\n## Contributing\n\n1. Fork it (<https://github.com/florian42/get-repo/fork>)\n2. Create your feature branch (`git checkout -b feature/fooBar`)\n3. Commit your changes (`git commit -am 'Add some fooBar'`)\n4. Push to the branch (`git push origin feature/fooBar`)\n5. Create a new Pull Request\n",
    'author': 'Florian',
    'author_email': 'hey@flo.fish',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/florian42/get-repo',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
