# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['actfw_raspberrypi', 'actfw_raspberrypi.vc4']

package_data = \
{'': ['*']}

install_requires = \
['actfw-core>=2.0.0,<3.0.0']

setup_kwargs = {
    'name': 'actfw-raspberrypi',
    'version': '2.1.0a0',
    'description': "actfw's additional components for RaspberryPi",
    'long_description': '# actfw-raspberrypi\n\nactfw\'s components for Raspberry Pi.\nactfw is a framework for Actcast Application written in Python.\n\n## Installation\n\n```console\nsudo apt-get update\nsudo apt-get install -y python3-pip python3-pil \npip3 install actfw-raspberrypi\n```\n\n## Document\n\n* [API References](https://idein.github.io/actfw-raspberrypi/latest/)\n\n## Usage\n\nSee [actfw-core](https://github.com/Idein/actfw-core) for basic usage.\n\nactfw-raspberrypi provides:\n\n* `actfw_raspberrypi.capture.PiCameraCapture` : Generate CSI camera capture image\n* `actfw_raspberrypi.Display` : Display using PiCamera Overlay\n* `actfw_raspberrypi.vc4.Display` : Display using VideoCore IV\n* `actfw_raspberrypi.vc4.Window` : Double buffered window\n\n## Example\n\n* `example/hello` : The most simple application example\n  * Use HDMI display as 640x480 area\n  * Capture 320x240 RGB image from CSI camera\n  * Draw "Hello, Actcast!" text\n  * Display it as 640x480 image (with x2 scaling)\n  * Notice message for each frame\n  * Support application setting\n  * Support application heartbeat\n  * Support "Take Photo" command\n  * Depends: python3-picamera fonts-dejavu-core\n* `example/grayscale` : Next level application example\n  * Use HDMI display as 640x480 area\n  * Capture 320x240 RGB image from CSI camera\n  * Convert it to grayscale\n  * Display it as 640x480 image (with x2 scaling)\n  * Notice message for each frame\n  * Support application setting\n  * Support application heartbeat\n  * Support "Take Photo" command\n  * Depends: python3-picamera\n* `example/parallel_grayscale` : Paralell processing application example\n  * Use HDMI display as 640x480 area\n  * Capture 320x240 RGB image from CSI camera\n  * Convert it to grayscale\n    * There exists 2 converter task\n    * Round-robin task scheduling\n  * Display it as 640x480 image (with x2 scaling)\n  * Notice message for each frame\n    * Show which converter processes image\n  * Support application setting\n  * Support application heartbeat\n  * Support "Take Photo" command\n  * Depends: python3-picamera\n* `example/uvccamera` : UVC camera capture example\n  * `picamera` is unnecessary\n  * Use HDMI display center 640x480 area\n  * Capture 320x240 RGB image from UVC camera\n  * Convert it to grayscale\n  * Display it as 640x480 image (with x2 scaling)\n  * Notice grayscale pixel data histogram\n  * Support application setting\n  * Support application heartbeat\n  * Support "Take Photo" command\n  * Depends: libv4l-0 libv4lconvert0\n\n## Development Guide\n\n### Installation of dev requirements\n\n```console\npip3 install poetry\npoetry install\n```\n\n### Running tests\n\n```console\npoetry run nose2 -v\n```\n\n### Running examples\n\nOn a Raspberry Pi connected to HDMI display:\n\n```console\npoetry run python example/hello\n```\n\n### Releasing package & API doc\n\nCI will automatically do.\nFollow the following branch/tag rules.\n\n1. Make changes for next version in `master` branch (via pull-requests).\n2. Make a PR that updates version in `pyproject.toml` and merge it to `master` branch.\n3. Create Git tag from `master` branch\'s HEAD named `release-<New version>`. E.g. `release-1.4.0`.\n4. Then CI will build/upload package to PyPI & API doc to GitHub Pages.\n',
    'author': 'Idein Inc.',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/Idein/actfw-raspberrypi',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6.2,<4.0.0',
}


setup(**setup_kwargs)
