from discoPy.base_request.base_request import BaseRequestAPI

class UserData(BaseRequestAPI):
    '''Contains a collection of user related methods.'''
    
    def __init__(self, token: str, url: str=None):
        super().__init__(token, url)

    def get_current_user(self) -> dict:
        '''https://discord.com/developers/docs/resources/user#get-current-user'''
        return self._request(method='GET', uri=f'/users/@me')

    def get_user(self, user_id) -> dict:
        '''https://discord.com/developers/docs/resources/user#get-user'''
        return self._request(method='GET', uri=f'/users/{user_id}')

    def modify_current_user(self, username: str=None, avatar=None) -> dict:
        '''https://discord.com/developers/docs/resources/user#modify-current-user'''
        payload = { }
        if username != None:
            payload['username'] = username
        if avatar != None:
            payload['avatar'] = avatar
        return self._request(method='PATCH', params=payload, uri=f'/users/@me')

    def get_current_user_guilds(self, before=None, after=None, limit: int=None) -> dict:
        '''https://discord.com/developers/docs/resources/user#get-current-user-guilds'''
        params = { }
        if before != None:
            params['before'] = before
        if after != None:
            params['after'] = after
        if limit != None:
            params['limit'] = limit
        return self._request(method='GET', params=params, uri=f'/users/@me/guilds')

    def get_current_user_guild_member(self, guild_id) -> dict:
        '''https://discord.com/developers/docs/resources/user#get-current-user-guild-member'''
        return self._request(method='GET', uri=f'/users/@me/guilds/{guild_id}/member')

    def leave_guild(self, guild_id) -> dict:
        '''https://discord.com/developers/docs/resources/user#leave-guild'''
        return self._request(method='DELETE', uri=f'/users/@me/guilds/{guild_id}')

    def create_dm(self, recipient_id) -> dict:
        '''https://discord.com/developers/docs/resources/user#create-dm'''
        payload = { 'recipient_id': recipient_id }
        return self._request(method='POST', params=payload, uri=f'/users/@me/channels')

    def create_group_dm(self, access_tokens: list, nicks: dict) -> dict:
        '''https://discord.com/developers/docs/resources/user#create-group-dm'''
        payload = {
            'access_tokens': access_tokens,
            'nicks': nicks
        }
        return self._request(method='POST', params=payload, uri=f'/users/@me/channels')

    def get_user_connections(self) -> dict:
        '''https://discord.com/developers/docs/resources/user#get-user-connections'''
        return self._request(method='GET', uri=f'/users/@me/connections')

    def list_voice_regions(self) -> dict:
        '''https://discord.com/developers/docs/resources/voice#list-voice-regions'''
        return self._request(method='GET', uri=f'/voice/regions')

    def get_invite(self, invite_code, with_counts: bool=None, with_expiration: bool=None, guild_scheduled_event_id=None) -> dict:
        '''https://discord.com/developers/docs/resources/invite#get-invite'''
        params = {}
        if with_counts != None:
            params['with_counts'] = with_counts
        if with_expiration != None:
            params['with_expiration'] = with_expiration
        if guild_scheduled_event_id != None:
            params['guild_scheduled_event_id'] = guild_scheduled_event_id
        return self._request(method='GET', params=params, uri=f'/invites/{invite_code}')

    def delete_invite(self, invite_code) -> dict:
        '''https://discord.com/developers/docs/resources/invite#delete-invite'''
        return self._request(method='DELETE', params=params, uri=f'/invites/{invite_code}')



    