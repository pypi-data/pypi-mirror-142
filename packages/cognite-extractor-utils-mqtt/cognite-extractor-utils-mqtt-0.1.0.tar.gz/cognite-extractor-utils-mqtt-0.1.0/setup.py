# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': '.'}

packages = \
['mqtt']

package_data = \
{'': ['*']}

install_requires = \
['cognite-extractor-utils>=2.1.3,<3.0.0', 'paho-mqtt>=1.6.1,<2.0.0']

setup_kwargs = {
    'name': 'cognite-extractor-utils-mqtt',
    'version': '0.1.0',
    'description': 'MQTT extension for the Cognite extractor-utils framework',
    'long_description': '# Cognite `extractor-utils` MQTT extension\n\nThe MQTT extension for [Cognite `extractor-utils`](https://github.com/cognitedata/python-extractor-utils) provides a way\nto easily write your own extractors for systems exposing an MQTT interface.\n\nThe library is currently under development, and should not be used in production environments yet.\n\n\n## Overview\n\nThe MQTT extension for extractor utils subscribes to MQTT topics, automatically serializes the payload into user-defined\nDTO classes, and handles uploading of data to CDF.\n\nThe only part of the extractor necessary to for a user to implement are\n\n * Describing the payload schema using Python `dataclass`es\n * Implementing a mapping from the source data model to the CDF data model\n\nAs an example, consider this example payload:\n\n``` json\n{\n    "elements": [\n        {\n            "pumpId": "bridge-pump-1453",\n            "startTime": "2022-02-27T12:13:00",\n            "duration": 16,\n        },\n        {\n            "pumpId": "bridge-pump-254",\n            "startTime": "2022-02-26T16:12:23",\n            "duration": 124,\n        },\n    ]\n}\n```\n\nWe want to make an extractor that can turn these MQTT messages into CDF events. First, we need to create some data\nclasses describing the expected schema of the payloads:\n\n```python\n@dataclass\nclass PumpEvent:\n    pumpId: str\n    startTime: str\n    duration: int\n\n@dataclass\nclass PumpEventList:\n    elements: List[PumpEvent]\n```\n\nThen, we can create an `MqttExtractor` instance, subscribe to the appropriate topic, and convert the payload into CDF\nevents:\n\n```python\nextractor = MqttExtractor(\n    name="PumpMqttExtractor",\n    description="Extracting pumping events from an MQTT source",\n    version="1.0.0",\n)\n\n@extractor.topic(topic="mytopic", qos=1, response_type=PumpEventList)\ndef subscribe_pump_events(events: PumpEventList) -> Iterable[Event]:\n    external_id_prefix = MqttExtractor.get_current_config_file()\n\n    for pump_event in events.elements:\n        start_time = arrow.get(pump_event.startTime)\n        end_time = start_time.shift(seconds=pump_event.duration)\n\n        yield Event(\n            external_id=f"{external_id_prefix}{pump_event.pumpId}-{uuid.uuid4()}",\n            start_time=start_time.int_timestamp*1000,\n            end_time=end_time.int_timestamp*1000,\n        )\n\nwith extractor:\n    extractor.run()\n```\n\nA demo example is provided in the [`example.py`](./example.py) file.\n\n\n## Contributing\n\nSee the [contribution guide for `extractor-utils`](https://github.com/cognitedata/python-extractor-utils#contributing)\nfor details on contributing.\n\n',
    'author': 'Einar Omang',
    'author_email': 'einar.omang@cognite.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/cognitedata/python-extractor-utils-mqtt',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<3.11',
}


setup(**setup_kwargs)
