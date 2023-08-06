# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['hub_scraper',
 'hub_scraper.console',
 'hub_scraper.filters',
 'hub_scraper.indexers',
 'hub_scraper.indexers.indexers',
 'hub_scraper.indexers.indexers.default_obsidian',
 'hub_scraper.models',
 'hub_scraper.scraper']

package_data = \
{'': ['*']}

install_requires = \
['aiofile>=3.7.4,<4.0.0',
 'chompjs>=1.1.6,<2.0.0',
 'click>=8.0.4,<9.0.0',
 'httpx>=0.22.0,<0.23.0',
 'loguru>=0.6.0,<0.7.0',
 'lxml>=4.8.0,<5.0.0',
 'markdownify>=0.10.3,<0.11.0',
 'pydantic>=1.9.0,<2.0.0']

entry_points = \
{'console_scripts': ['hub-scraper = hub_scraper.console.application:main']}

setup_kwargs = {
    'name': 'hub-scraper',
    'version': '0.6.1',
    'description': 'Tool to grab articles from the habr.com hubs.',
    'long_description': "# Hub scraper\n\nTool to grab articles from the habr.com hubs.\n\n## Requirements\n- Python 3.8+\n\n## Installation\n```bash\npip install hub-scraper\n```\n\n\n## Usage\n```bash\nhub-scraper --help\n\nhub-scraper -h python -of /home/user/Downloads/hubs\n```\n\nI'm using [Obsidian](https://obsidian.md/) to view the articles:\n![](https://github.com/dmitriiweb/hub-scraper/raw/main/images/default-obsidian.png)",
    'author': 'Dmitrii Kurlov',
    'author_email': 'dmitriik@protonmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/dmitriiweb/hub-scraper',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<3.11',
}


setup(**setup_kwargs)
