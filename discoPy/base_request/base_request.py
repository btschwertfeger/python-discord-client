import requests
import json

class BaseRequestAPI(object):

    BASE_URL = 'https://discord.com/api/v9'
    TIMEOUT = 10

    def __init__(self, token: str, url: str=None):
        self._token = token
        if url != None:
            self.BASE_URL = url
        self._session = self._get_session()

    def _request(self, method: str, params={}, uri: str='', headers: dict={}, files:dict=None) -> dict:
        uri_path = uri
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

        if method == 'GET':
            response = self._session.get(url=url, headers=headers, timeout=self.TIMEOUT)
        elif method == 'DELETE':
            response = self._session.delete(url=url, headers=headers, timeout=self.TIMEOUT)
        elif method == 'POST':
            response = self._session.post(url=url, data=payload, headers=headers, files=files, timeout=self.TIMEOUT)
        elif method == 'PATCH':
            response = self._session.patch(url=url, data=payload, headers=headers, timeout=self.TIMEOUT)
        elif method == 'PUT':
            response = self._session.put(url=url, data=payload, headers=headers, timeout=self.TIMEOUT)
        if response != None:
            return self.check_response(response)

    def _get_session(self) -> requests.Session:
        session = requests.Session()
        session.headers.update({
            'authorization': f'Bot {self._token}',
            'content-type': 'application/json',
            'user-agent': 'python-discord-client'
        })

        return session

    def _send_file_attachment(self, method: str, uri: str, file_names: [str], payload: dict={}, headers: dict={}) -> dict:
        self._session.headers.update({ 'content-type': None })
        headers = { 'content-disposition': 'form-data; name="payload_json"' }
        payload = { 'payload_json': json.dumps(payload) }
        prepared_files = {}
        for i, filename in enumerate(file_names):
            file_type = filename.split('.')[-1]
            media_type=None
            if file_type in ['jpg', 'png', 'jpeg', 'gif']:
                media_type = 'image'
                if file_type == 'svg':
                    file_type = 'svg+xml'

            prepared_files[f'files[{i}]'] = (filename, open(filename, 'rb'), f'{media_type}/{file_type}', {
                'Content-Disposition': f'form-data; name="files[{i}]"; filename="{filename}"'
                }
            )

        for key in prepared_files:
            payload[key] = prepared_files[key]

        response = self._request(method, params=payload, files=prepared_files, headers=headers, uri=uri)
        self._session.headers.update({ 'content-type': 'application/json' })
        return response

    @staticmethod
    def check_response(response_data) -> dict:
        if response_data.status_code == 200:
            try:
                data = response_data.json()
                # print(response_data.request.prepare_headers)
            except ValueError:
                raise Exception(response_data.content)
            else:
                return data
        else:
            raise Exception(f'{response_data.status_code}: {response_data.text}')