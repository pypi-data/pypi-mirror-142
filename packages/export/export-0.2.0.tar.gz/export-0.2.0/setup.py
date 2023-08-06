# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['export']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'export',
    'version': '0.2.0',
    'description': 'Control module exports',
    'long_description': "# export\nControl module exports\n\n## About\nThis library dynamically generates an `__all__` attribute for modules\n\n## Usage\n\n### Private by Default\n*Does* export objects marked **public**, *doesn't* export everything else\n\n```python\n# lib.py\n\nimport export\n\nexport.init(default=export.PRIVATE)\n\n@export.public\ndef foo():\n    pass\n\ndef bar():\n    pass\n\ndef baz():\n    pass\n```\n\n```python\n>>> import lib\n>>> \n>>> lib.__all__\n['foo']\n```\n\n### Public by Default\n*Doesn't* export objects marked **private**, *does* export everything else\n\n```python\n# lib.py\n\nimport export\n\nexport.init(default=export.PUBLIC)\n\ndef foo():\n    pass\n\n@export.private\ndef bar():\n    pass\n\n@export.private\ndef baz():\n    pass\n```\n\n```python\n>>> import lib\n>>> \n>>> lib.__all__\n['export', 'foo']\n```",
    'author': 'Tom Bulled',
    'author_email': '26026015+tombulled@users.noreply.github.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/tombulled/export',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
