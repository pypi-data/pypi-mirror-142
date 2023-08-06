# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['datacards']

package_data = \
{'': ['*']}

install_requires = \
['Markdown>=3.3.6,<4.0.0',
 'datasets>=1.14.0,<2.0.0',
 'pydantic>=1.8.0,<2.0.0',
 'requests>=2.27.1,<3.0.0',
 'rich[jupyter]>=10.14.0,<11.0.0',
 'wget>=3.2,<4.0']

setup_kwargs = {
    'name': 'datacards',
    'version': '0.1.0',
    'description': 'Append missing model cards to Huggingface datasets',
    'long_description': '# Datacard\n\nThis repo aims to find and update the missing model cards for Huggingface datasets.\n\nThe goal is to run the script once, manually update and review the files and datasets proposed and make a PR to the datasets repo.\n\n## WIP\n\n- [ ] Look into tools for Github and HF hub. Maybe create PR on new change or release?\n- [ ] Look into strategies for parsing\n      https://www.digitalocean.com/community/tutorials/how-to-use-python-markdown-to-convert-markdown-text-to-html\n\n- [ ] Look into how to provide multiple answers in model card (ex. Glue dataset)\n',
    'author': 'MarkusSagen',
    'author_email': 'markus.john.sagen@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/Hugging-Face-Supporter/datacards',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
