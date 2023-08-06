import fire
from slackarchiver.manage_channel import archive_channels, list_channels


def cli_list_channels() -> None:
    fire.Fire(list_channels)


def cli_archive_channels() -> None:
    fire.Fire(archive_channels)
