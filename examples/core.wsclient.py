# -*- coding: utf-8 -*-
import asyncio
import os
from typing import Any

from discord.WSClient import Channel, User, WSClient


class CustomClient(WSClient):
    async def on_event(self: "CustomClient", event: Any) -> None:
        # print(event)
        if not event or "op" not in event:
            return

        if not isinstance(event, dict):
            return
        if event["op"] == 0:  # Dispatch
            try:
                print(
                    f'Channel: {event["d"]["channel_id"]} | {event["d"]["author"]["username"]}: {event["d"]["content"]}'
                )
            except KeyError:
                # handle...
                pass

        elif event["op"] == 3:  # Presence Update
            print(f"This is OP 3 - {event}")
        elif event["op"] == 4:  # Voice State Update
            print(f"This is OP 4 - {event}")
        elif event["op"] == 6:  # Resume
            print(f"This is OP 6 - {event}")
        elif event["op"] == 7:  # Reconnect
            print(f"This is OP 7 - {event}")
        elif event["op"] == 8:  # Request Guild Members
            print(f"This is OP 8 - {event}")
        elif event["op"] == 9:  # Invalid Session
            print(f"This is OP 9 - Invalid Session! {event}")
        elif event["op"] == 10:  # Hello
            print("Hearbeat interval received!")
        elif event["op"] == 11:  # Heartbeat ACK
            print("Heartbeat Received")
        else:
            print(f"huh? {event}")


async def main() -> None:
    token: str = os.getenv("TOKEN")
    channel_id: str = os.getenv("DEFAULT_CHANNEL_ID")

    myclient: CustomClient = CustomClient(
        token=token,
        intents=WSClient.get_intents_list(),
    )
    user: User = User(token=token)
    print(user.get_current_user())

    channel: Channel = Channel(token=token)
    print(channel.get_channel(channel_id=channel_id))
    print(channel.create_message(channel_id=channel_id, content="Hello!"))

    print(myclient.list_roles())
    myclient.run()

    while True:
        await asyncio.sleep(30)


if __name__ == "__main__":
    asyncio.run(main())
