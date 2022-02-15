import asyncio
import logging
# import re
import sys
# from typing import IO
import urllib.error
import urllib.parse
import json
import aiohttp
from aiohttp import ClientSession

logging.basicConfig(
    format='%(asctime)s %(levelname)s:%(name)s: %(message)s',
    level=logging.WARNING,
    datefmt='%H:%M:%S',
    stream=sys.stderr,
)
logger = logging.getLogger(__name__)
logging.getLogger('chardet.charsetprober').disabled = True

from discoPy.core.application.application import Application
from discoPy.core.guild.guild import Guild
from discoPy.core.channel.channel import Channel
from discoPy.core.stage.stage import Stage
from discoPy.core.user.user import User
from discoPy.core.webhook.webhook import Webhook

class BaseClient(Application, Guild, Channel, Stage, User, Webhook):

    BASE_URL = 'https://discord.com/api/v9'
    TIMEOUT = 10
    headers = { 
        'content-type': 'application/json',
        'user-agent': 'python-discord-client'
    }

    def __init__(self, token: str, api_version: int=None) -> None:
        self._token = token
        if api_version != None:
            self.BASE_URL = f'https://discord.com/api/v{api_version}'
        
        self.headers['Authorization'] =  f'Bot {self._token}'

        self._callbacks = { 
            'on_event': [self.on_event] 
        }

    async def _request(self, method: str, params: dict={}, uri: str='', headers: dict={}, files: dict=None, **kwargs) -> dict:
        data_json = ''
        if method in ['GET', 'DELETE']:
            if params:
                strl = []
                for key in sorted(params):
                    strl.append('{}={}'.format(key, params[key]))
                data_json += '&'.join(strl)
                uri += f'?{data_json}'
        else:
            if params:
                data_json = params 
        try:
            payload = json.dumps(data_json)
        except:
            payload = data_json

        url = f'{self.BASE_URL}{uri}'
        response = None
        try:
            async with ClientSession(headers=self.headers) as session:
                if method == 'GET':
                    response = await session.request(method=method, url=url, headers=headers, timeout=self.TIMEOUT, **kwargs)
                elif method == 'DELETE':
                    response = await session.request(method=method, url=url, headers=headers, timeout=self.TIMEOUT, **kwargs)
                elif method == 'POST':
                    response = await session.request(method=method, url=url, data=payload, headers=headers,  timeout=self.TIMEOUT, **kwargs)
                elif method == 'PATCH':
                    response = await session.request(method=method, url=url, data=payload, headers=headers, timeout=self.TIMEOUT, **kwargs)
                elif method == 'PUT':
                    response = await session.request(method=method, url=url, data=payload, headers=headers, timeout=self.TIMEOUT, **kwargs)
        except (
            aiohttp.ClientError,
            aiohttp.http_exceptions.HttpProcessingError,
        ) as e:
            logger.error(
                'aiohttp exception for %s [%s]: %s',
                url,
                getattr(e, 'status', None),
                getattr(e, 'message', None),
            )
        except Exception as e:
            logger.exception('Non-aiohttp exception occured:  %s', getattr(e, '__dict__', {}))
        else:
            if response != None:
                return await self._check_response(response)
            else:
                print('!')

    async def _check_response(self, response) -> dict:
        if response.status == 200:
            try:
                 data = await response.json()
            except ValueError:
                raise Exception(response.text())
            else:
                return data
        else:
            raise Exception(f'{response.status}: {await response.text()}')


    async def _send_file_attachment(self, method: str, uri: str, file_names: [str], payload: dict={}) -> dict:
        raise NotImplementedError('Sorry, this is not working the asynchron way. Use the Rest endpoint instead! (discopy.rest.channel)')
        headers = { 'content-disposition': 'form-data; name="payload_json"', 'content-type': 'multipart/form-data' }
        payload = { 'payload_json': json.dumps(payload) }
        
        
        prepared_files = {}
        # for i, filename in enumerate(file_names):
        #     prepared_files[f'files[{i}]'] = (filename, open(filename, 'rb'), {
        #         'Content-Disposition': f'form-data; name="files[{i}]"; filename="{filename}"'
        #         }
        #     )

        # for key in prepared_files:
        #     payload[key] = prepared_files[key]

        print(payload)

        with aiohttp.MultipartWriter('mixed') as mp:
            y = mp.append_json(payload)
            x = mp.append(open('test.png','rb').read(), {
                'content-type': 'image/png',
                'Content-Disposition': 'form-data; name="files[0]"; filename="test.png"'
            })
        
            # payload2 = aiohttp.payload.get_payload(open('test.png', 'rb'))#, headers=headers)
            # payload2.set_content_disposition(
            #     'form-data',
            #     name='files[0]',
            #     filename='test.png'
            # )
            # payload2._headers['Content-Disposition'] = 'form-data; name="files[0]"; filename="test.png"'
            # Add part to multipart
            # part = mp.append(payload2)

        return await self._request(method, params=mp,  headers=headers, uri=uri)


    async def on(self, event_name: str, callback):
        if event_name not in self._callbacks:
            self._callbacks[event_name] = [callback]
        else:
            self._callbacks[event_name].append(callback)

    async def trigger(self, event_name: str, event_object):
        if event_name in self._callbacks:
            for callback in self._callbacks[event_name]:
                await callback(event_object)

    async def on_event(self, event) -> None:
        pass

