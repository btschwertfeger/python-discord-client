from discoPy.rest.base_request.base_request import BaseRequestAPI

class WebhookData(BaseRequestAPI):
    '''Contains a collection of webhook related methods.'''

    def __init__(self, token: str, url: str=None):
        super().__init__(token, url)

    def create_webhook(self, channel_id, name: str, avatar=None) -> dict:
        '''https://discord.com/developers/docs/resources/webhook#create-webhook'''
        payload = { 'name': name, 'avatar': avatar }
        payload = {k:v for k,v in payload.items() if v is not None}
        return self._request('POST', params=payload, uri=f'/channels/{channel_id}/webhooks')

    def get_channel_webhooks(self, channel_id) -> dict:
        '''https://discord.com/developers/docs/resources/webhook#create-webhook'''
        return self._request('GET', uri=f'/channels/{channel_id}/webhooks')

    def get_guild_webhooks(self, guild_id) -> dict:
        '''https://discord.com/developers/docs/resources/webhook#get-guild-webhooks'''
        return self._request('GET', uri=f'/guilds/{guild_id}/webhooks')

    def get_webhook(self, webhook_id) -> dict:
        '''https://discord.com/developers/docs/resources/webhook#get-webhook'''
        return self._request('GET', uri=f'/webhooks/{webhook_id}')

    def get_webhook_with_token(self, webhook_id, webhook_token: str) -> dict:
        '''https://discord.com/developers/docs/resources/webhook#get-webhook-with-token'''
        return self._request('GET', uri=f'/webhooks/{webhook_id}/{webhook_token}')

    def modify_webhook(self, webhook_id, name: str=None, avatar=None, channel_id=None) -> dict:
        '''https://discord.com/developers/docs/resources/webhook#modify-webhook'''
        payload = {
            'name': name,
            'avatar': avatar,
            'channel_id': channel_id
        }
        payload = {k:v for k,v in payload.items() if v is not None}
        return self._request('PATCH', params=payload, uri=f'/webhooks/{webhook_id}')

    def modify_webhook_with_token(self, webhook_id, webhook_token, name: str=None, avatar=None) -> dict:
        '''https://discord.com/developers/docs/resources/webhook#modify-webhook-with-token'''
        payload = { 'name': name, 'avatar': avatar }
        payload = {k:v for k,v in payload.items() if v is not None}
        return self._request('PATCH', params=payload, uri=f'/webhooks/{webhook_id}/{webhook_token}')

    def delete_webhook(self) -> dict:
        '''https://discord.com/developers/docs/resources/webhook#delete-webhook'''
        return self._request('DELETE', uri=f'/webhooks/{webhook_id}')

    def delete_webhook_with_token(self, webhook_id, webhook_token) -> dict:
        '''https://discord.com/developers/docs/resources/webhook#delete-webhook-with-token'''
        return self._request('DELETE', uri=f'/webhooks/{webhook_id}/{webhook_token}')

    def execute_webhook(self, 
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
        payload = {
            'content': content,
            'username': username,
            'avatar_url': avatar_url,
            'tts': tts,
            'allowed_mentions': allowed_mentions,
            'components': components,
            'files': files,
            'payload_json': payload_json,
            'attachments': attachments,
            'flags': flags
        }
        payload = {k:v for k,v in payload.items() if v is not None}
        uri = f'/webhooks/{webhook_id}/{webhook_token}'
        if wait or thread_id != None:
            uri = f'{uri}?{wait}&thread_id={thread_id}'
        return self._request('POST', params=payload, uri=uri)

    def execute_slack_compatible_webhook(self) -> dict:
        '''https://discord.com/developers/docs/resources/webhook#execute-slackcompatible-webhook'''
        raise NotImplementedError()

    def execute_github_compatible_webhook(self) -> dict:
        '''https://discord.com/developers/docs/resources/webhook#execute-githubcompatible-webhook'''
        raise NotImplementedError()

    def get_webhook_messages(self, webhook_id, webhook_token, message_id, thread_id=None) -> dict:
        '''https://discord.com/developers/docs/resources/webhook#get-webhook-message'''
        payload = { 'thread_id': thread_id}
        payload = {k:v for k,v in payload.items() if v is not None}
        return self._request('GET', params=payload, uri=f'/webhooks/{webhook_id}/{webhook_token}/messages/{message_id}')

    def edit_webhook_messages(self) -> dict:
        '''https://discord.com/developers/docs/resources/webhook#edit-webhook-message'''
        raise NotImplementedError()

    def delete_webhook_messages(self, webhook_id, webhook_token, message_id) -> dict:
        '''https://discord.com/developers/docs/resources/webhook#delete-webhook-message'''
        return self._request('DELETE', uri=f'/webhooks/{webhook_id}/{webhook_token}/messages/{message_id}')

    def get_original_interaction_response(self, application_id, interaction_token, thread_id=None) -> dict:
        '''https://discord.com/developers/docs/interactions/receiving-and-responding#get-original-interaction-response'''
        payload = { 'thread_id': thread_id }
        payload = {k:v for k,v in payload.items() if v is not None}
        return self._request('GET', params=parapayloadms, uri=f'/webhooks/{application_id}/{interaction_token}/messages/@original')

    def edit_original_interaction_response(self, application_id, interaction_token) -> dict:
        '''https://discord.com/developers/docs/interactions/receiving-and-responding#edit-original-interaction-response'''
        raise NotImplementedError()
        #return self._request('PATCH', uri=f'/webhooks/{application_id}/{interaction_token}/messages/@original')
        
    def delete_original_interaction_response(self, application_id, interaction_token) -> dict:
        '''https://discord.com/developers/docs/interactions/receiving-and-responding#delete-original-interaction-response'''
        return self._request('DELETE', uri=f'/webhooks/{application_id}/{interaction_token}/messages/@original')

    def create_followup_message(self, 
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
        payload = {
            'content': content,
            'tts': tts,
            'allowed_mentions': allowed_mentions,
            'components': components,
            'files': files,
            'payload_json': payload_json,
            'attachments': attachments,
            'flags': flags
        }
        payload = {k:v for k,v in payload.items() if v is not None}
        return self._request('POST', params=payload, uri=f'/webhooks/{application_id}/{interaction_token}')

    def get_followup_message(self, application_id, interaction_token, message_id, thread_id=None) -> dict:
        '''https://discord.com/developers/docs/interactions/receiving-and-responding#get-followup-message'''
        payload = { 'thread_id': thread_id}
        payload = {k:v for k,v in payload.items() if v is not None}
        return self._request('GET', params=payload, uri=f'/webhooks/{application_id}/{interaction_token}/messages/{message_id}')

    def edit_followup_message(self, application_id, interaction_token, message_id) -> dict:
        '''https://discord.com/developers/docs/interactions/receiving-and-responding#edit-followup-message'''
        raise NotImplementedError()
        #return self._request('PATCH', uri=f'/webhooks/{application_id}/{interaction_token}/messages/{message_id}')

    def delete_followup_message(self, application_id, interaction_token, message_id) -> dict:
        '''https://discord.com/developers/docs/interactions/receiving-and-responding#delete-followup-message'''
        return self._request('DELETE', uri=f'/webhooks/{application_id}/{interaction_token}/messages/{message_id}')

