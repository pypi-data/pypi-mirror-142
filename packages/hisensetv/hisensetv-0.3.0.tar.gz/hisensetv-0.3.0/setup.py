# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['hisensetv']

package_data = \
{'': ['*']}

install_requires = \
['paho-mqtt>=1.5,<2.0']

entry_points = \
{'console_scripts': ['hisensetv = hisensetv.__main__:main']}

setup_kwargs = {
    'name': 'hisensetv',
    'version': '0.3.0',
    'description': 'MQTT interface to Hisense televisions.',
    'long_description': 'Python API for Hisense Televisions\n##################################\n\n|Build Status| |Black| |PyPi Version| |docs|\n\nA work-in-progress python API for Hisense televisions based off of `mqtt-hisensetv`_.\n\nInstallation\n************\n\nLinux\n=====\n.. code:: bash\n\n    sudo -H python3.8 -m pip install hisensetv\n\nWindows\n=======\n.. code:: bash\n\n    py -3.8 -m pip install hisensetv\n\nCLI Usage\n*********\n::\n\n    usage: hisensetv [-h] [--authorize] [--get {sources,volume}]\n                     [--key {back,down,exit,left,menu,power,right,up}] [--no-ssl] [-v]\n                     hostname\n\n    Hisense TV control.\n\n    positional arguments:\n      hostname              Hostname or IP for the TV.\n\n    optional arguments:\n      -h, --help            show this help message and exit\n      --authorize           Authorize this API to access the TV.\n      --get {sources,volume}\n                            Gets a value from the TV.\n      --key {back,down,exit,left,menu,power,right,up}\n                            Sends a keypress to the TV.\n      --no-ssl              Do not connect with SSL (required for some models).\n      -v, --verbose         Logging verbosity.\n\nOne Time Setup\n==============\n**Note:** This is not required for all models!\n\n::\n\n    hisensetv 10.0.0.128 --authorize   \n    Please enter the 4-digit code: 7815\n\nKeypresses\n==========\n::\n\n    hisensetv 10.0.0.28 --key up\n    [2020-02-29 13:48:52,064] [INFO    ] sending keypress: up\n\nGets\n====\n::\n\n    hisensetv 10.0.0.28 --get volume\n    [2020-02-29 13:49:00,800] [INFO    ] volume: {\n        "volume_type": 0,\n        "volume_value": 1\n    }\n\n\nNo SSL\n======\nSome models do not have self-signed certificates and will fail to connect\nwithout ``--no-ssl``.\n\nPlease open an issue if yours is not listed here!\n\n    * H43A6250UK\n\nLimitations\n***********\n\nConcurrency\n===========\n* Multiple instances of this class will conflict with one-another.\n* Not thread-safe.\n* This API really *should* be asyncio in 2020, but asyncio is not yet part of the paho mqtt library (see `455`_).\n\nReliability\n===========\n* The concurrency issues contribute to reliability issues in general.\n* Unit tests do not exist yet.\n\nSecurity\n========\n* The self-signed certificates from the TV are completely bypassed.\n\n.. |Black| image:: https://img.shields.io/badge/code%20style-black-000000.svg\n    :target: https://github.com/psf/black\n.. |Build Status| image:: https://github.com/newAM/hisensetv/workflows/CI/badge.svg\n   :target: https://github.com/newAM/hisensetv/actions\n.. |PyPi Version| image:: https://img.shields.io/pypi/v/hisensetv\n    :target: https://pypi.org/project/hisensetv/\n.. |docs| image:: https://readthedocs.org/projects/hisensetv/badge/?version=latest\n   :target: https://hisensetv.readthedocs.io/en/latest/?badge=latest\n.. _mqtt-hisensetv: https://github.com/Krazy998/mqtt-hisensetv\n.. _455: https://github.com/eclipse/paho.mqtt.python/issues/455\n',
    'author': 'Alex Martens',
    'author_email': 'alex@thinglab.org',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/newAM/hisensetv',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
