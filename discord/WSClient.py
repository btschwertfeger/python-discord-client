import asyncio
import websockets as ws
import sys, traceback
import json
import time
import logging
from typing import Any, Optional, List

from discord.base_request import BaseRequestAPI
from discord.utils import Permissions, Intents


class WSClient(BaseRequestAPI, Permissions, Intents):
    """
    Connect to the Discord websocket-feed.

    @param: token (str): required
    @param: url (str):  required
    """

    HEARTBEAT_INTERVAL = 41250 / 1000  # in seconds
    LAST_PING = None
    SEQUENCE = None

    URL = "wss://gateway.discord.gg/?v=9&encording=json"

    def __init__(self, token: str, intents: List[str], api_version: str = None) -> None:
        super().__init__(token=token, api_version=api_version)

        self._log: logging.Logger = logging.getLogger(__name__)

        self._token: str = token
        self._intents: int = self._get_intents(intents_list=intents)

        if api_version is not None:
            self.URL = f"wss://gateway.discord.gg/?v={api_version}&encording=json"

    def run(self: "WSClient") -> None:
        self._connect()

    async def _main(self: "WSClient") -> None:
        try:
            keep_waiting = True
            async with ws.connect(self.URL) as socket:
                self.ws = socket
                await self._authenticate()

                try:
                    while keep_waiting:
                        if (
                            not self.LAST_PING
                            or int(time.time()) - self.LAST_PING
                            > self._get_ws_pingtimeout()
                        ):
                            await self._send_ping()
                        try:
                            evt = await asyncio.wait_for(
                                self.ws.recv(), timeout=self._get_ws_pingtimeout()
                            )
                        except asyncio.TimeoutError:
                            self._log.info(
                                f"No message in {self._get_ws_pingtimeout()} seconds"
                            )
                            await self._send_ping()
                        except asyncio.CancelledError:
                            self._log.warn("Cancelled error")
                            await self.ws.ping()
                        else:
                            try:
                                evt_obj = json.loads(evt)
                                if (
                                    evt_obj["op"] != 11
                                    and "s" in evt_obj
                                    and evt_obj["s"]
                                ):  # setting the _sequence
                                    self.SEQUENCE = evt_obj["s"]
                                    if evt_obj["op"] == 10:
                                        self.HEARTBEAT_INTERVAL = (
                                            int(evt_obj["d"]["heartbeat_interval"])
                                            / 1000
                                        )
                            except ValueError:
                                pass
                            else:
                                await self.trigger("on_event", evt_obj)

                except ws.ConnectionClosed:
                    keep_waiting = False
                    self._log.warn(
                        f"Websocket connection closed!  {e} {traceback.format_exc()}"
                    )
                    await self._reconnect()
                except Exception as e:
                    self._log.error(f"WS exception: {e} {traceback.format_exc()}")
                    keep_waiting = False
                    await self._reconnect()

        except Exception as e:
            self._log.error(f"Exception!: {e} {traceback.format_exc()}")

    def _connect(self: "WSClient") -> None:
        self._log.info("Connecting...")
        self._conn = asyncio.ensure_future(self._main())

    async def _reconnect(self: "WSClient") -> None:
        self._log.info("Reconnecting Websocket...")
        await self._close_connection()
        self._connect()

    async def _close_connection(self: "WSClient") -> None:
        await self.ws.close()

    async def send_message(self: "WSClient", message: dict) -> None:
        await self.ws.send(json.dumps(message))

    async def _send_ping(self: "WSClient") -> None:
        self._log.info(f"Sending ping now, _sequence: {self.SEQUENCE}")
        await self.send_message({"op": 1, "d": self.SEQUENCE})
        self.LAST_PING = int(time.time())

    async def _authenticate(self: "WSClient") -> None:
        await self.send_message(self._get_payload(kind="init"))

    def _get_ws_pingtimeout(self: "WSClient") -> float:
        return self.HEARTBEAT_INTERVAL

    def _get_payload(self: "WSClient", kind: str) -> dict:
        """https://discord.com/developers/docs/topics/gateway#identifying"""
        op: Optional[int] = None
        if kind == "reconnect":
            op = 7
        elif kind == "resume":
            op = 6
        elif kind == "init":
            op = 2
        else:
            raise ValueError
        return {
            "op": op,
            "d": {
                "token": self._token,
                "intents": f"{self._intents}",
                "properties": {
                    "$os": sys.platform,
                    "$browser": "disco",
                    "$device": "pc",
                },
                "compress": True,
            },
        }

    async def on(self: "WSClient", event_name: str, callback) -> None:
        if event_name not in self._callbacks:
            self._callbacks[event_name] = [callback]
        else:
            self._callbacks[event_name].append(callback)

    async def trigger(self: "WSClient", event_name: str, event_object: Any) -> None:
        if event_name in self._callbacks:
            for callback in self._callbacks[event_name]:
                await callback(event_object)

    async def on_event(self: "WSClient", event: Any) -> None:
        print(event)
