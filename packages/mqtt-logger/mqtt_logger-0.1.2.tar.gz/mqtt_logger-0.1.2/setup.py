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
    'version': '0.1.2',
    'description': 'Python based MQTT to SQLite3 logger',
    'long_description': '# MQTT to SQLite Logger\n\n## Installation\n\n```bash\npip install mqtt-logger\n```\n\n## Example Usage\n\n### Recording MQTT Messages\n\nThis example records messages to the `test/#` topic using a public MQTT broker. It will record for 10 seconds. If you are using a private broker, you may need to set the `username` and `password` parameters.\n\n```python\nimport mqtt_logger\nimport os\nimport time\n\n# Initalise mqtt recorder object\nrec = mqtt_logger.Recorder(\n    sqlite_database_path=os.path.join(os.path.dirname(__file__), "MQTT_log.db"),\n    topics=["test/#"],\n    broker_address="broker.hivemq.com",\n    verbose=True,\n    # username="username",\n    # password="password",\n)\n\n# Start the logger, wait 10 seconds and stop the logger\nrec.start()\ntime.sleep(10)\nrec.stop()\n```\n\n### Playback Recorded MQTT Messages\n\nThis example plays back previously recorded MQTT messages from `mqtt_logger.Recorder`. If you are using a private broker, you may need to set the `username` and `password` parameters.\n\n```python\nimport mqtt_logger\nimport os\n\n# Initalise playback object\nplayback = mqtt_logger.Playback(\n    sqlite_database_path=os.path.join(os.path.dirname(__file__), "MQTT_log.db"),\n    broker_address="broker.hivemq.com",\n    verbose=True,\n    # username="username",\n    # password="password",\n)\n\n# Start playback at 2x speed (twice as fast)\nplayback.play(speed=2)\n```\n\n## Unit Tests\n\n```bash\n# Run tests in poetry virtual environment\npoetry run pytest\n```',
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
