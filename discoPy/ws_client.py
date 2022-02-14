
import asyncio
import websockets as ws
import sys, traceback
import json
import time 
import logging 
import numpy as np

import requests
class WSClient(object):
    '''
        Connect to the Discord websocket-feed.

        @param: token (str): required 
        @param: url (str):  required
    '''
    _heartbeat_interval = 41250 / 1000 # in seconds
    _last_ping = None
    _sequence = None

    all_intents = [
        'GUILDS', 'GUILD_MEMBERS', 'GUILD_BANS', 'GUILD_EMOJIS_AND_STICKERS', 'GUILD_INTEGRATIONS', 'GUILD_WEBHOOKS',
        'GUILD_INVITES', 'GUILD_VOICE_STATES', 'GUILD_PRESENCES', 'GUILD_MESSAGES', 'GUILD_MESSAGE_REACTIONS',
        'GUILD_MESSAGE_TYPING', 'DIRECT_MESSAGES','DIRECT_MESSAGE_REACTIONS', 'GUILD_SCHEDULED_EVENTS', 'GUILD_SCHEDULED_EVENTS'
    ]

    _url = 'wss://gateway.discord.gg/?v=9&encording=json'

    def __init__(self, token: str, intents: list, callback=None, url: str=None):
        self._log = logging.getLogger(__name__)

        self._token = token
        self._intents = np.sum([self._get_intents(intent) for intent in intents])

        if url != None:
            self._url = url

        self._callback = callback
        self._connect()

    async def _run(self) -> None:
        # self._log.info('Run!')
        try:
            keepwaiting = True
            async with ws.connect(self._url) as socket:
                self.ws = socket
                await self._authenticate() 

                try:
                    while keepwaiting:
                        if not self._last_ping or int(time.time()) - self._last_ping > self._get_ws_pingtimeout():
                            await self._send_ping()
                        try:
                            evt = await asyncio.wait_for(self.ws.recv(), timeout=self._get_ws_pingtimeout())
                        except asyncio.TimeoutError:
                            self._log.info(f'No message in {self._get_ws_pingtimeout()} seconds')
                            await self._send_ping()
                        except asyncio.CancelledError:
                            self._log.warn(f'Cancelled error')
                            await self.ws.ping()
                        else:
                            try:
                                evt_obj = json.loads(evt)
                                if evt_obj['op'] != 11 and 's' in evt_obj and evt_obj['s']: # setting the _sequence
                                    self._sequence = evt_obj['s']
                                    if evt_obj['op'] == 10:  
                                        self._heartbeat_interval = int(evt_obj['d']['heartbeat_interval']) / 1000
                            except ValueError:
                                pass
                            else:
                                if self._callback:
                                    await self._callback(evt_obj)
                    
                except ws.ConnectionClosed:
                    keep_waiting = False
                    self._log.warn(f'Websocket connection closed!  {e} {traceback.format_exc()}')
                    await self._reconnect()
                except Exception as e:
                    self._log.error(f'WS exception: {e} {traceback.format_exc()}')
                    keep_waiting = False
                    await self._reconnect()

        except Exception as e:
            self._log.error(f'Exception!: {e} {traceback.format_exc()}')


    def _connect(self) -> None:
        self._log.info('Connecting...')
        self._conn = asyncio.ensure_future(self._run())

    async def _reconnect(self) -> None:
        self._log.info('Reconnecting Websocket...')
        await self._close_connection()
        self._connect()
    
    async def _close_connection(self) -> None:
        await self.ws.close()

    async def send_message(self, message: dict) -> None:
        await self.ws.send(json.dumps(message))

    async def _send_ping(self):
        self._log.info(f'Sending ping now, _sequence: {self._sequence}')
        await self.send_message({
            'op': 1,
            'd': self._sequence
        })
        self._last_ping = int(time.time())
    
    async def _authenticate(self) -> None:
        await self.send_message(self._get_payload(kind='init'))

    def _get_ws_pingtimeout(self) -> None:
        return self._heartbeat_interval

    def _get_payload(self, kind: str) -> dict:
        '''https://discord.com/developers/docs/topics/gateway#identifying'''
        op = None
        if kind == 'reconnect':
            op = 7
        elif kind == 'resume':
            op = 6
        elif kind == 'init':
            op = 2
        else:
            raise ValueError
        return {
            'op': op,
            'd': {
                'token': self._token,
                'intents': f'{self._intents}',
                'properties': {
                    '$os': sys.platform,
                    '$browser': 'disco',
                    '$device': 'pc'
                },
                'compress': True
            }
        }
    @classmethod
    def get_intents_list(cls) -> list:
        return cls.all_intents

    def _get_intents(self, intents: str) -> int:
        # https://discord.com/developers/docs/topics/gateway#gateway-intents
        if intents == 'GUILDS':
            '''
                - GUILD_CREATE
                - GUILD_UPDATE
                - GUILD_DELETE
                - GUILD_ROLE_CREATE
                - GUILD_ROLE_UPDATE
                - GUILD_ROLE_DELETE
                - CHANNEL_CREATE
                - CHANNEL_UPDATE
                - CHANNEL_DELETE
                - CHANNEL_PINS_UPDATE
                - THREAD_CREATE
                - THREAD_UPDATE
                - THREAD_DELETE
                - THREAD_LIST_SYNC
                - THREAD_MEMBER_UPDATE
                - THREAD_MEMBERS_UPDATE
                - STAGE_INSTANCE_CREATE
                - STAGE_INSTANCE_UPDATE
                - STAGE_INSTANCE_DELETE
            '''
            return (1 << 0)
        elif intents == 'GUILD_MEMBERS':
            '''
                - GUILD_MEMBER_ADD
                - GUILD_MEMBER_UPDATE
                - GUILD_MEMBER_REMOVE
                - THREAD_MEMBERS_UPDATE *
            '''
            return (1 << 1)
        elif intents == 'GUILD_BANS':
            '''
                - GUILD_BAN_ADD
                - GUILD_BAN_REMOVE
            '''
            return (1 << 2)
        elif intents == 'GUILD_EMOJIS_AND_STICKERS':
            '''
                - GUILD_EMOJIS_UPDATE
                - GUILD_STICKERS_UPDATE
            '''
            return (1 << 3)
        elif intents == 'GUILD_INTEGRATIONS': 
            '''
                - GUILD_INTEGRATIONS_UPDATE
                - INTEGRATION_CREATE
                - INTEGRATION_UPDATE
                - INTEGRATION_DELETE
            '''
            return (1 << 4)
        elif intents == 'GUILD_WEBHOOKS':
            '''
                - WEBHOOKS_UPDATE
            '''
            return (1 << 5)
        elif intents == 'GUILD_INVITES':
            '''
                - INVITE_CREATE
                - INVITE_DELETE
            '''
            return (1 << 6)
        elif intents == 'GUILD_VOICE_STATES': 
            '''
                - VOICE_STATE_UPDATE
            '''
            return (1 << 7)
        elif intents == 'GUILD_PRESENCES': 
            '''
                - PRESENCE_UPDATE
            '''
            return (1 << 8)
        elif intents == 'GUILD_MESSAGES':
            '''
                - MESSAGE_CREATE
                - MESSAGE_UPDATE
                - MESSAGE_DELETE
                - MESSAGE_DELETE_BULK
            '''
            return  (1 << 9)
        elif intents == 'GUILD_MESSAGE_REACTIONS':
            '''
                - MESSAGE_REACTION_ADD
                - MESSAGE_REACTION_REMOVE
                - MESSAGE_REACTION_REMOVE_ALL
                - MESSAGE_REACTION_REMOVE_EMOJI
            '''
            return  (1 << 10)
        elif intents == 'GUILD_MESSAGE_TYPING': 
            '''
                - TYPING_START
            '''
            return (1 << 11)
        elif intents == 'DIRECT_MESSAGES':
            '''
                - MESSAGE_CREATE
                - MESSAGE_UPDATE
                - MESSAGE_DELETE
                - CHANNEL_PINS_UPDATE
            '''
            return (1 << 12)
        elif intents == 'DIRECT_MESSAGE_REACTIONS': 
            '''
                - MESSAGE_REACTION_ADD
                - MESSAGE_REACTION_REMOVE
                - MESSAGE_REACTION_REMOVE_ALL
                - MESSAGE_REACTION_REMOVE_EMOJI
            '''
            return (1 << 13)
        elif intents == 'DIRECT_MESSAGE_TYPING': 
            '''
                - TYPING_START
            '''
            return (1 << 14)
        elif intents == 'GUILD_SCHEDULED_EVENTS': 
            '''
                - GUILD_SCHEDULED_EVENT_CREATE
                - GUILD_SCHEDULED_EVENT_UPDATE
                - GUILD_SCHEDULED_EVENT_DELETE
                - GUILD_SCHEDULED_EVENT_USER_ADD
                - GUILD_SCHEDULED_EVENT_USER_REMOVE
            '''
            return (1 << 16)
        else:
            raise Exception('Uknown Intent!')