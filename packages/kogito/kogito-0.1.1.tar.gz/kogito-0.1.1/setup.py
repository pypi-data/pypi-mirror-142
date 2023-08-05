# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['kogito',
 'kogito.core',
 'kogito.models',
 'kogito.models.bart',
 'kogito.models.gpt2']

package_data = \
{'': ['*']}

install_requires = \
['git-python==1.0.3',
 'inflect>=5.3.0,<5.4.0',
 'pandas>=1.3.5,<1.4.0',
 'pytextrank>=3.2.2,<3.3.0',
 'pytorch-lightning==0.8.5',
 'rouge-score>=0.0.4,<0.1.0',
 'sacrebleu>=2.0.0,<2.1.0',
 'spacy>=3.2.3,<3.3.0',
 'torch>=1.10.1,<1.11.0',
 'transformers>=4.15.0,<4.16.0',
 'wandb>=0.12.9,<0.13.0']

setup_kwargs = {
    'name': 'kogito',
    'version': '0.1.1',
    'description': 'A Python NLP Commonsense Reasoning library',
    'long_description': '# kogito\nA Python NLP Commonsense Reasoning library\n',
    'author': 'Mete Ismayil',
    'author_email': 'mahammad.ismayilzada@epfl.ch',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/mismayil/kogito',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<3.11',
}


setup(**setup_kwargs)
