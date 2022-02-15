
class Webhook(object):
    '''Contains a collection of webhook related methods.'''
    
    async def create_webhook(self, channel_id, name: str, avatar=None) -> dict:
        '''https://discord.com/developers/docs/resources/webhook#create-webhook'''
        payload = { 'name': name }
        if avatar != None:
            payload['avatar'] = avatar
        return await self._request('POST', params=payload, uri=f'/channels/{channel_id}/webhooks')

    async def get_channel_webhooks(self, channel_id) -> dict:
        '''https://discord.com/developers/docs/resources/webhook#create-webhook'''
        return await self._request('GET', uri=f'/channels/{channel_id}/webhooks')

    async def get_guild_webhooks(self, guild_id) -> dict:
        '''https://discord.com/developers/docs/resources/webhook#get-guild-webhooks'''
        return await self._request('GET', uri=f'/guilds/{guild_id}/webhooks')

    async def get_webhook(self, webhook_id) -> dict:
        '''https://discord.com/developers/docs/resources/webhook#get-webhook'''
        return await self._request('GET', uri=f'/webhooks/{webhook_id}')

    async def get_webhook_with_token(self, webhook_id, webhook_token: str) -> dict:
        '''https://discord.com/developers/docs/resources/webhook#get-webhook-with-token'''
        return await self._request('GET', uri=f'/webhooks/{webhook_id}/{webhook_token}')

    async def modify_webhook(self, webhook_id, name: str=None, avatar=None, channel_id=None) -> dict:
        '''https://discord.com/developers/docs/resources/webhook#modify-webhook'''
        payload = {}
        if name != None:
            payload['name'] = name
        if avatar != None:
            payload['avatar'] = avatar
        if channel_id != None:
            payload['channel_id'] = channel_id
        return await self._request('PATCH', params=payload, uri=f'/webhooks/{webhook_id}')

    async def modify_webhook_with_token(self, webhook_id, webhook_token, name: str=None, avatar=None) -> dict:
        '''https://discord.com/developers/docs/resources/webhook#modify-webhook-with-token'''
        payload = {}
        if name != None:
            payload['name'] = name
        if avatar != None:
            payload['avatar'] = avatar
        return await self._request('PATCH', params=payload, uri=f'/webhooks/{webhook_id}/{webhook_token}')

    async def delete_webhook(self) -> dict:
        '''https://discord.com/developers/docs/resources/webhook#delete-webhook'''
        return await self._request('DELETE', uri=f'/webhooks/{webhook_id}')

    async def delete_webhook_with_token(self, webhook_id, webhook_token) -> dict:
        '''https://discord.com/developers/docs/resources/webhook#delete-webhook-with-token'''
        return await self._request('DELETE', uri=f'/webhooks/{webhook_id}/{webhook_token}')

    async def execute_webhook(self, 
        wait: bool=False, 
        thread_id=None, 
        content: str=None, 
        username: str=None,
        avatar_url: str=None,
        tts: bool=None,
        embeds: list=None,
        allowed_mentions=None,
        components: list=None,
        files=None,
        payload_json: dict=None,
        attachments: list=None,
        flags: int=None
    ) -> dict:
        '''https://discord.com/developers/docs/resources/webhook#execute-webhook
        ! Note that when sending a message, you must provide a value for at least one of content, embeds, or file.
        '''
        payload = {}
        if content != None:
            payload['content'] = content
        if username != None:
            payload['username'] = username
        if avatar_url != None:
            payload['avatar_url'] = avatar_url
        if tts != None:
            payload['tts'] = tts
        if allowed_mentions != None:
            payload['allowed_mentions'] = allowed_mentions
        if components != None:
            payload['components'] = components
        if files != None:
            payload['files'] = files
        if payload_json != None:
            payload['payload_json'] = payload_json
        if attachments != None:
            payload['attachments'] = attachments
        if flags != None:
            payload['flags'] = flags

        uri = f'/webhooks/{webhook_id}/{webhook_token}'
        if wait or thread_id != None:
            uri = f'{uri}?{wait}&thread_id={thread_id}'
        return await self._request('POST', params=payload, uri=uri)

    async def execute_slack_compatible_webhook(self) -> dict:
        '''https://discord.com/developers/docs/resources/webhook#execute-slackcompatible-webhook'''
        raise NotImplementedError()

    async def execute_github_compatible_webhook(self) -> dict:
        '''https://discord.com/developers/docs/resources/webhook#execute-githubcompatible-webhook'''
        raise NotImplementedError()

    async def get_webhook_messages(self, webhook_id, webhook_token, message_id, thread_id=None) -> dict:
        '''https://discord.com/developers/docs/resources/webhook#get-webhook-message'''
        params = {}
        if thread_id != None:
            params['thread_id'] = thread_id
        return await self._request('GET', params=params, uri=f'/webhooks/{webhook_id}/{webhook_token}/messages/{message_id}')

    async def edit_webhook_messages(self) -> dict:
        '''https://discord.com/developers/docs/resources/webhook#edit-webhook-message'''
        raise NotImplementedError()

    async def delete_webhook_messages(self, webhook_id, webhook_token, message_id) -> dict:
        '''https://discord.com/developers/docs/resources/webhook#delete-webhook-message'''
        return await self._request('DELETE', uri=f'/webhooks/{webhook_id}/{webhook_token}/messages/{message_id}')

    async def get_original_interaction_response(self, application_id, interaction_token, thread_id=None) -> dict:
        '''https://discord.com/developers/docs/interactions/receiving-and-responding#get-original-interaction-response'''
        params = {}
        if thread_id != None:
            params['thread_id'] = thread_id
        return await self._request('GET', params=params, uri=f'/webhooks/{application_id}/{interaction_token}/messages/@original')

    async def edit_original_interaction_response(self, application_id, interaction_token) -> dict:
        '''https://discord.com/developers/docs/interactions/receiving-and-responding#edit-original-interaction-response'''
        raise NotImplementedError()
        #return await self._request('PATCH', uri=f'/webhooks/{application_id}/{interaction_token}/messages/@original')
        
    async def delete_original_interaction_response(self, application_id, interaction_token) -> dict:
        '''https://discord.com/developers/docs/interactions/receiving-and-responding#delete-original-interaction-response'''
        return await self._request('DELETE', uri=f'/webhooks/{application_id}/{interaction_token}/messages/@original')

    async def create_followup_message(self, 
        application_id, 
        interaction_token,
        content: str=None, 
        tts: bool=None,
        embeds: list=None,
        allowed_mentions=None,
        components: list=None,
        files=None,
        payload_json: dict=None,
        attachments: list=None,
        flags: int=None
    ) -> dict:
        '''https://discord.com/developers/docs/interactions/receiving-and-responding#create-followup-message'''
        payload = {}
        if content != None:
            payload['content'] = content
        if tts != None:
            payload['tts'] = tts
        if allowed_mentions != None:
            payload['allowed_mentions'] = allowed_mentions
        if components != None:
            payload['components'] = components
        if files != None:
            payload['files'] = files
        if payload_json != None:
            payload['payload_json'] = payload_json
        if attachments != None:
            payload['attachments'] = attachments
        if flags != None:
            payload['flags'] = flags

        return await self._request('POST', params=payload, uri=f'/webhooks/{application_id}/{interaction_token}')

    async def get_followup_message(self, application_id, interaction_token, message_id, thread_id=None) -> dict:
        '''https://discord.com/developers/docs/interactions/receiving-and-responding#get-followup-message'''
        params = {}
        if thread_id != None:
            params['thread_id'] = thread_id
        return await self._request('GET', params=params, uri=f'/webhooks/{application_id}/{interaction_token}/messages/{message_id}')

    async def edit_followup_message(self, application_id, interaction_token, message_id) -> dict:
        '''https://discord.com/developers/docs/interactions/receiving-and-responding#edit-followup-message'''
        raise NotImplementedError()
        #return await self._request('PATCH', uri=f'/webhooks/{application_id}/{interaction_token}/messages/{message_id}')

    async def delete_followup_message(self, application_id, interaction_token, message_id) -> dict:
        '''https://discord.com/developers/docs/interactions/receiving-and-responding#delete-followup-message'''
        return await self._request('DELETE', uri=f'/webhooks/{application_id}/{interaction_token}/messages/{message_id}')

