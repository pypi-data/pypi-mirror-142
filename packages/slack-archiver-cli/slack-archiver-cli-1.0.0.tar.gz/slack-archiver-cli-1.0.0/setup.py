# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['slackarchiver']

package_data = \
{'': ['*']}

install_requires = \
['fire>=0.4.0,<0.5.0',
 'python-dotenv>=0.19.2,<0.20.0',
 'slack-sdk>=3.15.2,<4.0.0']

entry_points = \
{'console_scripts': ['archive-channels = '
                     'slackarchiver.cli:cli_archive_channels',
                     'list-channels = slackarchiver.cli:cli_list_channels']}

setup_kwargs = {
    'name': 'slack-archiver-cli',
    'version': '1.0.0',
    'description': '',
    'long_description': '# slack-archiver-cli: A CLI tool to archive many slack channels at once\n\n![PyPi ver](https://img.shields.io/pypi/v/slack-archiver-cli?style=flat-square)\n![LICENSE budge](https://img.shields.io/github/license/joe-yama/slack-archiver-cli?style=flat-square)\n\n## Basic Usage\n\n### Listing channels with prefix\n\n```bash\n$ list-channels channel-prefix\nchannel-prefix-mychannel1\nchannel-prefix-mychannel2\n```\n\n### Archive channels with prefix\n\n```bash\n$ archive-channels slackarchiver\nslackarchiver-test1\nslackarchiver-test2\n2 channels found (prefix: slackarchiver)\nDo you want to archive 2 channels? [Y/n] yes\nArchived channel: slackarchiver-test1\nArchived channel: slackarchiver-test2\n```\n\n## Installation\n\n```bash\n$ pip install slack-archiver-cli\n```\n\n### Requirements\n\n- Python >= 3.7\n- Dependencies:\n  - python-dotenv\n  - fire\n  - slack-sdk\n\n## License\n\nThis software is released under the MIT License, see LICENSE.\n',
    'author': 'joe-yama',
    'author_email': 's1r0mqme@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/joe-yama/slack-archiver-cli',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4',
}


setup(**setup_kwargs)
