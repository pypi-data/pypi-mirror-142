import fire
from slackarchiver.manage_channel import archive_channels, list_channels


def cli_list_channels() -> int:
    fire.Fire(list_channels)
    return 0


def cli_archive_channels() -> int:
    fire.Fire(archive_channels)
    return 0
