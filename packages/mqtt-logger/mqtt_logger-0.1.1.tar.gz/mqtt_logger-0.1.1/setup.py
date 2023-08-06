# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['mqtt_logger']

package_data = \
{'': ['*']}

install_requires = \
['paho-mqtt>=1.6.1,<2.0.0']

setup_kwargs = {
    'name': 'mqtt-logger',
    'version': '0.1.1',
    'description': 'Python based MQTT to SQLite3 logger',
    'long_description': '# MQTT to SQLite Logger\n\n## Installation\n\n```bash\npip install mqtt-logger\n```\n\n## Examples\n\n```python\nhello = 3\n\n```\n\n## Unit Tests\n\n```bash\n# Run tests in poetry virtual environment\npoetry run pytest\n```',
    'author': 'Blake Haydon',
    'author_email': 'blake.a.haydon@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/Blake-Haydon/mqtt-logger',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
