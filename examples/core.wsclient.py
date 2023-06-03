# -*- coding: utf-8 -*-
import asyncio

from dotenv import dotenv_values

from discord.rest.WSClient import WSClient


class CustomClient(WSClient):
    async def on_event(self, event) -> None:
        # print(event)
        if not event or "op" not in event:
            return

        if event["op"] == 0:  # Dispatch
            try:
                print(
                    f'Channel: {data["d"]["channel_id"]} | {data["d"]["author"]["username"]}: {data["d"]["content"]}'
                )
            except:
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
    config = dotenv_values(".pythonenv")
    token = config["TOKEN"]
    channel_id = config["DEFAULT_CHANNEL_ID"]
    guild_id = config["DEFAULT_GUILD_ID"]

    myclient = CustomClient(
        token=token,
        intents=WSClient.get_intents_list(),
    )

    print(await myclient.get_current_user())
    print(await myclient.get_channel(channel_id=channel_id))
    print(await myclient.create_message(channel_id=channel_id, content="Hello!"))

    print(myclient.list_roles())
    myclient.run()

    while True:
        await asyncio.sleep(30)


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
