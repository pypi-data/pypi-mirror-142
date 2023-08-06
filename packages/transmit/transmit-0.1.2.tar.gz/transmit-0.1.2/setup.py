# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['transmit', 'transmit.trans']

package_data = \
{'': ['*']}

install_requires = \
['thrift>=0.15.0,<0.16.0']

setup_kwargs = {
    'name': 'transmit',
    'version': '0.1.2',
    'description': 'Transmit Server & Client use thrift',
    'long_description': '# Transmit Server & Client\n\n## Install\n```\npip install transmit\n```\n\n## Usage\n\n### Server\n```\nfrom server import Server\n\nclass TestServer(Server):\n    def __init__(self,port=18100):\n        super().__init__(port)\n\n    def test_function(self,msg):\n        print(\'Testing:\',msg)\n        return {"say":"Happy everyday!!!"}\n\nif __name__ == \'__main__\':\n    ts = TestServer()\n    ts.run()\n\n```\n> Result\n\n```shell\nstart python server 0.0.0.0:18100\n\n```\n#### Success Response\n```\n{\n    "code":1,\n    "msg":"success",\n    "data":"handle result data. AnyType"\n}\n```\n#### Error Response\n```\n{\n    "code":0,\n    "msg":"error message",\n    "data":{}\n}\n```\n\n\n### Client\n```\nfrom client import Client\n\nwith Client("127.0.0.1",18100) as c:\n    result = c.test_function({"msg":"hello world"})\n    print(type(result))\n    print(result)\n\n```\n> Result\n\n```shell\n<class \'str\'>\n{\n "code": 1,\n "msg": "success",\n "data": {\n  "say": "Happy everyday!!!"\n }\n}\n```\n\n### Refs\n[Thrift](https://thrift.apache.org/)\n',
    'author': 'hbh112233abc',
    'author_email': 'hbh112233abc@163.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/hbh112233abc/py-transmit',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
