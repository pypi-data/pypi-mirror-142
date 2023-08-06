# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['ua']

package_data = \
{'': ['*']}

install_requires = \
['parse>=1.19.0,<2.0.0']

setup_kwargs = {
    'name': 'ua',
    'version': '0.1.5',
    'description': 'User-Agent parsing and creation',
    'long_description': "# ua\nUser-Agent parsing and creation\n\n## Installation\n```console\npip install ua\n```\n\n## Usage\n```python\n>>> import ua\n```\n\n### Parsing\n```python\n>>> user_agent = ua.parse('Mozilla/5.0 (X11; Linux x86_64; rv:88.0) Gecko/20100101 Firefox/88.0')\n>>>\n>>> user_agent\nUserAgent(\n    products=[\n        Product(name='Mozilla', version='5.0', comments=['X11', 'Linux x86_64', 'rv:88.0']),\n        Product(name='Gecko', version='20100101', comments=[]),\n        Product(name='Firefox', version='88.0', comments=[])\n    ]\n)\n>>>\n>>> str(user_agent)\n'Mozilla/5.0 (X11; Linux x86_64; rv:88.0) Gecko/20100101 Firefox/88.0'\n```\n\n### Creation\n```python\n>>> user_agent = ua.UserAgent(\n    products=[\n        ua.Product(\n            name='SomeProduct',\n            version='1.0',\n            comments=['SomeComment']\n        )\n    ]\n)\n>>>\n>>> str(user_agent)\n'SomeProduct/1.0 (SomeComment)'\n```\n\n## References\n* [User agent - Wikipedia](https://en.wikipedia.org/wiki/User_agent)\n* [User-Agent - HTTP | MDN](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/User-Agent)\n* [RFC 7231 - Hypertext Transfer Protocol (HTTP/1.1): Semantics and Content](https://datatracker.ietf.org/doc/html/rfc7231#section-5.5.3)",
    'author': 'Tom Bulled',
    'author_email': '26026015+tombulled@users.noreply.github.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/tombulled/ua',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
