# Discord-Websocket-Client

Simple Websocket Client for Discord

This project is still in progress.

## Example Usage

```python
import asyncio
from pydisco_client.ws_client import ReconnectingWebsocket

token = "your-discord-token"
async def main():
    async def handle_event(data: dict):
        print(data)
        if not data or "op" not in data:
            return

        if data["op"] == 0:  # Dispatch
            try:
                print(f"{data['d']['channel_id']}: ...print some messages?")
            except:
                # handle...
                pass

        elif data["op"] == 3:  # Presence Update
            print(f"This is OP 3 - {data}")
        elif data["op"] == 4:  # Voice State Update
            print(f"This is OP 4 - {data}")
        elif data["op"] == 6:  # Resume
            print(f"This is OP 6 - {data}")
        elif data["op"] == 7:  # Reconnect
            print(f"This is OP 7 - {data}")
        elif data["op"] == 8:  # Request Guild Members
            print(f"This is OP 8 - {data}")
        elif data["op"] == 9:  # Invalid Session
            print(f"This is OP 9 - {data}")
        elif data["op"] == 10:  # Hello
            print("Hearbeat intervall received!")
        elif data["op"] == 11:  # Heartbeat ACK
            print("Heartbeat Received")
        else:
            print(f"huh? {data}")

    ws_client = ReconnectingWebsocket(
        token=token,
        url="wss://gateway.discord.gg/?v=9&encording=json",
        coro=handle_event
    )

    while True:
        await asyncio.sleep(30)

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
```

# Notes

Discord Documentation: https://discord.com/developers/docs/topics/gateway
