# slack-archiver-cli: A CLI tool to archive many slack channels at once

![PyPi ver](https://img.shields.io/pypi/v/slack-archiver-cli?style=flat-square)
[![pytest](https://github.com/joe-yama/slack-archiver-cli/actions/workflows/pytest.yml/badge.svg?branch=main)](https://github.com/joe-yama/slack-archiver-cli/actions/workflows/pytest.yml?branch=main)
[![pysen](https://github.com/joe-yama/slack-archiver-cli/actions/workflows/pysen_lint.yml/badge.svg)](https://github.com/joe-yama/slack-archiver-cli/actions/workflows/pysen_lint.yml)
![LICENSE budge](https://img.shields.io/github/license/joe-yama/slack-archiver-cli?style=flat-square)

## Basic Usage

![UsageGIF](https://user-images.githubusercontent.com/17776221/158164007-3fba787e-208a-4686-b06f-17b47ff3bb73.gif)

### Installation

```bash
$ pip install slack-archiver-cli
```

### Set token

```bash
$ export SLACK_BOT_TOKEN = "xoxb-your-slack-bot-token"
```

### List channels with prefix

```bash
$ list-channels channel-prefix
channel-prefix-mychannel1
channel-prefix-mychannel2
```

### Archive channels with prefix

```bash
$ archive-channels slackarchiver
slackarchiver-test1
slackarchiver-test2
2 channels found (prefix: slackarchiver)
Do you want to archive 2 channels? [Y/n] yes
Archived channel: slackarchiver-test1
Archived channel: slackarchiver-test2
```

## Requirements

### Version and Dependencies

- Python >= 3.7
- Dependencies:
  - python-dotenv
  - fire
  - slack-sdk

### Slack Bot Token OAuth & Permission Scopes

- `channels:join`
- `channels:manage`
- `groups:write`
- `im:write`
- `mpim:write`

## License

This software is released under the MIT License, see LICENSE.
