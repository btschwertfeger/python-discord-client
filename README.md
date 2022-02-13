# Welcome to python-discord-client

[![Generic badge](https://img.shields.io/badge/license-MIT-green.svg)](https://shields.io/)
[![Generic badge](https://img.shields.io/badge/python-3.7+-blue.svg)](https://shields.io/)

# Features

- Connect to your discord Account
- Simple handling of authentication
- Implement websockets (note only python3.7+)

# Quick Start

- Register at [Discord](https://discord.com/).
- Login and copy your auth token.

```bash
python3 -m pip install python-discord-client
```

## Rest Client

- not implemented yet

## Websockets

```python
import asyncio
from python_discord_client.ws_client import ReconnectingWebsocket

token = "your-discord-token"
async def main():
    async def handle_event(data: dict):
        #print(data)
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
            print("Hearbeat interval received!")
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

# Todo

- Rest Client
