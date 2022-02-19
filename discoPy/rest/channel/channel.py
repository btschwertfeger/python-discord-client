from discoPy.rest.base_request.base_request import BaseRequestAPI
import json


class ChannelData(BaseRequestAPI):
    '''Contains a collection of channel related methods.'''

    def __init__(self, token: str, url: str=None):
        super().__init__(token, url)
            
    def get_channel(self, channel_id) -> dict:
        '''https://discord.com/developers/docs/resources/channel#get-channel'''
        return self._request('GET', uri=f'/channels/{channel_id}')

    def modify_channel(self, 
        channel_id,
        name: str=None,     
        icon=None, 
        type: int=None,
        position: int=None,
        topic: str=None,
        nsfw: bool=None,
        rate_limit_per_user: int=None,
        bitrate: int=None,
        user_limit: int=None,
        permission_overwrites: list=None,
        parent_id=None,
        rtc_region: str=None,
        video_quality_mode: int=None,
        default_auto_archive_duration: int=None,
        archived: bool=None,
        auto_archive_duration: int=None,
        locked: bool=None,
        invitable: bool=None,
        **kwargs
    ) -> dict:
        '''https://discord.com/developers/docs/resources/channel#modify-channel
            
            ----- P A R M E T E R S -----
            If Channel == Group DM
                @name
                @icon
            If Channel == Guild Channel
                @name
                @type
                @position
                @topic
                @nsfw
                @rate_limit_per_user
                @bitrate
                @user_limit
                @permission_overwrites
                @parent_id
                @rtc_region
                @video_quality_mode
                @default_auto_archive_duration
            If Chanel == Thread
                @name
                @archived
                @auto_archive_duration
                @locked
                @invitable
                @rate_limit_per_user
        '''
        payload = {
            'name': name,
            'icon': icon,
            'type': type,
            'topic': topic,
            'nsfw': nsfw,
            'rate_limit_per_user': rate_limit_per_user,
            'bitrate': bitrate,
            'user_limit': user_limit,
            'permission_overwrites': permission_overwrites,
            'parent_id': parent_id,
            'rtc_region': rtc_region,
            'video_quality_mode': video_quality_mode,
            'default_auto_archive_duration': default_auto_archive_duration,
            'archived': archived,
            'auto_archive_duration': auto_archive_duration,
            'locked': locked,
            'invitable': invitable
        }        
        payload = {k:v for k,v in payload.items() if v is not None}
        return  self._request('PATCH', params=payload, uri=f'/channels/{channel_id}')
        
    def delete_close_channel(self, channel_id) -> dict:
        '''https://discord.com/developers/docs/resources/channel#deleteclose-channel'''
        return  self._request('DELETE', uri=f'/channels/{channel_id}')

    def get_channel_messages(self,
        channel_id,
        around=None,
        before=None,
        after=None,
        limit: int=None,
    ) -> dict:
        '''https://discord.com/developers/docs/resources/channel#get-channel-messages'''
        payload = {
            'around': around,
            'before': before,
            'after': after,
            'limit': limit
        }
        payload = {k:v for k,v in payload.items() if v is not None}
        return  self._request('GET', params=payload, uri=f'/channels/{channel_id}/messages')

    def get_channel_message(self) -> dict:
        '''https://discord.com/developers/docs/resources/channel#get-channel-message'''
        return  self._request('GET',uri=f'/channels/{channel_id}/messages')

    def create_message(self,
        channel_id,
        content: str=None,
        tts: bool=None,
        embeds: [dict]=None,
        allowed_mentions=None,
        message_reference=None,
        components: list=None,
        files: [str]=None,
        attachments: [dict]=None,
        sticker_ids: list=None,
        flags: int=None,
    ) -> dict:
        '''https://discord.com/developers/docs/resources/channel#create-message'''

        payload = {
            'content': content,
            'tts': tts,
            'allowed_mentions': allowed_mentions,
            'message_reference': message_reference,
            'components': components,
            'sticker_ids': sticker_ids,
            'flags': flags,
            'embeds': embeds,
            'attachments': attachments
        }
        payload = {k:v for k,v in payload.items() if v is not None}
        uri = f'/channels/{channel_id}/messages'
        if files != None:
            return  self._send_file_attachment(method='POST', uri=uri, file_names=files, payload=payload)
        else:
            return  self._request(method='POST', uri=uri, params=payload)

    def crosspost_message(self, message_id, channel_id) -> dict:
        '''https://discord.com/developers/docs/resources/channel#crosspost-message'''
        response = self._request('POST', uri=f'/channels/{channel_id}/messages/{message_id}/crosspost')

    def create_reaction(self, channel_id, message_id, emoji) -> dict:
        '''https://discord.com/developers/docs/resources/channel#create-reaction
            "The emoji must be URL Encoded or the request will fail with 10014: Unknown Emoji. 
            To use custom emoji, you must encode it in the format name:id with the emoji name and emoji id."
        '''
        response = self._request('PUT', uri=f'/channels/{channel_id}/messages/{message_id}/reactions/{emoji}/@me')

    def delete_own_reaction(self, channel_id, message_id, emoji) -> dict:
        '''https://discord.com/developers/docs/resources/channel#delete-own-reaction
            "The emoji must be URL Encoded or the request will fail with 10014: Unknown Emoji. 
            To use custom emoji, you must encode it in the format name:id with the emoji name and emoji id."
        '''
        response = self._request('DELETE', uri=f'/channels/{channel_id}/messages/{message_id}/reactions/{emoji}/@me')

    def delete_user_reaction(self, channel_id, message_id, user_id, emoji) -> dict:
        '''https://discord.com/developers/docs/resources/channel#delete-user-reaction
            "The emoji must be URL Encoded or the request will fail with 10014: Unknown Emoji. 
            To use custom emoji, you must encode it in the format name:id with the emoji name and emoji id."
        '''
        response = self._request('DELETE', uri=f'/channels/{channel_id}/messages/{message_id}/reactions/{emoji}/{user_id}')

    def get_reactions(self, channel_id, message_id, emoji, after=None, limit: int=None) -> dict:
        '''https://discord.com/developers/docs/resources/channel#get-reactions
            "The emoji must be URL Encoded or the request will fail with 10014: Unknown Emoji. 
            To use custom emoji, you must encode it in the format name:id with the emoji name and emoji id."
        '''
        response = self._request('GET', uri=f'/channels/{channel_id}/messages/{message_id}/reactions/{emoji}')

    def delete_all_reactions(self, channel_id, message_id) -> dict:
        '''https://discord.com/developers/docs/resources/channel#delete-all-reactions'''
        response = self._request('DELETE', uri=f'/channels/{channel_id}/messages/{message_id}/reactions')
        
    def delete_all_reactions_for_emoji(self, channel_id, message_id, emoji) -> dict:
        '''https://discord.com/developers/docs/resources/channel#delete-all-reactions-for-emoji
            "The emoji must be URL Encoded or the request will fail with 10014: Unknown Emoji. 
            To use custom emoji, you must encode it in the format name:id with the emoji name and emoji id."
        '''
        response = self._request('DELETE', uri=f'/channels/{channel_id}/messages/{message_id}/reactions/{emoji}')

    def edit_message(self,
        channel_id,
        message_id, 
        content: str=None,
        embeds: [dict]=None,
        flags: int=None,
        allowed_mentions=None,
        components=list,
        files: [str]=None,
        payload_json: str=None,
        attachments: list=None,
        **kwargs
    ) -> dict:
        '''https://discord.com/developers/docs/resources/channel#edit-message'''
        payload = {
            'content': content,
            'flags': flags,
            'allowed_mentions': allowed_mentions,
            'components': components,
            'payload_json': payload_json,
            'attachments': attachments,
            'embeds': embeds
        }
        payload = {k:v for k,v in payload.items() if v is not None}
        uri = f'/channels/{channel_id}/messages/{message_id}'
        if files != None:
            return  self._send_file_attachment(method='POST', uri=uri, file_names=files, payload=payload)
        else:
            return  self._request(method='POST', uri=uri, payload=payload)

    def delete_message(self, channel_id, message_id) -> dict:
        '''https://discord.com/developers/docs/resources/channel#delete-message'''
        return  self._request('DELETE', uri=f'/channels/{channel_id}/messages/{message_id}')

    def bulk_delete_message(self, channel_id, messages: list) -> dict:
        '''https://discord.com/developers/docs/resources/channel#bulk-delete-messages'''
        paylaod = { 'messages': messages }
        return  self._request('POST', params=payload, uri=f'/channels/{channel_id}/messages/bulk-delete')

    def edit_channel_permissions(self, channel_id, overwrite_id, allow=None, deny=None, type: int=None) -> dict:
        '''https://discord.com/developers/docs/resources/channel#edit-channel-permissions'''
        payload = {
            'allow': allow,
            'deny': deny,
            'type': type
        }
        payload = {k:v for k,v in payload.items() if v is not None}
        return  self._request('PUT', params=payload, uri=f'/channels/{channel_id}/permissions/{overwrite_id}')

    def get_channel_invites(self, channel_id) -> dict:
        '''https://discord.com/developers/docs/resources/channel#get-channel-invites'''
        return  self._request('GET', uri=f'/channels/{channel_id}/invites')

    def create_channel_invite(self,
        channel_id,
        max_age: int=None,
        max_uses: int=None,
        temporary: bool=None,
        unique: bool=None,
        target_type: int=None,
        target_user_id=None,
        target_application_id=None,
    ) -> dict:
        '''https://discord.com/developers/docs/resources/channel#create-channel-invite'''
        payload = {
            'max_age': max_age,
            'max_uses': max_uses,
            'temporary': temporary,
            'unique': unique,
            'target_type': target_type,
            'target_user_id': target_user_id,
            'target_application_id': target_application_id
        }
        payload = {k:v for k,v in payload.items() if v is not None}
        return  self._request('POST', params=payload, uri=f'/channels/{channel_id}/invites')

    def delete_channel_permission(self, channel_id, overwrite_id) -> dict:
        '''https://discord.com/developers/docs/resources/channel#delete-channel-permission'''
        return  self._request('DELETE', uri=f'/channels/{channel_id}/permissions/{overwrite_id}')

    def follow_news_channel(self, channel_id, webhook_channel_id) -> dict:
        '''https://discord.com/developers/docs/resources/channel#follow-news-channel'''
        payload = { 'webhook_channel_id': webhook_channel_id }
        return  self._request('POST', params=payload, uri=f'/channels/{channel_id}/followers')

    def trigger_typing_indicatoe(self, channel_id) -> dict:
        '''https://discord.com/developers/docs/resources/channel#trigger-typing-indicator'''
        return  self._request('POST', uri=f'/channels/{channel_id}/typing')

    def get_pinned_message(self, channel_id) -> dict:
        '''https://discord.com/developers/docs/resources/channel#get-pinned-messages'''
        return  self._request('GET', uri=f'/channels/{channel_id}/pins')

    def pin_message(self, channel_id, message_id) -> dict:
        '''https://discord.com/developers/docs/resources/channel#pin-message'''
        return  self._request('PUT', uri=f'/channels/{channel_id}/pins/{message_id}')

    def unpin_message(self, channel_id,  message_id) -> dict:
        '''https://discord.com/developers/docs/resources/channel#unpin-message'''
        return  self._request('DELETE', uri=f'/channels/{channel_id}/pins/{message_id}')

    def group_dm_add_recipient(self, channel_id, user_id, access_token, nick) -> dict:
        '''https://discord.com/developers/docs/resources/channel#group-dm-add-recipient'''
        payload = {
            'access_token': access_token,
            'nick':nick
        }
        payload = {k:v for k,v in payload.items() if v is not None}
        return  self._request('PUT', params=payload, uri=f'/channels/{channel_id}/recipients/{user_id}')

    def group_dm_remove_recipient(self, channel_id, user_id) -> dict:
        '''https://discord.com/developers/docs/resources/channel#group-dm-remove-recipient'''
        return  self._request('DELETE', uri=f'/channels/{channel_id}/recipients/{user_id}')

    def start_thread_with_message(self, channel_id, user_id, name: str, auto_archive_duration: int=None, rate_limit_per_user: int=None) -> dict:
        '''https://discord.com/developers/docs/resources/channel#start-thread-with-message'''
        payload = { 
            'name': name,
            'auto_archive_duration': auto_archive_duration,
            'rate_limit_per_user': rate_limit_per_user
        }
        payload = {k:v for k,v in payload.items() if v is not None}
        return  self._request('POST', params=payload, uri=f'/channels/{channel_id}/messages/{message_id}/threads')

    def start_thread_without_message(self, 
        channel_id,
        auto_archive_duration: str=None,
        type: int=None,
        invitable: bool=None,
        rate_limit_per_user: int=None,
    ) -> dict:
        '''https://discord.com/developers/docs/resources/channel#start-thread-without-message'''
        payload = { 
            'name': name,
            'auto_archive_duration': auto_archive_duration,
            'type': type,
            'invitable': invitable,
            'rate_limit_per_user': rate_limit_per_user
        }
        payload = {k:v for k,v in payload.items() if v is not None}
        return  self._request('POST', params=payload, uri=f'/channels/{channel_id}/threads')

    def join_thread(self, channel_id) -> dict:
        '''https://discord.com/developers/docs/resources/channel#join-thread'''
        return  self._request('PUT', uri=f'/channels/{channel_id}/thread-members/@me')

    def add_thread_member(self, channel_id, user_id) -> dict:
        '''https://discord.com/developers/docs/resources/channel#add-thread-member'''
        return  self._request('PUT', uri=f'/channels/{channel_id}/thread-members/{user_id}')

    def leave_thread(self, channel_id) -> dict:
        '''https://discord.com/developers/docs/resources/channel#leave-thread'''
        return  self._request('DELETE', uri=f'/channels/{channel_id}/thread-members/@me')

    def remove_thread_member(self, channel_id, user_id) -> dict:
        '''https://discord.com/developers/docs/resources/channel#remove-thread-member'''
        return  self._request('DELETE', uri=f'/channels/{channel_id}/thread-members/{user_id}')

    def get_thread_member(self, channel_id, user_id) -> dict:
        '''https://discord.com/developers/docs/resources/channel#get-thread-member'''
        return  self._request('GET', uri=f'/channels/{channel_id}/thread-members/{user_id}')

    def list_thread_member(self, channel_id) -> dict:
        '''https://discord.com/developers/docs/resources/channel#list-thread-members'''
        return  self._request('GET', uri=f'/channels/{channel_id}/thread-members')

    def list_active_threads(self, channel_id, threads: list, members: list, has_more: bool ) -> dict:
        '''https://discord.com/developers/docs/resources/channel#list-active-threads'''
        payload = {
            'threads': threads,
            'members': members,
            'has_more': has_more
        }
        return  self._request('GET', params=payload, uri=f'/channels/{channel_id}/threads/active')

    def list_public_archived_threads(self, channel_id, before=None, limit:int=None ) -> dict:
        '''https://discord.com/developers/docs/resources/channel#list-public-archived-threads'''
        payload = { 'before': before, 'limit': limit}
        payload = {k:v for k,v in payload.items() if v is not None}
        return  self._request('GET', params=params, uri=f'/channels/{channel_id}/threads/archived/public')

    def list_private_archived_threads(self, channel_id) -> dict:
        '''https://discord.com/developers/docs/resources/channel#list-private-archived-threads'''
        payload = { 'before': before, 'limit': limit }
        payload = {k:v for k,v in payload.items() if v is not None}
        return  self._request('GET', params=payload, uri=f'/channels/{channel_id}/threads/archived/private')

    def list_joined_private_archived_threads(self, channel_id, before=None, limit:int=None) -> dict:
        '''https://discord.com/developers/docs/resources/channel#list-joined-private-archived-threads'''
        payload = { 'before': before, 'limit': limit }
        payload = {k:v for k,v in payload.items() if v is not None}
        return  self._request('GET', params=payload, uri=f'/channels/{channel_id}/users/@me/threads/archived/private')