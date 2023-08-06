# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['gibbs_sampler']

package_data = \
{'': ['*']}

install_requires = \
['bio>=1.3.3,<2.0.0']

setup_kwargs = {
    'name': 'gibbs-sampler',
    'version': '0.1.0',
    'description': 'Gibbs Sampler for motif discovery',
    'long_description': '# gibbs_sampler\n\nGibbs Sampler for motif discovery\n\n## Installation\n\n```bash\n$ pip install gibbs_sampler\n```\n\n## Usage\n\n- TODO\n\n## Contributing\n\nInterested in contributing? Check out the contributing guidelines. Please note that this project is released with a Code of Conduct. By contributing to this project, you agree to abide by its terms.\n\n## License\n\n`gibbs_sampler` was created by Monty Python. It is licensed under the terms of the CC0 v1.0 Universal license.\n\n## Credits\n\n`gibbs_sampler` was created with [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) and the `py-pkgs-cookiecutter` [template](https://github.com/py-pkgs/py-pkgs-cookiecutter).\n',
    'author': 'Monty Python',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
