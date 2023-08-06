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
    'version': '1.1.0',
    'description': 'A CLI tool to archive many slack channels at once',
    'long_description': '# slack-archiver-cli: A CLI tool to archive many slack channels at once\n\n![PyPi ver](https://img.shields.io/pypi/v/slack-archiver-cli?style=flat-square)\n[![pytest](https://github.com/joe-yama/slack-archiver-cli/actions/workflows/pytest.yml/badge.svg?branch=main)](https://github.com/joe-yama/slack-archiver-cli/actions/workflows/pytest.yml?branch=main)\n[![pysen](https://github.com/joe-yama/slack-archiver-cli/actions/workflows/pysen_lint.yml/badge.svg)](https://github.com/joe-yama/slack-archiver-cli/actions/workflows/pysen_lint.yml)\n![LICENSE budge](https://img.shields.io/github/license/joe-yama/slack-archiver-cli?style=flat-square)\n\n## Basic Usage\n\n![UsageGIF](https://user-images.githubusercontent.com/17776221/158164007-3fba787e-208a-4686-b06f-17b47ff3bb73.gif)\n\n### Installation\n\n```bash\n$ pip install slack-archiver-cli\n```\n\n### Set token\n\n```bash\n$ export SLACK_BOT_TOKEN = "xoxb-your-slack-bot-token"\n```\n\n### List channels with prefix\n\n```bash\n$ list-channels channel-prefix\nchannel-prefix-mychannel1\nchannel-prefix-mychannel2\n```\n\n### Archive channels with prefix\n\n```bash\n$ archive-channels slackarchiver\nslackarchiver-test1\nslackarchiver-test2\n2 channels found (prefix: slackarchiver)\nDo you want to archive 2 channels? [Y/n] yes\nArchived channel: slackarchiver-test1\nArchived channel: slackarchiver-test2\n```\n\n## Requirements\n\n### Version and Dependencies\n\n- Python >= 3.7\n- Dependencies:\n  - python-dotenv\n  - fire\n  - slack-sdk\n\n### Slack Bot Token OAuth & Permission Scopes\n\n- `channels:join`\n- `channels:manage`\n- `groups:write`\n- `im:write`\n- `mpim:write`\n\n## License\n\nThis software is released under the MIT License, see LICENSE.\n',
    'author': 'joe-yama',
    'author_email': 's1r0mqme@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/joe-yama/slack-archiver-cli',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4',
}


setup(**setup_kwargs)
