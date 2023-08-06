# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['mldictionary']

package_data = \
{'': ['*']}

install_requires = \
['bs4>=0.0.1,<0.0.2', 'requests==2.25.1']

setup_kwargs = {
    'name': 'mldictionary',
    'version': '0.2.6',
    'description': "word's dictionary for several languages",
    'long_description': '# MLDictionary\n\n## **MLDictionary** is word\'s dictionary for several language\n\n```python\n>>> from mldictionary import English\n>>> english_dictionary = English()\n>>> snake_means = english_dictionary.get_meanings(\'snake\')\n>>> len(snake_means)\n4\n>>> snake_means\n[\'a reptile with a long body and no legs: \' ...]\n...\n```\n\n<p align="center">\n    <a href="https://pypi.org/project/mldictionary/" target="_blank" align="center">\n        <img alt="PyPI" src="https://img.shields.io/pypi/v/mldictionary?color=%233f7&logo=pypi&style=plastic">    \n    </a>&nbsp;&nbsp;\n    <a href="https://pypi.org/project/mldictionary/" target="_blank" align="center">\n        <img alt="PyPI - License" src="https://img.shields.io/pypi/l/mldictionary?color=%237f7&logo=pypi&style=plastic">    \n    </a>&nbsp;&nbsp;\n    <a href="https://pypi.org/project/mldictionary/" target="_blank" align="center">\n<img alt="GitHub Workflow Status (event)" src="https://img.shields.io/github/workflow/status/pabloemidio/mldictionary/unittest?color=%233f7&label=tests&logo=pypi&style=plastic">\n    </a>&nbsp;&nbsp;\n    <a href="https://pypi.org/project/mldictionary/" target="_blank" align="center">\n        <img alt="PyPI - Downloads" src="https://img.shields.io/pypi/dm/mldictionary?color=%237f7&logo=pypi&style=plastic">    \n    </a>\n</p>\n\n---\n\n## **Installing MLDictionary** \n\n```console\n$ pip install mldictionary\n```\nMLDictionary officially supports 3.9+.\n\n---\n\n## Some examples\n\n```python\n>>> from mldictionary import Portuguese\n>>> portuguese_dictionary = Portuguese()\n>>> vida_means = portuguese_dictionary.get_meanings(\'vida\')\n>>> vida_means\n[\'Conjunto dos hábitos e costumes de alguém; maneira de viver: tinha uma vida de milionário.\' ...]\n>>> from mldictionary import Spanish\n>>> spanish_dictionary = Spanish()\n>>> coche_means = spanish_dictionary.get_meanings(\'coche\')\n>>> coche_means\n[\'Automóvil destinado al transporte de personas y con capacidad no superior a siete plazas.\' ...]\n```\n\n---\n\n### Make your own dictionary\n```python\nfrom mldictionary import Dictionary\n\nclass MyOwnDictionary(Dictionary):\n    url = \'somedictionary.com\'\n    language = \'language name\'\n    target_tag = \'tag_where_means_is\'\n    target_attr = {\'attr\': \'attr_value\'}\n    replaces = {\'something\', \'another thing\'}\n\n>>> myowndictionary = MyOwnDictionary()\n>>> myowndictionary.get_meanings(\'other language word\')\n```\nTo more details, see the [wiki](https://github.com/PabloEmidio/mldictionary/wiki)\n\nAlso, it has a insightful [article on linkedin](https://www.linkedin.com/pulse/mldictionary-pablo-em%25C3%25ADdio)\n',
    'author': 'Pablo Emidio',
    'author_email': 'p.emidiodev@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://pypi.org/project/mldictionary/',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
