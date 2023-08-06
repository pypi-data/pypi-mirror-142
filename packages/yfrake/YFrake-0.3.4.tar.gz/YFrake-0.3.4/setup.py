# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['yfrake',
 'yfrake.client',
 'yfrake.openapi',
 'yfrake.openapi.specs',
 'yfrake.server']

package_data = \
{'': ['*']}

install_requires = \
['aiohttp-cors>=0.7,<0.8',
 'aiohttp-swagger3>=0.7,<0.8',
 'aiohttp>=3.8,<3.9',
 'psutil>=5.9,<5.10',
 'pyyaml>=6.0,<6.1',
 'tomli>=2.0,<2.1']

entry_points = \
{'console_scripts': ['gen-spec = '
                     'yfrake.openapi.generator:generate_openapi_spec']}

setup_kwargs = {
    'name': 'yfrake',
    'version': '0.3.4',
    'description': 'A flexible and agile stock market data scraper and server.',
    'long_description': '# YFrake\n\n<a target="new" href="https://pypi.python.org/pypi/yfrake"><img border=0 src="https://img.shields.io/badge/python-3.10+-blue.svg?label=python" alt="Supported Python versions"></a>\n<a target="new" href="https://pypi.python.org/pypi/yfrake"><img border=0 src="https://img.shields.io/pypi/v/yfrake?label=version" alt="Package version on PyPI"></a>\n<a target="new" href="https://www.codefactor.io/repository/github/aspenforest/yfrake"><img border=0 src="https://img.shields.io/codefactor/grade/github/aspenforest/yfrake?label=code quality" alt="CodeFactor code quality"></a>\n<a target="new" href="https://scrutinizer-ci.com/g/aspenforest/yfrake/"><img border=0 src="https://img.shields.io/scrutinizer/build/g/aspenforest/yfrake" alt="Scrutinizer build inspection"></a>\n<a target="new" href="https://app.codecov.io/gh/aspenforest/yfrake"><img border=0 src="https://img.shields.io/codecov/c/github/aspenforest/yfrake" alt="Code coverage"></a> \n<br />\n<a target="new" href="https://pypi.python.org/pypi/yfrake"><img border=0 src="https://img.shields.io/pypi/dm/yfrake?label=installs" alt="Installs per month"></a>\n<a target="new" href="https://github.com/aspenforest/yfrake/issues"><img border=0 src="https://img.shields.io/github/issues/aspenforest/yfrake" alt="Issues on Github"></a>\n<a target="new" href="https://github.com/aspenforest/yfrake/blob/main/LICENSE"><img border=0 src="https://img.shields.io/github/license/aspenforest/yfrake" alt="License on GitHub"></a>\n<a target="new" href="https://github.com/aspenforest/yfrake/stargazers"><img border=0 src="https://img.shields.io/github/stars/aspenforest/yfrake?style=social" alt="Stars on GitHub"></a>\n<a target="new" href="https://twitter.com/aabmets"><img border=0 src="https://img.shields.io/twitter/url?style=social&url=https%3A%2F%2Ftwitter.com%2Faabmets&label=Say%20Thanks" alt="Say thanks on Twitter"></a>\n\n\n\n\n### Disclaimer\nThe current version of YFrake is usable, but ***not*** production ready.\n\n### Description\nYFrake is a ***flexible*** and ***agile*** stock market data scraper and server [&#91;note1&#93;](#footnote1).\nIt enables developers to build powerful apps without having to worry about maximizing network request throughput [&#91;note2&#93;](#footnote1).\nYFrake can be used as a client to directly return market data or as a ***programmatically controllable server*** to forward data to web clients.\nIn addition, all network requests by YFrake are ***non-blocking***, which means that your program can continue running your code while network requests are in progress.\nThe best part about YFrake is its ***built-in swagger API documentation*** which you can use to perform test queries and examine the returned responses.\n\n\n### Getting started\nHow to install yfrake:\n~~~\npip install yfrake\n~~~\nHow to import yfrake:\n~~~\nfrom yfrake import client, server\n~~~\n\n### Server examples\nHow to run the server with default settings:\n~~~\nserver.start()\n# do other stuff\nserver.stop()\n~~~\nHow to run the server with custom settings:\n~~~\nsettings = dict(\n    host=\'localhost\',\n    port=8888,\n    limit=100,\n    timeout=1,\n    backlog=200\n)\nserver.start(**settings)\n# do other stuff\nserver.stop()\n~~~\n\n\n### Sync execution examples\nHow to continue the current function while checking for response status:\n~~~\nfrom yfrake import client\n\n@client.configure(limit=100, timeout=1)\ndef main()\n    resp = client.get(\'quote_type\', symbol=\'msft\')\n    \n    while not resp.available():\n        # do other stuff\n        \n    if not resp.error:\n        print(resp.endpoint)\n        print(resp.data)\n    \nif __name__ == \'__main__\':\n    main()\n~~~\nHow to pause the current function to wait for the result:\n~~~\nfrom yfrake import client\n\n@client.configure(limit=100, timeout=1)\ndef main()\n    resp = client.get(\'quote_type\', symbol=\'msft\')\n    \n    resp.wait_for_result()\n    \n    if not resp.error:\n        print(resp.endpoint)\n        print(resp.data)\n    \nif __name__ == \'__main__\':\n    main()\n~~~\nHow to run multiple queries concurrently:\n~~~\nfrom yfrake import client\nimport time\n\n@client.configure(limit=100, timeout=1)\ndef main()\n    def save_result(obj):\n        resp = in_progress.pop(obj)\n        resp.wait_for_result()\n        results.append(resp)\n\n    in_progress = dict()\n    results = list()\n    args_list = [\n        dict(endpoint=\'quote_type\', symbol=\'msft\'),\n        dict(endpoint=\'price_overview\', symbol=\'aapl\')\n    ]\n    for args_dict in args_list:\n        resp = client.get(**args_dict)\n        obj = resp.get_async_object()\n        obj.add_done_callback(save_result)\n        in_progress[obj] = resp\n\n    while in_progress:\n        time.sleep(0)\n    for resp in results:\n        if not resp.error:\n            print(resp.endpoint)\n            print(resp.data)\n    \nif __name__ == \'__main__\':\n    main()\n~~~\n\n### Async execution examples\nHow to continue the current coroutine while checking for response status:\n~~~\nfrom yfrake import client\nimport asyncio\n\n@client.configure(limit=100, timeout=1)\nasync def main():\n    resp = client.get(\'quote_type\', symbol=\'msft\')\n    \n    while not resp.available():\n        # do other stuff\n        \n    if not resp.error:\n        print(resp.endpoint)\n        print(resp.data)\n\nif __name__ == \'__main__\':\n    asyncio.run(main())\n~~~\nHow to pause the current coroutine to await for the result:\n~~~\nfrom yfrake import client\nimport asyncio\n\n@client.configure(limit=100, timeout=1)\nasync def main():\n    resp = client.get(\'quote_type\', symbol=\'msft\')\n    \n    await resp.result()\n    \n    if not resp.error:\n        print(resp.endpoint)\n        print(resp.data)\n\nif __name__ == \'__main__\':\n    asyncio.run(main())\n~~~\nHow to run multiple queries concurrently:\n~~~\nfrom yfrake import client\nimport asyncio\n\n@client.configure(limit=100, timeout=1)\nasync def main():\n    args_list = [\n        dict(endpoint=\'quote_type\', symbol=\'msft\'),\n        dict(endpoint=\'price_overview\', symbol=\'aapl\')\n    ]\n    tasks_list = []\n    for args_dict in args_list:\n        resp = client.get(**args_dict)\n        obj = resp.get_async_object()\n        tasks_list.append(obj)\n\n    results = await asyncio.gather(*tasks_list)\n    for resp in results:\n        if not resp.error:\n            print(resp.endpoint)\n            print(resp.data)\n\nif __name__ == \'__main__\':\n    asyncio.run(main())\n~~~\n\n<br/>\n<a id="footnote1"><sup>&#91;note1&#93;:</sup></a> Stock market data is sourced from Yahoo Finance. <br/>\n<a id="footnote2"><sup>&#91;note2&#93;:</sup></a> You still need to know how to correctly use asyncio.\n',
    'author': 'Mattias Aabmets',
    'author_email': 'mattias.aabmets@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
