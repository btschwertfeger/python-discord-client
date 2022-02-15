from discoPy.rest.base_request.base_request import BaseRequestAPI

class StageData(BaseRequestAPI):
    '''Contains a collection of stage related methods.'''

    def __init__(self, token: str, url: str=None):
        super().__init__(token, url)

    def create_stage_instance(self, channel_id, topic: str, privacy_level: int=None) -> dict:
        '''https://discord.com/developers/docs/resources/stage-instance#create-stage-instance'''
        payload = {
            'channel_id': channel_id,
            'topic': topic
        }
        if privacy_level != None:
            payload['privacy_level'] = privacy_level
        return self._request('POST', params=payload, uri=f'/stage-instances')

    def get_stage_instance(self, channel_id) -> dict:
        '''https://discord.com/developers/docs/resources/stage-instance#get-stage-instance'''
        return self._request('GET', uri=f'/stage-instances/{channel_id}')

    def modify_stage_instance(self, topic: str=None, privacy_level=None) -> dict:
        '''https://discord.com/developers/docs/resources/stage-instance#modify-stage-instance'''
        payload = {}
        if topic != None:
            payload['topic'] = topic
        if privacy_level != None:
            payload['privacy_level'] = privacy_level
        return self._request('PATCH', params=payload, uri=f'/stage-instances/{channel_id}')

    def delete_stage_instance(self) -> dict:
        '''https://discord.com/developers/docs/resources/stage-instance#delete-stage-instance'''
        return self._request('DELETE', uri=f'/stage-instances/{channel_id}')