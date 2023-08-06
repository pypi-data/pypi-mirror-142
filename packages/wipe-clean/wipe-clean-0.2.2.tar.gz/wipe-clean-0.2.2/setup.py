# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['wipe_clean', 'wipe_clean._rich']

package_data = \
{'': ['*']}

entry_points = \
{'console_scripts': ['wipe-clean = wipe_clean.main:_outer_cli']}

setup_kwargs = {
    'name': 'wipe-clean',
    'version': '0.2.2',
    'description': 'Clear your terminal in a ritual way. Zero dependency.',
    'long_description': '<div align="center">\n\n# Wipe Clean\n\n<a href="https://github.com/wenoptics/python-wipe-clean">\n  <img src="https://github.com/wenoptics/python-wipe-clean/blob/master/doc/logo.png?raw=true" alt="Logo" width="200" height="200">\n</a>\n\n![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)\n![PyPI - Python Version](https://img.shields.io/pypi/pyversions/wipe-clean?logo=python)\n\n[![PyPI](https://img.shields.io/pypi/v/wipe-clean?logo=pypi)](https://pypi.org/project/wipe-clean/)\n[![PyPI - Wheel](https://img.shields.io/pypi/wheel/wipe-clean)](https://pypi.org/project/wipe-clean/)\n[![PyPI - Status](https://img.shields.io/pypi/status/wipe-clean)](https://pypi.org/project/wipe-clean/)\n\n[![Linux](https://img.shields.io/badge/Linux-FCC624?logo=linux&logoColor=black)](https://github.com/wenoptics/python-wipe-clean)\n[![Mac OS](https://img.shields.io/badge/MacOS--9cf?logo=Apple&style=social)](https://github.com/wenoptics/python-wipe-clean)\n[![Windows](https://img.shields.io/badge/Windows-0078D6?logo=windows&logoColor=white)](https://github.com/wenoptics/python-wipe-clean)\n\n</div>\n\n---\n\n## wipe-clean\n\nClear your terminal in a _ritual_ way. Works on Windows, Linux and macOS. **0-dependency**.\n\n\n![demo](https://github.com/wenoptics/python-wipe-clean/blob/master/doc/terminal.gif?raw=true)\n\nInstall with pip:\n\n```bash\npip install wipe-clean\n```\n\n> `wipe-clean` currently requires Python 3.6.1 and above. Note that Python 3.6.0 is\n not supported due to lack of `NamedTuples` typing.\n\n\n## Usages\n\nJust:\n\n```bash\nwipe-clean\n```\n\nUse `-h, --help` to show all available options\n\n```bash\nwipe-clean -h\n```\n\n## Advanced usages\n\n### 1. Use API\n\n```python\nfrom wipe_clean.main import cli as wc_cli\n\nwc_cli()\n# Or with arguments\nwc_cli(\'--frame-interval=0.005\', \'--min-frame-delay=0\')\n```\n\n### 2. Customization\n\nIt\'s possible to design your own brush shape and animation!\n\n#### Example brush\n\nTo create a new brush type, implement the `Brush` interface, e.g.\n\n```python\nfrom wipe_clean.brush import Brush, ScreenPointDrawing, ScreenPoint as P\n\nclass Wipe2x2(Brush):\n    def get_points(self, x, y, angle) -> List[ScreenPointDrawing]:\n        return [\n            ScreenPointDrawing(P(x    , y    ), \'#\'),\n            ScreenPointDrawing(P(x + 1, y    ), \'#\'),\n            ScreenPointDrawing(P(x    , y + 1), \'#\'),\n            ScreenPointDrawing(P(x + 1, y + 1), \'#\'),\n        ]\n```\n\nThis will define a brush like this:\n\n```text\n##\n##\n```\n\n#### Example path\n\nSimilarly, you can implement the `Path` interface to create a new brush path.\n\n```python\nimport math\nfrom wipe_clean.path import Path, PathPoint, ScreenPoint as P\n\nclass MySimplePath(Path):\n    def get_points(self) -> Iterable[PathPoint]:\n        return [\n            PathPoint(P(10, 10), math.radians(45)),\n            PathPoint(P(20,  5), math.radians( 0)),\n            PathPoint(P(40, 20), math.radians(90)),\n        ]\n```\n\n\n## Roadmap\n\nSee [`DEVELOPMENT.md`](./DEVELOPMENT.md)\n\n\n## Related projects\n\n- [`JeanJouliaCode/wipeclean`](https://github.com/JeanJouliaCode/wipeClean) - JavaScript version\n\n  _The first brush type (`BrushWipe`) and path animations (`PathZigZag`, `PathRectEdge`) are direct ports\n  of `JeanJouliaCode/wipeclean`. Credits go to JeanJouliaCode!_\n\n- [`Textualize/rich`](https://github.com/Textualize/rich) - _An inspiring textual UI library_\n',
    'author': 'wenoptk',
    'author_email': 'wenoptics@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/wenoptics/python-wipe-clean',
    'packages': packages,
    'package_data': package_data,
    'entry_points': entry_points,
    'python_requires': '>=3.6.2,<4.0.0',
}


setup(**setup_kwargs)
