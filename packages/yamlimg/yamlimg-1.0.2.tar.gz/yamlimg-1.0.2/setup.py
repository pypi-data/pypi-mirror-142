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
    'version': '1.0.2',
    'description': 'A way to store images in YAML.',
    'long_description': '# YAMLImg\n\nA way to store images in YAML.\n\nI made this after seeing [Roadcrosser\'s JSON-G](https://github.com/Roadcrosser/JSON-G) because it was too inspiring to ignore this opportunity.\n\n![Lint](https://github.com/vcokltfre/yamlimg/actions/workflows/lint.yml/badge.svg)\n\n## Installation\n\n```sh\npip install yamlimg\n```\n\nor from GitHub\n\n```sh\npip install git+https://github.com/vcokltfre/yamlimg\n```\n\n## Usage\n\nDumping an image:\n\n```sh\nyamlimg dump <image> [--output=output.yaml]\n```\n\nLoading an image:\n\n```sh\nyamlimg load <image> [--output=image.png]\n```\n\nUsing the programmatic API:\n\n```py\nfrom PIL import Image\nfrom yamlimg import yaml_to_image, image_to_yaml\n\n# Open an image\nimage = Image.open("image.png")\n\n# Convert the image to yaml\nyaml = image_to_yaml(image)\n\n# Convert the yaml back to an image\nimage = yaml_to_image(yaml)\n```\n\n## Note\n\nThere is no point in using this. It was made as a joke and I implore you not to ever actually use this for anything other than a joke.\n',
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
