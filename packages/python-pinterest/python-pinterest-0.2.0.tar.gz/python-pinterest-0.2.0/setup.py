# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pinterest',
 'pinterest.asynchronous',
 'pinterest.models',
 'pinterest.sync',
 'pinterest.utils']

package_data = \
{'': ['*']}

install_requires = \
['Authlib>=0.15.5,<0.16.0', 'dataclasses-json>=0.5.6,<0.6.0', 'httpx==0.22.0']

setup_kwargs = {
    'name': 'python-pinterest',
    'version': '0.2.0',
    'description': 'A simple Python wrapper for Pinterest REST API (Beta) (5.x) ✨ 🍰 ✨',
    'long_description': '================\npython-pinterest\n================\n\nA simple Python wrapper for Pinterest REST API (Beta) (5.x) ✨ 🍰 ✨\n\n.. image:: https://github.com/sns-sdks/python-pinterest/workflows/Test/badge.svg\n    :target: https://github.com/sns-sdks/python-pinterest/actions\n\n.. image:: https://codecov.io/gh/sns-sdks/python-pinterest/branch/main/graph/badge.svg\n    :target: https://codecov.io/gh/sns-sdks/python-pinterest\n\n\nIntroduction\n============\n\nThis library provides a service to easily use Pinterest REST API for v5.x.\n\nAnd support ``Async`` And ``sync`` mode.\n\nMore docs has published on https://sns-sdks.lkhardy.cn/python-pinterest/\n\nUsing\n=====\n\nThe API is exposed via the ``pinterest.Api`` class and ``pinterest.AsyncApi`` class.\n\nINSTANTIATE\n-----------\n\nYou can initial an instance with ``access token``::\n\n    # Sync\n    >>> from pinterest import Api\n    >>> p = Api(access_token="Your access token")\n    # Async\n    >>> from pinterest import AsyncApi\n    >>> ap = AsyncApi(access_token="Your access token")\n\nUsage\n-----\n\nGet pin info::\n\n    # Sync\n    >>> p.pins.get(pin_id="1022106077902810180")\n    # Pin(id=\'1022106077902810180\', created_at=\'2022-02-14T02:54:38\')\n    # Async\n    >>> await ap.pins.get(pin_id="1022106077902810180")\n    # Pin(id=\'1022106077902810180\', created_at=\'2022-02-14T02:54:38\')\n\nMore docs has published on https://sns-sdks.lkhardy.cn/python-pinterest/\n\nTODO\n====\n\n- Tests',
    'author': 'ikaroskun',
    'author_email': 'merle.liukun@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/sns-sdks/python-pinterest',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6.2,<4.0.0',
}


setup(**setup_kwargs)
