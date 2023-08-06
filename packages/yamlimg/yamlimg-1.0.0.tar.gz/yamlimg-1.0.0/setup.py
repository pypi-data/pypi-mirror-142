# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['yamlimg', 'yamlimg.cli', 'yamlimg.impl']

package_data = \
{'': ['*']}

install_requires = \
['Pillow>=9.0.1,<10.0.0',
 'PyYAML>=6.0,<7.0',
 'pydantic>=1.9.0,<2.0.0',
 'typer>=0.4.0,<0.5.0']

entry_points = \
{'console_scripts': ['yamlimg = yamlimg.cli:app']}

setup_kwargs = {
    'name': 'yamlimg',
    'version': '1.0.0',
    'description': 'A way to store images in YAML.',
    'long_description': None,
    'author': 'vcokltfre',
    'author_email': 'vcokltfre@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/vcokltfre/yamlimg',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
