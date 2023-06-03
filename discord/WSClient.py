# -*- coding: utf-8 -*-

"""Module that implements the websocket client"""

import asyncio
import json
import logging
import sys
import time
import traceback
from typing import Any, List, Optional

import websockets as ws

from discord.base_request import BaseRequestAPI
from discord.utils import Intents, Permissions


class WSClient(BaseRequestAPI, Permissions, Intents):
    """
    Connect to the Discord websocket-feed.

    @param: token (str): required
    @param: url (str):  required
    """

    HEARTBEAT_INTERVAL: float = 41250 / 1000  # in seconds
    LAST_PING: Optional[int] = None
    SEQUENCE: str = None
    LOG: logging.Logger = logging.getLogger(__name__)
    URL: str = "wss://gateway.discord.gg/?v=9&encording=json"

    def __init__(
        self,
        token: str,
        intents: List[str],
        api_version: Optional[str] = None,
    ) -> None:
        super().__init__(token=token, api_version=api_version)

        self.__conn: Optional[Any] = None  # pylint: disable=unused-private-member
        self.ws: Optional[Any] = None  # pylint: disable=unused-private-member
        self._token: str = token
        self._intents: int = self._get_intents(intents_list=intents)

        if api_version is not None:
            self.URL = f"wss://gateway.discord.gg/?v={api_version}&encording=json"

    def run(self: "WSClient") -> None:
        """Connect to the websocket feed"""
        self.__connect()

    async def __main(self: "WSClient") -> None:
        try:
            keep_waiting: bool = True
            async with ws.connect(self.URL) as socket:
                self.ws = socket
                await self.__authenticate()

                try:
                    while keep_waiting:
                        if (
                            not self.LAST_PING
                            or int(time.time()) - self.LAST_PING
                            > self.HEARTBEAT_INTERVAL
                        ):
                            await self.__send_ping()
                        try:
                            evt: Any = await asyncio.wait_for(
                                self.ws.recv(), timeout=self.HEARTBEAT_INTERVAL
                            )
                        except asyncio.TimeoutError:
                            self.LOG.info(
                                f"No message in {self.HEARTBEAT_INTERVAL} seconds"
                            )
                            await self.__send_ping()
                        except asyncio.CancelledError:
                            self.LOG.warning("Cancelled error")
                            await self.ws.ping()
                        else:
                            try:
                                evt_obj = json.loads(evt)
                                if (
                                    evt_obj["op"] != 11
                                    and "s" in evt_obj
                                    and evt_obj["s"]
                                ):
                                    # setting the SEQUENCE
                                    self.SEQUENCE = evt_obj["s"]
                                    if evt_obj["op"] == 10:
                                        self.HEARTBEAT_INTERVAL = (
                                            int(evt_obj["d"]["heartbeat_interval"])
                                            / 1000
                                        )
                            except ValueError as exc:
                                logging.warning(exc)
                            else:
                                await self.on_event(evt_obj)

                except ws.ConnectionClosed as exc:
                    keep_waiting = False
                    self.LOG.warning(
                        f"Websocket connection closed!  {exc} {traceback.format_exc()}"
                    )
                    await self._reconnect()
                except Exception as exc:
                    self.LOG.error(f"WS exception: {exc} {traceback.format_exc()}")
                    keep_waiting = False
                    await self._reconnect()

        except Exception as exc:
            self.LOG.error(f"Exception!: {exc} {traceback.format_exc()}")

    async def on_event(self: "WSClient", event: Any) -> None:
        """Overload this function!"""
        print(event)

    def __connect(self: "WSClient") -> None:
        """Connect to the websocket feed"""
        self.LOG.info("Connecting...")
        self.__conn = asyncio.ensure_future(  # pylint: disable=unused-private-member
            self.__main()
        )

    async def _reconnect(self: "WSClient") -> None:
        """Closes and reopens the websocket connection"""
        self.LOG.info("Reconnecting Websocket...")
        await self.__close_connection()
        self.__connect()

    async def __close_connection(self: "WSClient") -> None:
        """Closes the websocket connection"""
        await self.ws.close()

    async def send_message(self: "WSClient", message: dict) -> None:
        """Send a message via the websocket feed."""
        await self.ws.send(json.dumps(message))

    async def __send_ping(self: "WSClient") -> None:
        """Send a ping message"""
        self.LOG.info(f"Sending ping now, _sequence: {self.SEQUENCE}")
        await self.send_message({"op": 1, "d": self.SEQUENCE})
        self.LAST_PING = int(time.time())

    async def __authenticate(self: "WSClient") -> None:
        """Authentication"""
        await self.send_message(self.__get_payload(kind="init"))

    def __get_payload(self: "WSClient", kind: str) -> dict:
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
