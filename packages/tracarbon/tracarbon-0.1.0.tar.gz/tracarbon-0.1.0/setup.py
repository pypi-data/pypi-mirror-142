# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['tracarbon',
 'tracarbon.cli',
 'tracarbon.emissions',
 'tracarbon.exporters',
 'tracarbon.hardwares',
 'tracarbon.locations',
 'tracarbon.locations.data']

package_data = \
{'': ['*']}

install_requires = \
['aiocache>=0.11.1,<0.12.0',
 'aiohttp>=3.8.1,<4.0.0',
 'loguru>=0.6.0,<0.7.0',
 'msgpack>=1.0.3,<2.0.0',
 'psutil>=5.9.0,<6.0.0',
 'pydantic>=1.9.0,<2.0.0',
 'typer>=0.4.0,<0.5.0',
 'ujson>=5.1.0,<6.0.0']

extras_require = \
{'datadog': ['datadog>=0.44.0,<0.45.0']}

entry_points = \
{'console_scripts': ['tracarbon = tracarbon.cli:main']}

setup_kwargs = {
    'name': 'tracarbon',
    'version': '0.1.0',
    'description': "Tracarbon tracks your device's power consumption and calculates your carbon emissions.",
    'long_description': '![Alt text](logo.png?raw=true "Tracarbon logo")\n\n[![doc](https://img.shields.io/badge/docs-python-blue.svg?style=flat-square)](https://fvaleye.github.io/tracarbon)\n[![pypi](https://img.shields.io/pypi/v/tracarbon.svg?style=flat-square)](https://pypi.org/project/tracarbon/)\n![example workflow](https://github.com/fvaleye/tracarbon/actions/workflows/build.yml/badge.svg)\n\n\n## 📌 Overview\nTracarbon is a Python library that tracks your device\'s power consumption and calculates your carbon emissions.\n\n## 📦 Where to get it\n\n```sh\n# Install Tracarbon\npip install \'tracarbon\'\n```\n\n```sh\n# Install one or more exporters from the list\npip install \'tracarbon[datadog]\'\n```\n\n### 🔌 Devices: energy consumption\n\n| **Device**  |                **Description**                |\n|-------------|:---------------------------------------------:|\n| **Mac**     | Battery energy consumption (must be plugged). |\n| **Linux**   |             Not yet implemented.              |\n| **Windows** |             Not yet implemented.              |\n\n## 📡 Exporters\n\n| **Exporter** |                **Description**                |\n|--------------|:-----------------------------------------:|\n| **Stdout**   |       Print the metrics in Stdout.        |\n| **Datadog**  |      Publish the metrics on Datadog.      |\n\n### 🗺️ Locations\n\n\n| **Location**                    |                  **Description**                   | **Source**                                                                                                                                                   |\n|-------------------------------|:--------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------------------------------------------|\n| **European Environment Agency** | European Emission co2g/kwh for European countries. | [EEA website](https://www.eea.europa.eu/data-and-maps/daviz/co2-emission-intensity-9#tab-googlechartid_googlechartid_googlechartid_googlechartid_chart_11111)|\n| **France**                      |      RTE energy consumption API in real-time.      | [RTE API](https://opendata.reseaux-energies.fr)                                                                                                              |\n\n\n## 🔎 Usage\n\n**API**\n```python\nimport asyncio\n\nfrom tracarbon import CarbonEmission, EnergyConsumption, Country\nfrom tracarbon.exporters import Metric, StdoutExporter\nfrom tracarbon.hardwares import HardwareInfo\n\nexporter = StdoutExporter()\nmetrics = list()\nlocation = asyncio.run(Country.get_location())\nenergy_consumption = EnergyConsumption.from_platform()\nplatform = HardwareInfo.get_platform()\nmetrics.append(\n    Metric(\n        name="energy_consumption",\n        value=energy_consumption.run,\n        tags=[f"platform:{platform}", f"location:{location}"]\n    )\n)\nmetrics.append(\n    Metric(\n        name="co2_emission",\n        value=CarbonEmission(energy_consumption=energy_consumption, location=location).run,\n        tags=[f"platform:{platform}", f"location:{location}"]\n    )\n)\nmetrics.append(\n    Metric(\n        name="hardware_cpu_usage",\n        value=HardwareInfo().get_cpu_usage,\n        tags=[f"platform:{platform}", f"location:{location}"]\n    )\n)\nmetrics.append(\n    Metric(\n        name="hardware_memory_usage",\n        value=HardwareInfo().get_memory_usage,\n        tags=[f"platform:{platform}", f"location:{location}"]\n    )\n)\nasyncio.run(exporter.launch_all(metrics=metrics))\n```\n\n**CLI**\n```sh\ntracarbon run Stdout\n```\n\n## 🛡️ Licence\nhttps://raw.githubusercontent.com/fvaleye/tracarbon/main/LICENSE.txt[Apache License 2.0]\n\n## 📚 Documentation\nThe documentation is hosted here: https://fvaleye.github.io/tracarbon/documentation\n',
    'author': 'Florian Valeye',
    'author_email': 'fvaleye@github.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
