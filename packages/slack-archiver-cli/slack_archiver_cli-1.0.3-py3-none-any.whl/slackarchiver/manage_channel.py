import sys
from dataclasses import dataclass
from typing import List

from slack_sdk import WebClient
from slack_sdk.errors import SlackClientError
from slack_sdk.web import SlackResponse
from slackarchiver.settings import SLACK_BOT_TOKEN
from slackarchiver.utils import confirm_user_input

client: WebClient = WebClient(token=SLACK_BOT_TOKEN)


@dataclass
class Channel:
    id: str
    name: str

    def __str__(self) -> str:
        return self.name


class SlackResponseError(SlackClientError):
    pass


def list_channels(
    channel_prefix: str = "",
    exclude_archived: bool = True,
    include_private_channels: bool = False,
) -> List[Channel]:
    next_cursor: str = ""  # for pagenation
    hit_channels: List[Channel] = []
    while True:
        response: SlackResponse = client.conversations_list(
            exclude_archived=exclude_archived,
            types="public_channel,private_channel"
            if include_private_channels
            else "public_channel",
            limit=200,
            cursor=next_cursor,
        )
        if not response["ok"] or not response:
            raise SlackResponseError(
                f"Response of conversations_list api finished in fail. response: {response}",
            )
        for channel in response["channels"]:
            if (channel_name := channel["name_normalized"]).startswith(channel_prefix):
                hit_channels.append(Channel(channel["id"], channel_name))
        next_cursor = response["response_metadata"]["next_cursor"]
        if not next_cursor:
            break
    return hit_channels


def archive_channels(
    channel_prefix: str, include_private_channels: bool = False
) -> None:
    target_channels: List[Channel] = list_channels(
        channel_prefix=channel_prefix, include_private_channels=include_private_channels
    )
    for channel in target_channels:
        sys.stdout.write(str(channel) + "\n")
    sys.stdout.write(
        f"{len(target_channels):,d} channels found (prefix: {channel_prefix})" + "\n"
    )
    if not target_channels:
        # hit no channels
        return

    if confirm_user_input(
        f"Do you want to archive {len(target_channels):,d} channels?"
    ):
        for channel in target_channels:
            client.conversations_join(channel=channel.id)
            response_for_archive: SlackResponse = client.conversations_archive(
                channel=channel.id
            )
            if response_for_archive["ok"]:
                sys.stdout.write(f"Archived channel: {channel}" + "\n")
    else:
        sys.stdout.write(
            f"Don't worry! {len(target_channels):,d} channels were left unchanged."
            + "\n"
        )
    return
