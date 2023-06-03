# -*- coding: utf-8 -*-
import asyncio
import logging
import os
import sys
import traceback

import websockets as ws
from dotenv import dotenv_values

sys.path.append(os.environ.get("PROJECT_ROOT_DIR"))
from discord.rest.client import Application, Channel, Guild, Stage, User, Webhook
from discord.rest.ws_client import WSClient

logging.basicConfig(
    # filename='example.log', filemode='w',
    level=logging.INFO,  # or logging.DEBUG
    format="%(asctime)s, line: %(lineno)d \t| %(message)s",
)


def main() -> None:
    config = dotenv_values(".pythonenv")
    token = config["TOKEN"]
    channel_id = config["DEFAULT_CHANNEL_ID"]
    guild_id = config["DEFAULT_GUILD_ID"]

    # no channel specified
    channel = Channel(token=token)

    print(
        channel.create_message(
            channel_id=channel_id,
            content="Hello World!",
            embeds=[
                {
                    "title": "Look at these",
                    "description": "What a nice shot",
                    "thumbnail": {"url": "attachment://test.png"},
                }
            ],
            attachments=[
                {
                    "id": 0,
                    "description": "Image of a cute little cat",
                    "filename": "test.png",
                }
            ],
            files=["test.png"],
        )
    )

    user = User(token=token)
    print(user.get_current_user())

    channel = Channel(token)
    channel.create_message(channel_id=channel_id, content="Hello")

    guild = Guild(token=token)
    print(guild.get_guild(guild_id=guild_id))

    stage = Stage(token=token)
    print(stage.get_stage_instance(channel_id=channel_id))

    app = Application(token=token)
    app.get_application_commands(application_id="<some-app-id>")


if __name__ == "__main__":
    main()
