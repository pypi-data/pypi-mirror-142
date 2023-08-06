# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['py_epg', 'py_epg.common', 'py_epg.scrapers']

package_data = \
{'': ['*']}

install_requires = \
['PyYAML>=6.0,<7.0',
 'beautifulsoup4>=4.10.0,<5.0.0',
 'fake-useragent>=0.1.11,<0.2.0',
 'lxml>=4.6.3,<5.0.0',
 'py-xmltv>=1.0.8,<2.0.0',
 'python-dateutil>=2.8.2,<3.0.0',
 'python-xmltv>=1.4.3,<2.0.0',
 'requests>=2.26.0,<3.0.0',
 'roman>=3.3,<4.0',
 'tqdm>=4.62.3,<5.0.0']

entry_points = \
{'console_scripts': ['epg = py_epg.main:main']}

setup_kwargs = {
    'name': 'py-epg',
    'version': '0.2.9',
    'description': 'py_epg is an easy to use, modular, multi-process EPG grabber written in Python.',
    'long_description': '# py-epg\n\n**py-epg** is an easy to use, modular, multi-process EPG grabber written in Python.\n\n* 📺 Scrapes various TV Program websites and saves programs in XMLTV format.\n* 🧩 Simply extend [EpgScraper](https://github.com/szab100/py_epg/blob/main/py_epg/common/epg_scraper.py) to grab EPG from your favorite TV site (requires basic Python skills).\n* 🤖 The framework provides the rest:\n    * [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc) - easily search & extract data from html elements \n    * multi-processing\n    * config management\n    * logging\n    * build & write XMLTV (with auto-generated fields, eg \'stop\')\n    * proxy server support\n    * auto http/s retries\n    * random fake user_agents\n* 🚀 Save time by fetching channels in parallel (caution: use proxy server(s) to avoid getting blacklisted)!\n* 🧑🏻\u200d💻 Your contributions are welcome! Feel free to create a PR with your tv-site scraper and/or framework improvements.\n\n<p align="center">\n  <img src="https://raw.githubusercontent.com/szab100/py_epg/main/py_epg.gif">\n</p>\n\n## Usage\n\n1. Install package:\n    ```sh\n    $ pip3 install py_epg\n    ```\n2. Create configuration: py_epg.xml\n    - Add all your channels (see [sample config](https://github.com/szab100/py-epg/blob/main/py_epg.xml)).\n    - Make sure there is a corresponding site scraper implementation in [py_epg/scrapers](https://github.com/szab100/py-epg/tree/main/py_epg/scrapers) for each channels (\'site\' attribute).\n3. Run:\n    ```sh\n    $ python3 -m py_epg -c </path/to/your/py_epg.xml> -p\n    ```\n\n    ..or see all supported flags:\n    ```sh\n    $ python3 -m py_epg -h\n    usage: py_epg [-h] [-p [PROGRESS_BAR]] [-q [QUIET]] -c CONFIG\n    ...\n    ```\n\n## Development\n\nYour contributions are welcome! Setup your dev environment as described below. [VSCode](https://code.visualstudio.com/) is a great free IDE for python projects. Once you are ready with your cool tv site scraper or framework feature, feel free to open a Pull Request here.\n\n1. Install poetry: \n    ```sh\n    curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -\n    ```\n\n2. Clone repository & install dependencies:\n      ```sh\n      git clone https://github.com/szab100/py-epg.git && cd py-epg\n      ```\n\n3. Configure py_epg.xml\n    - Add all your channels (see the sample config xml). Make sure you have a scraper implementation in py_epg/scrapers/ for each channels (\'site\' attribute).\n\n4. Run:\n      ```sh\n      poetry install\n      poetry run epg -c py_epg.xml\n      ```\n\n## License\n\nCopyright 2021. Released under the MIT license.\n',
    'author': 'Szabolcs Fruhwald',
    'author_email': 'mail@szab100.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/szab100/py-epg',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
