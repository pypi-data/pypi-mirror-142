# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['mlpractice',
 'mlpractice.linear_classifier',
 'mlpractice.rnn_torch',
 'mlpractice.tests',
 'mlpractice.tests.linear_classifier',
 'mlpractice.tests.rnn_torch']

package_data = \
{'': ['*'],
 'mlpractice': ['templates/linear_classifier/*', 'templates/rnn_torch/*']}

install_requires = \
['ipython>=7.30.1,<8.0.0',
 'jupyter>=1.0.0,<2.0.0',
 'numpy>=1.21.4,<2.0.0',
 'scipy>=1.7.2,<2.0.0',
 'torch>=1.10.0,<2.0.0']

entry_points = \
{'console_scripts': ['mlpractice = mlpractice.cli:command_line']}

setup_kwargs = {
    'name': 'mlpractice',
    'version': '0.0.2',
    'description': 'MLpractice is a course, in which you will learn about the most effective machine learning techniques,and gain practice implementing them.',
    'long_description': '# <div align="center">MLpractice</div>\n<a href=\'https://mlpractice.readthedocs.io/en/latest/?badge=latest\'>\n    <img src=\'https://readthedocs.org/projects/mlpractice/badge/?version=latest\' alt=\'Documentation Status\' />\n</a>\n\nMLpractice 🚀 is a course, in which you will learn about the most effective machine learning techniques, and gain practice implementing them.\n\n## <div align="center">Documentation</div>\n\nSee the [MLpractice Docs](https://mlpractice.readthedocs.io/en/latest/?badge=latest) for full documentation on course task functions.\n\n## <div align="center">Quick Start</div>\n\n<details open>\n<summary>Install</summary>\n  \n### Pip\nPip install it in a [**Python>=3.7.0**](https://www.python.org/) environment.\n```bash\npip install mlpractice\n```\n\n<!-- ### Clone and install\nClone repo and install [requirements.txt](https://github.com/avalur/mlpractice/blob/main/requirements.txt) in a\n[**Python>=3.7.0**](https://www.python.org/) environment.\n\n```bash\ngit clone https://github.com/avalur/mlpractice  # clone\ncd mlpractice\npip install -r requirements.txt  # install\n``` -->\n\n</details>\n\n<details open>\n<summary>Init</summary>\n\nMake a course folder with tasks by simply running\n```bash\nmlpractice init\n```\n\n</details>\n\n## <div align="center">Contact</div>\n\nFor MLpractice bugs and feature requests please visit [GitHub Issues](https://github.com/avalur/mlpractice/issues).\n\n</div>\n',
    'author': 'Vladislav Ushakov',
    'author_email': 'uvd2001@mail.ru',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/avalur/mlpractice',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<=3.9',
}


setup(**setup_kwargs)
