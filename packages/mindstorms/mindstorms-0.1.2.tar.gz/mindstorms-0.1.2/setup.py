# -*- coding: utf-8 -*-
from setuptools import setup

modules = \
['mindstorms']
install_requires = \
['rshell>=0.0.31,<0.0.32']

setup_kwargs = {
    'name': 'mindstorms',
    'version': '0.1.2',
    'description': 'Operate LEGO MINDSTORMS Inventor Hub from your computer',
    'long_description': '# Operate LEGO MINDSTORMS Inventor Hub from your computer\n\nThis module allows you to operate the LEGO mindstorms hub from\nyour computer. This means that instead of sending entire python\nfiles to the hub and letting it run them, you can run the command\none after another from your computer. This allows easy experimenting\nfrom a python shell on your computer, showing you completions and\nAPI documentation on the way. This also allows you to use the\nregular debugging facilities you\'re used to.\n\nThe API mirrors that of the actual micropython API, so programs that run\non the hub (and don\'t use callbacks) should run on your computer using this\nmodule and vice versa.\n\n\nThe API documentation was copied from the official\n[LEGO MINDSTORMS Inventor Hub documentation](https://lego.github.io/MINDSTORMS-Robot-Inventor-hub-API/).\n\nManaging the actual connection to the hub is using the excellent\n[rshell](https://github.com/dhylands/rshell) project.\n\n## Getting Started\n\nRun:\n\n```commandline\npip install mindstorms\n```\n\nConnect the hub to your computer using the USB cable, and then\nrun this from Python:\n\n```python\nfrom mindstorms import Hub\nhub = Hub()\nwhile True:\n    while hub.motion.gesture() != hub.motion.TAPPED:\n        pass\n    hub.sound.play(\'/extra_files/Hello\')\n```\n\nTap the hub, and hear it say "hello".\n\n## Easier usage of sensors using `spikedev`\n\nYou can use Daniel Walton\'s `spikedev` for easier usage of the sensors,\nlike this:\n\n```shell\npip install git+https://github.com/noamraph/spikedev.git@sensor-support-cpython\n```\n\n```python\n>>> from mindstorms import *\n>>> from spikedev.sensor import *\n>>> hub = Hub()\n>>> color = ColorSensor(hub.port.D)\n>>> color.value()\n[0]\n>>> dist = DistanceSensor(hub.port.E)\n>>> dist.set_mode(DistanceSensorMode.DISTL)\n>>> dist.value()\n[58]\n```\n\nThis currently relies on my pull-request. I hope it will be merged, and\nthen you\'ll be able to use it directly from his repository.\n\n## Notes\n\nThe only missing classes from the official API are `hub.BT_VCP`\nand `hub.USB_VCP`. Adding them shouldn\'t be too difficult, \nI just didn\'t know how to test them.\n\nI added all the methods from the official API, except for those that\ncontains a callback.\n\n## License\n\nMIT license.\n\nCopyright (c) 2022 - Noam Raphael.\n\nBased on the [official API docs](https://lego.github.io/MINDSTORMS-Robot-Inventor-hub-API/license.html):\n\n```\nThe MIT License (MIT)\n\nCopyright (c) 2017-2021 - LEGO System A/S - Aastvej 1, 7190 Billund, DK\n\nPermission is hereby granted, free of charge, to any person obtaining a copy\nof this software and associated documentation files (the “Software”), to deal\nin the Software without restriction, including without limitation the rights\nto use, copy, modify, merge, publish, distribute, sublicense, and/or sell\ncopies of the Software, and to permit persons to whom the Software is\nfurnished to do so, subject to the following conditions:\n\nThe above copyright notice and this permission notice shall be included in all\ncopies or substantial portions of the Software.\n\nTHE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR\nIMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,\nFITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE\nAUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER\nLIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,\nOUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE\nSOFTWARE.\n```',
    'author': 'Noam Raphael',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/noamraph/mindstorms',
    'py_modules': modules,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
