# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['jinja2_workarounds']

package_data = \
{'': ['*']}

install_requires = \
['Jinja2>=3.0.3,<4.0.0']

setup_kwargs = {
    'name': 'jinja2-workarounds',
    'version': '0.1.0',
    'description': 'A jinja2 extension for includes with correct indentation',
    'long_description': "# 🦸\u200d♂️ Not the solution `jinja2` deserves, but the workaround it needs right now.\n`jinja2_workarounds` offers an extension for jinja2 that works around a long standing issue[^1]\nwhere `include` does not preserve correct indentation for multi-line includes. Simply add the\n`jinja2_workarounds.MultiLineInclude` [extension to your environment](https://jinja.palletsprojects.com/en/3.0.x/extensions/) and use the `indent content` directive to\ncorrectly indent your multi-line includes.\n\n## Installation\n```pip install jinja2_workarounds```\n\n\n## Usage example\n```jinja2\n# text.j2\nthis\nis \nsome \ntext\n```\n\n```jinja2\n# example.j2\nexample:\n    {% include 'text.j2' indent content %}\n```\n\nis then rendered as \n\n```\nexample:\n    this\n    is \n    some \n    text\n```\n\ncompared to `jinja2`'s default `include` which would result in \n\n```\nexample:\n    this\nis \nsome \ntext\n```\n\n## Advanced features\n`MultiLineInclude` is compatible with custom `block_start_string` and `block_end_string`. It also works with \nthe advanced features of `jinja2'`s `include` statement. The following variants are all supported and work as\nexpected\n\n```jinja2\n{% include 'missing.j2' ignore missing indent content %}  # handle missing templates\n{% include ['foo.j2', 'bar.j2'] indent content %}  # multiple alternative templates\n{% include 'child.j2' without context %}  # include child with/without content\n{%- include 'child.j2' +%}  # include with custom whitespace control\n```\n\n[^1]: https://github.com/pallets/jinja/issues/178",
    'author': 'Sascha Desch',
    'author_email': 'sascha.desch@hotmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
