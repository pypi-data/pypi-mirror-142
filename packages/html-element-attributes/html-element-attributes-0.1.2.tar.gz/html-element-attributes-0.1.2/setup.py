# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['HtmlElementAttributes']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'html-element-attributes',
    'version': '0.1.2',
    'description': 'List of known HTML tag attributes',
    'long_description': '# HtmlElementAttributes\n\nPython port of npm package [html-element-attributes](https://www.npmjs.com/package/html-element-attributes).\n\nList of known HTML tag attribute names.\n\n## What is this?\n\nThis is a list of HTML tag attribute names.\n\n## Install\n\n```sh\npip install html-element-attributes\n```\n\n## Use\n\n```py\nfrom HtmlTagNames import html_element_attributes\n\nprint(html_element_attributes["*"])\n```\n\nYields:\n\n```py\n[\n  \'accesskey\',\n  \'autocapitalize\',\n  \'autofocus\',\n  \'class\',\n  // …\n  \'style\',\n  \'tabindex\',\n  \'title\',\n  \'translate\'\n]\n```\n## License\n\n[GPL][license] © Riverside Healthcare\nPorted from `html-element-attributes` [MIT][LICENSE] © [Titus Wormer][https://github.com/wooorm]\n\n[license]: LICENSE',
    'author': 'Christopher Pickering',
    'author_email': 'cpickering@rhc.net',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/Riverside-Healthcare/html-element-attributes',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
