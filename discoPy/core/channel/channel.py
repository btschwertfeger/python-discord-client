class Channel(object):
    '''Contains a collection of channel related methods.'''

    async def get_channel(self, channel_id) -> dict:
        '''https://discord.com/developers/docs/resources/channel#get-channel'''
        return await self._request('GET', uri=f'/channels/{channel_id}')

    async def modify_channel(self, 
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
        payload = {}
        if name != None:
            payload['name'] = name
        if icon != None:
            payload['icon'] = icon
        if type != None:
            payload['type'] = type
        if topic != None:
            payload['topic'] = topic
        if nsfw != None:
            payload['nsfw'] = nsfw
        if rate_limit_per_user != None:
            payload['rate_limit_per_user'] = rate_limit_per_user
        if bitrate != None:
            payload['bitrate'] = bitrate
        if user_limit != None:
            payload['user_limit'] = user_limit
        if permission_overwrites != None:
            payload['permission_overwrites'] = permission_overwrites
        if parent_id != None:
            payload['parent_id'] = parent_id
        if rtc_region != None:
            payload['rtc_region'] = rtc_region
        if video_quality_mode != None:
            payload['video_quality_mode'] = video_quality_mode
        if default_auto_archive_duration != None:
            payload['default_auto_archive_duration'] = default_auto_archive_duration
        if archived != None:
            payload['archived'] = archived
        if auto_archive_duration != None:
            payload['auto_archive_duration'] = auto_archive_duration
        if locked != None:
            payload['locked'] = locked
        if invitable != None:
            payload['invitable'] = invitable
        return await  self._request('PATCH', params=payload, uri=f'/channels/{await self._get_channel_id(kwargs)}')
        
    async def delete_close_channel(self, **kwargs) -> dict:
        '''https://discord.com/developers/docs/resources/channel#deleteclose-channel'''
        return await  self._request('DELETE', uri=f'/channels/{await self._get_channel_id(kwargs)}')

    async def get_channel_messages(self,
        around=None,
        before=None,
        after=None,
        limit: int=None,
        **kwargs
    ) -> dict:
        '''https://discord.com/developers/docs/resources/channel#get-channel-messages'''
        params = {}
        if around != None:
            params['around'] = around
        if before != None:
            params['before'] = beforde
        if after != None:
            params['after'] = after
        if limit != None:
            params['limit'] = limit
        return await  self._request('GET', params=params, uri=f'/channels/{await self._get_channel_id(kwargs)}/messages')

    async def get_channel_message(self, **kwargs) -> dict:
        '''https://discord.com/developers/docs/resources/channel#get-channel-message'''
        return await  self._request('GET',uri=f'/channels/{await self._get_channel_id(kwargs)}/messages')

    async def create_message(self,
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
        **kwargs
    ) -> dict:
        '''https://discord.com/developers/docs/resources/channel#create-message'''

        payload = {}
        if content != None:
            payload['content'] = content
        if tts != None:
            payload['tts'] = tts
        if allowed_mentions != None:
            payload['allowed_mentions'] = allowed_mentions
        if message_reference != None:
            payload['message_reference'] = message_reference
        if components != None:
            payload['components'] = components
        if sticker_ids != None:
            payload['sticker_ids'] = sticker_ids
        if flags != None:
            payload['flags'] = flags
        if embeds != None:
            payload['embeds'] = embeds
        if attachments != None:
            payload['attachments'] = attachments
        
        uri = f'/channels/{await self._get_channel_id(kwargs)}/messages'
        if files != None:
            return await  self._send_file_attachment(method='POST', uri=uri, file_names=files, payload=payload)
        else:
            return await  self._request(method='POST', uri=uri, params=payload)

    async def crosspost_message(self, message_id, **kwargs) -> dict:
        '''https://discord.com/developers/docs/resources/channel#crosspost-message'''
        response = self._request('POST', uri=f'/channels/{await self._get_channel_id(kwargs)}/messages/{message_id}/crosspost')

    async def create_reaction(self, message_id, emoji, **kwargs) -> dict:
        '''https://discord.com/developers/docs/resources/channel#create-reaction
            "The emoji must be URL Encoded or the request will fail with 10014: Unknown Emoji. 
            To use custom emoji, you must encode it in the format name:id with the emoji name and emoji id."
        '''
        response = self._request('PUT', uri=f'/channels/{await self._get_channel_id(kwargs)}/messages/{message_id}/reactions/{emoji}/@me')

    async def delete_own_reaction(self,  message_id, emoji, **kwargs) -> dict:
        '''https://discord.com/developers/docs/resources/channel#delete-own-reaction
            "The emoji must be URL Encoded or the request will fail with 10014: Unknown Emoji. 
            To use custom emoji, you must encode it in the format name:id with the emoji name and emoji id."
        '''
        response = self._request('DELETE', uri=f'/channels/{await self._get_channel_id(kwargs)}/messages/{message_id}/reactions/{emoji}/@me')

    async def delete_user_reaction(self, message_id, user_id, emoji, **kwargs) -> dict:
        '''https://discord.com/developers/docs/resources/channel#delete-user-reaction
            "The emoji must be URL Encoded or the request will fail with 10014: Unknown Emoji. 
            To use custom emoji, you must encode it in the format name:id with the emoji name and emoji id."
        '''
        response = self._request('DELETE', uri=f'/channels/{await self._get_channel_id(kwargs)}/messages/{message_id}/reactions/{emoji}/{user_id}')

    async def get_reactions(self, message_id, emoji, after=None, limit: int=None, **kwargs) -> dict:
        '''https://discord.com/developers/docs/resources/channel#get-reactions
            "The emoji must be URL Encoded or the request will fail with 10014: Unknown Emoji. 
            To use custom emoji, you must encode it in the format name:id with the emoji name and emoji id."
        '''
        response = self._request('GET', uri=f'/channels/{await self._get_channel_id(kwargs)}/messages/{message_id}/reactions/{emoji}')

    async def delete_all_reactions(self, message_id, **kwargs) -> dict:
        '''https://discord.com/developers/docs/resources/channel#delete-all-reactions'''
        response = self._request('DELETE', uri=f'/channels/{await self._get_channel_id(kwargs)}/messages/{message_id}/reactions')
        
    async def delete_all_reactions_for_emoji(self, message_id, emoji, **kwargs) -> dict:
        '''https://discord.com/developers/docs/resources/channel#delete-all-reactions-for-emoji
            "The emoji must be URL Encoded or the request will fail with 10014: Unknown Emoji. 
            To use custom emoji, you must encode it in the format name:id with the emoji name and emoji id."
        '''
        response = self._request('DELETE', uri=f'/channels/{await self._get_channel_id(kwargs)}/messages/{message_id}/reactions/{emoji}')

    async def edit_message(self,
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
        payload = {}
        if content != None:
            payload['content'] = content
        if flags != None:
            payload['flags'] = flags
        if allowed_mentions != None:
            payload['allowed_mentions'] = allowed_mentions
        if components != None:
            payload['components'] = components
        if payload_json != None:
            payload['payload_json'] = payload_json
        if attachments != None:
            payload['attachments'] = attachments
        if embeds != None:
            payload['embeds'] = embeds

        uri = f'/channels/{await self._get_channel_id(kwargs)}/messages/{message_id}'
        if files != None:
            return await  self._send_file_attachment(method='POST', uri=uri, file_names=files, payload=payload)
        else:
            return await  self._request(method='POST', uri=uri, payload=payload)

    async def delete_message(self, message_id, **kwargs) -> dict:
        '''https://discord.com/developers/docs/resources/channel#delete-message'''
        return await  self._request('DELETE', uri=f'/channels/{await self._get_channel_id(kwargs)}/messages/{message_id}')

    async def bulk_delete_message(self, messages: list, **kwargs) -> dict:
        '''https://discord.com/developers/docs/resources/channel#bulk-delete-messages'''
        paylaod = { 'messages': messages }
        return await  self._request('POST', params=payload, uri=f'/channels/{await self._get_channel_id(kwargs)}/messages/bulk-delete')

    async def edit_channel_permissions(self,overwrite_id, allow=None, deny=None, type: int=None, **kwargs) -> dict:
        '''https://discord.com/developers/docs/resources/channel#edit-channel-permissions'''
        payload = {}
        if allow != None:
            payload['allow'] = allow
        if deny != None:
            payload['deny'] = deny
        if type != None:
            payload['type'] = type
        return await  self._request('PUT', params=payload, uri=f'/channels/{await self._get_channel_id(kwargs)}/permissions/{overwrite_id}')

    async def get_channel_invites(self, **kwargs) -> dict:
        '''https://discord.com/developers/docs/resources/channel#get-channel-invites'''
        return await  self._request('GET', uri=f'/channels/{await self._get_channel_id(kwargs)}/invites')

    async def create_channel_invite(self,
        max_age: int=None,
        max_uses: int=None,
        temporary: bool=None,
        unique: bool=None,
        target_type: int=None,
        target_user_id=None,
        target_application_id=None,
        **kwargs
    ) -> dict:
        '''https://discord.com/developers/docs/resources/channel#create-channel-invite'''
        payload = {}
        if max_age != None:
            payload['max_age'] = max_age
        if max_uses != None:
            payload['max_uses'] = max_uses
        if temporary != None:
            payload['temporary'] = temporary
        if unique != None:
            payload['unique'] = unique
        if target_type != None:
            payload['target_type'] = target_type
        if target_user_id != None:
            payload['target_user_id'] = target_user_id
        if target_application_id != None:
            payload['target_application_id'] = target_application_id
        return await  self._request('POST', params=payload, uri=f'/channels/{await self._get_channel_id(kwargs)}/invites')

    async def delete_channel_permission(self, overwrite_id, **kwargs) -> dict:
        '''https://discord.com/developers/docs/resources/channel#delete-channel-permission'''
        return await  self._request('DELETE', uri=f'/channels/{await self._get_channel_id(kwargs)}/permissions/{overwrite_id}')

    async def follow_news_channel(self, webhook_channel_id, **kwargs) -> dict:
        '''https://discord.com/developers/docs/resources/channel#follow-news-channel'''
        payload = { 'webhook_channel_id': webhook_channel_id }
        return await  self._request('POST', params=payload, uri=f'/channels/{await self._get_channel_id(kwargs)}/followers')

    async def trigger_typing_indicatoe(self, **kwargs) -> dict:
        '''https://discord.com/developers/docs/resources/channel#trigger-typing-indicator'''
        return await  self._request('POST', uri=f'/channels/{await self._get_channel_id(kwargs)}/typing')

    async def get_pinned_message(self, **kwargs) -> dict:
        '''https://discord.com/developers/docs/resources/channel#get-pinned-messages'''
        return await  self._request('GET', uri=f'/channels/{await self._get_channel_id(kwargs)}/pins')

    async def pin_message(self, message_id, **kwargs) -> dict:
        '''https://discord.com/developers/docs/resources/channel#pin-message'''
        return await  self._request('PUT', uri=f'/channels/{await self._get_channel_id(kwargs)}/pins/{message_id}')

    async def unpin_message(self, message_id, **kwargs) -> dict:
        '''https://discord.com/developers/docs/resources/channel#unpin-message'''
        return await  self._request('DELETE', uri=f'/channels/{await self._get_channel_id(kwargs)}/pins/{message_id}')

    async def group_dm_add_recipient(self, user_id, access_token, nick, **kwargs) -> dict:
        '''https://discord.com/developers/docs/resources/channel#group-dm-add-recipient'''
        payload = {
            'access_token': access_token,
            'nick':nick
        }
        return await  self._request('PUT', params=payload, uri=f'/channels/{await self._get_channel_id(kwargs)}/recipients/{user_id}')

    async def group_dm_remove_recipient(self, user_i, **kwargsd) -> dict:
        '''https://discord.com/developers/docs/resources/channel#group-dm-remove-recipient'''
        return await  self._request('DELETE', uri=f'/channels/{await self._get_channel_id(kwargs)}/recipients/{user_id}')

    async def start_thread_with_message(self, user_id, name: str, auto_archive_duration: int=None, rate_limit_per_user: int=None, **kwargs) -> dict:
        '''https://discord.com/developers/docs/resources/channel#start-thread-with-message'''
        payload = { 'name': name }
        if auto_archive_duration != None:
            payload['auto_archive_duration'] = auto_archive_duration
        if rate_limit_per_user != None:
            payload['rate_limit_per_user'] = rate_limit_per_user
        return await  self._request('POST', params=payload, uri=f'/channels/{await self._get_channel_id(kwargs)}/messages/{message_id}/threads')

    async def start_thread_without_message(self, 
        auto_archive_duration: str=None,
        type: int=None,
        invitable: bool=None,
        rate_limit_per_user: int=None,
        **kwargs
    ) -> dict:
        '''https://discord.com/developers/docs/resources/channel#start-thread-without-message'''
        payload = { 'name': name }
        if auto_archive_duration != None:
            payload['auto_archive_duration'] = auto_archive_duration
        if type != None:
            payload['type'] = type
        if invitable != None:
            payload['invitable'] = invitable
        if rate_limit_per_user != None:
            payload['rate_limit_per_user'] = rate_limit_per_user
        return await  self._request('POST', params=payload, uri=f'/channels/{await self._get_channel_id(kwargs)}/threads')

    async def join_thread(self, **kwargs) -> dict:
        '''https://discord.com/developers/docs/resources/channel#join-thread'''
        return await  self._request('PUT', uri=f'/channels/{await self._get_channel_id(kwargs)}/thread-members/@me')

    async def add_thread_member(self, user_id, **kwargs) -> dict:
        '''https://discord.com/developers/docs/resources/channel#add-thread-member'''
        return await  self._request('PUT', uri=f'/channels/{await self._get_channel_id(kwargs)}/thread-members/{user_id}')

    async def leave_thread(self, **kwargs) -> dict:
        '''https://discord.com/developers/docs/resources/channel#leave-thread'''
        return await  self._request('DELETE', uri=f'/channels/{await self._get_channel_id(kwargs)}/thread-members/@me')

    async def remove_thread_member(self, user_id, **kwargs) -> dict:
        '''https://discord.com/developers/docs/resources/channel#remove-thread-member'''
        return await  self._request('DELETE', uri=f'/channels/{await self._get_channel_id(kwargs)}/thread-members/{user_id}')

    async def get_thread_member(self, user_id, **kwargs) -> dict:
        '''https://discord.com/developers/docs/resources/channel#get-thread-member'''
        return await  self._request('GET', uri=f'/channels/{await self._get_channel_id(kwargs)}/thread-members/{user_id}')

    async def list_thread_member(self, **kwargs) -> dict:
        '''https://discord.com/developers/docs/resources/channel#list-thread-members'''
        return await  self._request('GET', uri=f'/channels/{await self._get_channel_id(kwargs)}/thread-members')

    async def list_active_threads(self,  threads: list, members: list, has_more: bool, **kwargs ) -> dict:
        '''https://discord.com/developers/docs/resources/channel#list-active-threads'''
        params = {
            'threads': threads,
            'members': members,
            'has_more': has_more
        }
        return await  self._request('GET', params=params, uri=f'/channels/{await self._get_channel_id(kwargs)}/threads/active')

    async def list_public_archived_threads(self, before=None, limit:int=None, **kwargs ) -> dict:
        '''https://discord.com/developers/docs/resources/channel#list-public-archived-threads'''
        params = {}
        if before != None:
            params['before'] = before
        if limit != None:
            params['limit'] = limit
        return await  self._request('GET', params=params, uri=f'/channels/{await self._get_channel_id(kwargs)}/threads/archived/public')

    async def list_private_archived_threads(self, **kwargs) -> dict:
        '''https://discord.com/developers/docs/resources/channel#list-private-archived-threads'''
        params = {}
        if before != None:
            params['before'] = before
        if limit != None:
            params['limit'] = limit
        return await  self._request('GET', params=params, uri=f'/channels/{await self._get_channel_id(kwargs)}/threads/archived/private')

    async def list_joined_private_archived_threads(self, before=None, limit:int=None, **kwargs) -> dict:
        '''https://discord.com/developers/docs/resources/channel#list-joined-private-archived-threads'''
        params = {}
        if before != None:
            params['before'] = before
        if limit != None:
            params['limit'] = limit
        return await  self._request('GET', params=params, uri=f'/channels/{await self._get_channel_id(kwargs)}/users/@me/threads/archived/private')

    async def _get_channel_id(self, kwargs) -> str:
        try:
            channel_id = kwargs.get('channel_id', None)
            return  channel_id if channel_id != None else self.data['id']
        except:
            raise ValueError('channel_id not defined!')