# slack-archiver-cli: A CLI tool to archive many slack channels at once

![PyPi ver](https://img.shields.io/pypi/v/slack-archiver-cli?style=flat-square)
![LICENSE budge](https://img.shields.io/github/license/joe-yama/slack-archiver-cli?style=flat-square)

## Basic Usage

### Listing channels with prefix

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

## Installation

```bash
$ pip install slack-archiver-cli
```

### Requirements

- Python >= 3.7
- Dependencies:
  - python-dotenv
  - fire
  - slack-sdk

## License

This software is released under the MIT License, see LICENSE.
