# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pynblint']

package_data = \
{'': ['*']}

install_requires = \
['GitPython>=3.1.26,<4.0.0',
 'ipython<8',
 'nbconvert>=6.4.0,<7.0.0',
 'nbformat>=5.1.3,<6.0.0',
 'pydantic[dotenv]>=1.9.0,<2.0.0',
 'rich>=11.1.0,<12.0.0',
 'typer>=0.4.0,<0.5.0']

entry_points = \
{'console_scripts': ['pynblint = pynblint.main:app']}

setup_kwargs = {
    'name': 'pynblint',
    'version': '0.1.3',
    'description': 'A linter for Jupyter notebooks written in Python.',
    'long_description': '# Pynblint\n\n[![CI](https://github.com/collab-uniba/pynblint/actions/workflows/CI.yml/badge.svg)](https://github.com/collab-uniba/pynblint/actions/workflows/CI.yml)\n[![Documentation Status](https://readthedocs.org/projects/pynblint/badge/?version=latest)](https://pynblint.readthedocs.io/en/latest/?badge=latest)\n[![codecov](https://codecov.io/gh/collab-uniba/pynblint/branch/master/graph/badge.svg?token=CSX10BJ1CU)](https://codecov.io/gh/collab-uniba/pynblint)\n[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)\n[![code style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)\n\nMany professional data scientists use Jupyter Notebook to accomplish their daily tasks, from preliminary data exploration to model prototyping. Notebooks\' interactivity is particularly convenient for data-centric programming; moreover, their self-documenting nature greatly simplifies and enhances the communication of analytical results.\n\nHowever, Jupyter Notebook has often been criticized for offering scarce native support for Software Engineering best practices and inducing bad programming habits. To really benefit from computational notebooks, practitioners need to be aware of their common pitfalls and learn how to avoid them.\n\nIn our paper ["Eliciting Best Practices for Collaboration with Computational Notebooks" [1]](https://arxiv.org/abs/2202.07233), we introduced a catalog of validated best practices for the collaborative use of notebooks in professional contexts.\n\nTo raise awareness of these best practices and promote their adoption, we have created Pynblint, a static analysis tool for Jupyter notebooks written in Python. Pynblint can be operated as a standalone CLI application or as part of a CI/CD pipeline. It reveals potential defects of Jupyter notebooks found in software repositories and recommends corrective actions.\n\nThe core linting rules that power Pynblint have been derived as operationalizations of the validated best practices from our catalog. Nonetheless, the tool is designed to be easily customized and extended with new rules.\n\n## Catalog of best practices\n\n- Use version control\n- Manage project dependencies\n- Use self-contained environments\n- Put imports at the beginning\n- Ensure re-executability (re-run notebooks top to bottom)\n- Modularize your code\n- Test your code\n- Name your notebooks consistently\n- Stick to coding standards\n- Use relative paths\n- Document your analysis\n- Leverage Markdown headings to structure your notebook\n- Keep your notebook clean\n- Keep your notebook concise\n- Distinguish production and development artifacts\n- Make your notebooks available\n- Make your data available\n\n## Installation\n\nTo use Pynblint, clone this repository and install it with [Poetry](https://python-poetry.org):\n\n```bash\npoetry install --no-dev\n```\n\nTo install Pynblint for development purposes, simply omit the `--no-dev` option:\n\n```bash\npoetry install\n```\n\nAt present, we are finalizing the first version of Pynblint (v0.1.0).\nWhen released, it will become available as a Python package on PyPI and installable via `pip`.\n\n\n## Usage\n\nOnce installed, Pynblint can be used to analyze:\n\n- a single notebook:\n\n    ```bash\n    pynblint path/to/the/notebook.ipynb\n    ```\n- the set of notebooks found in the current working directory:\n\n    ```bash\n    pynblint .\n    ```\n\n- the set of notebooks found in the directory located at the specified path:\n\n    ```bash\n    pynblint path/to/the/project/dir/\n    ```\n\n- the set of notebooks found in a compressed `.zip` archive:\n\n    ```bash\n    pynblint path/to/the/compressed/archive.zip\n    ```\n\n- the set of notebooks found in a _public_ GitHub repository (support for private repositories is on our roadmap 🙂):\n\n    ```bash\n    pynblint --from-github https://github.com/collab-uniba/pynblint\n    ```\n\nFor further information on the available options, please read Pynblint\'s CLI manual:\n\n```bash\npynblint --help\n```\n\n## References\n\nLuigi Quaranta, Fabio Calefato, and Filippo Lanubile. 2022. [Eliciting Best Practices for Collaboration with Computational Notebooks.](https://arxiv.org/abs/2202.07233) *Proc. ACM Hum.-Comput. Interact.* 6, CSCW1, Article 87 (April 2022), 41 pages. <https://doi.org/10.1145/3512934>\n',
    'author': 'Luigi Quaranta',
    'author_email': 'luigi.quaranta@uniba.it',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://pynblint.readthedocs.io/en/latest/',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
