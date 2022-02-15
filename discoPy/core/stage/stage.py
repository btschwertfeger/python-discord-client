
class Stage(object):
    '''Contains a collection of stage related methods.'''

    async def create_stage_instance(self, channel_id, topic: str, privacy_level: int=None) -> dict:
        '''https://discord.com/developers/docs/resources/stage-instance#create-stage-instance'''
        payload = {
            'channel_id': channel_id,
            'topic': topic
        }
        if privacy_level != None:
            payload['privacy_level'] = privacy_level
        return await awaitself._request('POST', params=payload, uri=f'/stage-instances')

    async def get_stage_instance(self, channel_id) -> dict:
        '''https://discord.com/developers/docs/resources/stage-instance#get-stage-instance'''
        return await awaitself._request('GET', uri=f'/stage-instances/{channel_id}')

    async def modify_stage_instance(self, topic: str=None, privacy_level=None) -> dict:
        '''https://discord.com/developers/docs/resources/stage-instance#modify-stage-instance'''
        payload = {}
        if topic != None:
            payload['topic'] = topic
        if privacy_level != None:
            payload['privacy_level'] = privacy_level
        return await awaitself._request('PATCH', params=payload, uri=f'/stage-instances/{channel_id}')

    async def delete_stage_instance(self) -> dict:
        '''https://discord.com/developers/docs/resources/stage-instance#delete-stage-instance'''
        return await awaitself._request('DELETE', uri=f'/stage-instances/{channel_id}')