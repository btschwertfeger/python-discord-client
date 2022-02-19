class Guild(object):
    '''Contains a collection of guild/server related methods.'''
    
    # -----======= G E N E R A L =======-----
    async def create_guild(self, 
        name: str, 
        region: str=None, 
        icon=None, 
        verification_level: int=None, 
        default_message_notifications: int=None, 
        explicit_content_filter: int=None, 
        roles: list=None, 
        channels: list=None, 
        afk_channel_id: str=None, 
        afk_timeout: int=None, 
        system_channel_id: str=None, 
        system_channel_flags: int=None
    ) -> dict:
        '''https://discord.com/developers/docs/resources/guild#create-guild'''
        payload = { 
            'name': name,
            'region': region,
            'icon': icon,
            'verification_level': verification_level,
            'default_message_notifications': default_message_notifications,
            'explicit_content_filter': explicit_content_filter,
            'roles': roles,
            'channels': channels,
            'afk_channel_id': afk_channel_id,
            'afk_timeout': afk_timeout,
            'system_channel_id': system_channel_id,
            'system_channel_flags': system_channel_flags
        }
        payload = {k:v for k,v in payload.items() if v is not None}
        return await self._request('POST', params=payload, uri='/guilds')

    async def get_guild(self, guild_id, with_counts: bool=False) -> dict:
        '''https://discord.com/developers/docs/resources/guild#get-guild'''
        payload = { 'width_couunts': with_counts }
        return await self._request('GET', params=payload, uri=f'/guilds/{guild_id}')

    async def get_guild_preview(self, guild_id) -> dict:
        '''https://discord.com/developers/docs/resources/guild#get-guild-preview'''
        return await self._request(method='GET', uri=f'/guilds/{guild_id}/preview')

    async def modify_guild(self,
        guild_id,
        name: str,
        region: str=None,
        verification_level: int=None,
        default_message_notifications: int=None,
        explicit_content_filter: int=None,
        afk_channel_id: str=None,
        afk_timeout: int=None,
        icon=None, 
        owner_id=None,
        splash=None,
        discovery_splash=None,
        banner=None,
        system_channel_id=None,
        system_channel_flags: int=None,rules_channel_id=None,
        public_updates_channel_id=None,
        preferred_locale: str=None,
        features: list=None,
        description: str=None,premium_progress_bar_enabled: bool=None
    ) -> dict:
        '''https://discord.com/developers/docs/resources/guild#modify-guild'''
        payload = {
            'name': name,
            'region': region,
            'verification_level': verification_level,
            'default_message_notifications': default_message_notifications,
            'explicit_content_filter': explicit_content_filter,
            'afk_channel_id': afk_channel_id,
            'afk_timeout': afk_timeout,
            'icon': icon,
            'owner_id': owner_id,
            'splash': splash,
            'discovery_splash': discovery_splash,
            'banner': banner,
            'system_channel_id': system_channel_id,
            'system_channel_flags': system_channel_flags,
            'public_updates_channel_id': public_updates_channel_id,
            'preferred_locale': preferred_locale,
            'features': features,
            'description': description
        }
        payload = {k:v for k,v in payload.items() if v is not None}
        return await self._request(method='POST', params=payload, uri=f'/guilds/{guild_id}')

    async def delete_guild(self, guild_id) -> dict:
        '''https://discord.com/developers/docs/resources/guild#delete-guild'''
        return await self._request(method='DELETE', uri=f'/guilds/{guild_id}')

    async def get_guild_channels(self, guild_id) -> dict:
        '''https://discord.com/developers/docs/resources/guild#get-guild-channels'''
        return await self._request(method='GET', uri=f'/guilds/{guild_id}/channels')

    async def create_guild_channel(self, 
        guild_id,
        name: str,
        type: int,
        topic: str,
        bitrate: int,
        user_limit: int,
        rate_limit_per_user: int,
        position: int,
        permission_overwrites: list,
        parent_id,
        nsfw: bool
    ) -> dict:
        '''https://discord.com/developers/docs/resources/guild#create-guild-channel'''
        payload = {
            'guild_id': guild_id,
            'name': name,
            'type': type,
            'topic': topic,
            'bitrate': bitrate,
            'user_limit': user_limit,
            'rate_limit_per_user': rate_limit_per_user,
            'position': position,
            'permission_overwrites': permission_overwrites,
            'parent_id': parent_id,
            'nsfw': nsfw
        }
        payload = {k:v for k,v in payload.items() if v is not None}
        return await self._request(method='POST', params=payload, uri=f'/guilds/{guild_id}/channels')

    async def modify_channel_positions(self, 
        guild_id, id, position: int=None, lock_permissions: bool=None, parent_id=None
    ) -> dict:
        '''https://discord.com/developers/docs/resources/guild#modify-guild-channel-positions'''
        payload = {
            'id': id,
            'position': position,
            'lock_permissions': lock_permissions,
            'parent_id': parent_id
        }
        payload = {k:v for k,v in payload.items() if v is not None}
        return await self._request(method='PATCH', params=payload, uri=f'/guilds/{guild_id}/channels')

    async def list_active_threads(self, guild_id) -> dict:
        '''https://discord.com/developers/docs/resources/guild#list-active-threads'''
        return await self._request(method='GET', uri=f'/guilds/{guild_id}/threads/active')

    async def get_guild_member(self, guild_id, user_id) -> dict:
        '''https://discord.com/developers/docs/resources/guild#get-guild-member'''
        return await self._request(method='GET', uri=f'/guilds/{guild_id}/members/{user_id}')

    async def list_guild_members(self, guild_id, limit: int, after) -> dict:
        '''https://discord.com/developers/docs/resources/guild#list-guild-members'''
        payload = { 'limit': limit, 'after': after}
        payload = {k:v for k,v in payload.items() if v is not None}
        return await self._request(method='GET', params=params, uri=f'/guilds/{guild_id}/members')

    async def search_guild_members(self, guild_id, query: str, limit:int=None) -> dict:
        '''https://discord.com/developers/docs/resources/guild#search-guild-members'''
        payload = { 'query': query, 'limit': limit }
        payload = {k:v for k,v in payload.items() if v is not None}
        return await self._request(method='GET', params=params, uri=f'/guilds/{guild_id}/members/search')

    async def add_guild_member(self, guild_id, user_id, access_token: str, nick: str, roles: list, mute: bool, deaf: bool) -> dict:
        '''https://discord.com/developers/docs/resources/guild#add-guild-member'''
        payload = {
            'access_token': access_token,
            'nick': nick,
            'roles': roles,
            'mute': mute,
            'deaf': deaf
        }

        payload = {k:v for k,v in payload.items() if v is not None}
        return await self._request(method='PUT', params=payload, uri=f'/guilds/{guild_id}/members/{user_id}')

    async def modify_current_member(self, guild_id, nick: str=None) -> dict:
        '''https://discord.com/developers/docs/resources/guild#modify-current-member'''
        payload = { 'nick': nick }
        payload = {k:v for k,v in payload.items() if v is not None}
        return await self._request(method='PATCH', params=payload, uri=f'/guilds/{guild_id}/members/@me')

    async def add_guild_member_role(self, guild_id, user_id, role_id) -> dict:
        '''https://discord.com/developers/docs/resources/guild#add-guild-member-role'''
        return await self._request(method='PUT', uri=f'/guilds/{guild_id}/members/{user_id}/roles/{role_id}')

    async def remove_guild_member_role(self, guild_id, user_id, role_id) -> dict:
        '''https://discord.com/developers/docs/resources/guild#remove-guild-member-role'''
        return await self._request(method='DELETE', uri=f'/guilds/{guild_id}/members/{user_id}/roles/{role_id}')

    async def remove_guild_member(self, guild_id, user_id) -> dict:
        '''https://discord.com/developers/docs/resources/guild#remove-guild-member'''
        return await self._request(method='DELETE', uri=f'/guilds/{guild_id}/members/{user_id}')

    async def get_guild_bans(self, guild_id) -> dict:
        '''https://discord.com/developers/docs/resources/guild#get-guild-bans'''
        return await self._request(method='GET', uri=f'/guilds/{guild_id}/bans')

    async def get_guild_ban(self, guild_id, user_id) -> dict:
        '''https://discord.com/developers/docs/resources/guild#get-guild-ban'''
        return await self._request(method='GET', uri=f'/guilds/{guild_id}/bans/{user_id}')

    async def create_guild_ban(self, guild_id, user_id, delete_message_days: int=None, reason: str=None) -> dict:
        '''https://discord.com/developers/docs/resources/guild#create-guild-ban'''
        payload = { 'delete_message_days':delete_message_days, 'reason': reason }
        payload = {k:v for k,v in payload.items() if v is not None}
        return await self._request(method='PUT', params=params, uri=f'/guilds/{guild_id}/bans/{user_id}')

    async def remove_guild_ban(self, guild_id, user_id) -> dict:
        '''https://discord.com/developers/docs/resources/guild#remove-guild-ban'''
        return await self._request(method='DELETE', uri=f'/guilds/{guild_id}/bans/{user_id}')

    async def get_guild_roles(self, guild_id) -> dict:
        '''https://discord.com/developers/docs/resources/guild#get-guild-roles'''
        return await self._request(method='GET', uri=f'/guilds/{guild_id}/roles')

    async def create_guild_role(self, 
        guild_id, name: str, permissions: str, 
        color: int=0, hoist: bool=False, icon=None, unicode_emoji: str=None, 
        mentionable: bool=False
    ) -> dict:
        '''https://discord.com/developers/docs/resources/guild#create-guild-role'''
        payload = {
            'name': name,
            'permissions': permissions,
            'color': color,
            'hoist':hoist,
            'icon': icon,
            'unicode_emoji': unicode_emoji,
            'mentionable': mentionable
        }

        payload = {k:v for k,v in payload.items() if v is not None}
        return await self._request(method='POST', params=payload, uri=f'/guilds/{guild_id}/roles')

    async def modify_guild_role_permissions(self, guild_id, id, position: int=None) -> dict:
        '''https://discord.com/developers/docs/resources/guild#modify-guild-role-positions'''
        payload = { 'id': id, 'position': position }
        payload = {k:v for k,v in payload.items() if v is not None}
        return await self._request(method='PATCH', params=payload, uri=f'/guilds/{guild_id}/roles')

    async def modify_guild_role(self, 
        guild_id, role_id, name: str=None, permission: str=None, 
        color: int=None, hoist: bool=None, icon=None, unicode_emoji: str=None, mentionable: bool=None
    ) -> dict:
        '''https://discord.com/developers/docs/resources/guild#modify-guild-role'''
        payload = {
            'name': name,
            'permission': permission,
            'color': color,
            'hoist': hoist,
            'icon': icon,
            'unicode_emoji': unicode_emoji,
            'mentionable': mentionable
        }
        payload = {k:v for k,v in payload.items() if v is not None}
        return await self._request(method='PATCH', params=payload, uri=f'/guilds/{guild_id}/roles/{role_id}')

    async def delete_guild_role(self, guild_id, role_id) -> dict:
        '''https://discord.com/developers/docs/resources/guild#delete-guild-role'''
        return await self._request(method='DELETE', uri=f'/guilds/{guild_id}/roles/{role_id}')

    async def get_guild_prune_count(self, guild_id, days: int=7, include_roles: str=None) -> dict:
        '''https://discord.com/developers/docs/resources/guild#get-guild-prune-count'''
        payload = { 'days': days, 'include_roles': include_roles }
        payload = {k:v for k,v in payload.items() if v is not None}
        return await self._request(method='GET', params=params, uri=f'/guilds/{guild_id}/prune')

    async def beginn_guild_prune(self, guild_id, days: int, compute_prune_count: bool, include_roles: str, reason: str=None) -> dict:
        '''https://discord.com/developers/docs/resources/guild#begin-guild-prune'''
        payload = {
            'days': days,
            'compute_prune_count': compute_prune_count,
            'include_roles': include_roles,
            'reason': reason
        }
        payload = {k:v for k,v in payload.items() if v is not None}
        return await self._request(method='POST', params=payload, uri=f'/guilds/{guild_id}/prune')

    async def get_guild_voice_regions(self, guild_id) -> dict:
        '''https://discord.com/developers/docs/resources/guild#get-guild-voice-regions'''
        return await self._request(method='GET', uri=f'/guilds/{guild_id}/regions')

    async def get_guild_invites(self, guild_id) -> dict:
        '''https://discord.com/developers/docs/resources/guild#get-guild-invites'''
        return await self._request(method='GET', uri=f'/guilds/{guild_id}/invites')

    async def get_guild_integrations(self, guild_id) -> dict:
        '''https://discord.com/developers/docs/resources/guild#get-guild-integrations'''
        return await self._request(method='GET', uri=f'/guilds/{guild_id}/integrations')

    async def delete_guild_integrations(self, guild_id, integration_id) -> dict:
        '''https://discord.com/developers/docs/resources/guild#delete-guild-integration'''
        return await self._request(method='DELETE', uri=f'/guilds/{guild_id}/integrations/{integration_id}')

    async def get_guild_widget_settings(self, guild_id) -> dict:
        '''https://discord.com/developers/docs/resources/guild#get-guild-widget-settings'''
        return await self._request(method='DELETE', uri=f'/guilds/{guild_id}/widget')

    async def modify_guild_widget(self, guild_id, settings: dict) -> dict:
        '''https://discord.com/developers/docs/resources/guild#modify-guild-widget'''
        return await self._request(method='PATCH', params=settings, uri=f'/guilds/{guild_id}/widget')

    async def get_guild_widget(self, guild_id) -> dict:
        '''https://discord.com/developers/docs/resources/guild#get-guild-widget'''
        return await self._request(method='GET', uri=f'/guilds/{guild_id}/widget.json')

    async def get_guild_vanity_url(self, guild_id) -> dict:
        '''https://discord.com/developers/docs/resources/guild#get-guild-vanity-url'''
        return await self._request(method='GET', uri=f'/guilds/{guild_id}/vanity-url')

    async def get_guild_widget_image(self, guild_id, style: str) -> dict:
        '''https://discord.com/developers/docs/resources/guild#get-guild-widget-image
        @param style can be one of : [shield, banner1, banner2, banner3, banner4]
        '''
        payload = { 'style': style }
        return await self._request(method='GET', params=params, uri=f'/guilds/{guild_id}/widget.png')

    async def get_guild_welcome_screen(self, guild_id) -> dict:
        '''https://discord.com/developers/docs/resources/guild#get-guild-welcome-screen'''
        return await self._request(method='GET', params=params, uri=f'/guilds/{guild_id}/welcome-screen')

    async def modify_guild_welcome_screen(self, guild_id, enabled: bool=None, welcome_channels: list=None, description: str=None) -> dict:
        '''https://discord.com/developers/docs/resources/guild#modify-guild-welcome-screen'''
        payload = {
            'enabled': enabled,
            'welcome_channels': welcome_channels,
            'description': description
        }
        payload = {k:v for k,v in payload.items() if v is not None}
        return await self._request(method='PATCH', params=params, uri=f'/guilds/{guild_id}/welcome-screen')

    async def modify_current_user_voice_state(self, guild_id, channel_id, suppress: bool=None, request_to_speak_timestamp=None) -> dict:
        '''https://discord.com/developers/docs/resources/guild#modify-current-user-voice-state'''
        payload = { 
            'channel_id': channel_id, 
            'suppress': suppress,
            'request_to_speak_timestamp': request_to_speak_timestamp
        }
        payload = {k:v for k,v in payload.items() if v is not None}
        return await self._request(method='PATCH', params=params, uri=f'/guilds/{guild_id}/voice-states/@me')
    
    async def modify_user_voice_state(self, guild_id, user_id, channel_id, suppress: bool=None) -> dict:
        '''https://discord.com/developers/docs/resources/guild#modify-user-voice-state'''
        payload = { 'channel_id': channel_id, 'suppress': suppress }
        payload = {k:v for k,v in payload.items() if v is not None}
        return await self._request(method='PATCH', params=params, uri=f'/guilds/{guild_id}/voice-states/{user_id}e')

    async def get_guild_audit_log(self, guild_id, user_id, action_type:int, before=None, limit: int=50) -> dict:
        '''https://discord.com/developers/docs/resources/audit-log#get-guild-audit-log'''
        payload = {
            'user_id': user_id,
            'action_type': action_type,
            'before': before,
            'limit': limit
        }
        payload = {k:v for k,v in payload.items() if v is not None}
        return await self._request('GET', params=params, uri=f'/guilds/{guild_id}/audit-logs')

    # -----======= S H E D U L E D - E V E N T S =======-----
    async def list_scheduled_events_for_guild(self, guild_id, with_user_count:bool=None) -> dict:
        '''https://discord.com/developers/docs/resources/guild-scheduled-event#list-scheduled-events-for-guild'''
        payload = {'with_user_count': with_user_count}
        payload = {k:v for k,v in payload.items() if v is not None}
        return await self._request('GET', params=params, uri=f'/guilds/{guild_id}/scheduled-events')

    async def create_guild_scheduled_event(self, 
        guild_id,
        name: str,
        entity_type,
        privacy_level,
        scheduled_start_time,
        scheduled_end_time,
        channel_id=None,
        entity_metadata=None,
        description: str=None,
        image=None
    ) -> dict:
        '''https://discord.com/developers/docs/resources/guild-scheduled-event#create-guild-scheduled-event'''
        payload = {
            'name': name,
            'entity_type': entity_type,
            'privacy_level': privacy_level,
            'scheduled_start_time': scheduled_start_time,
            'scheduled_end_time': scheduled_end_time,
            'channel_id': channel_id,
            'entity_metadata': entity_metadata,
            'description': description,
            'image': image
        }        
        payload = {k:v for k,v in payload.items() if v is not None}
        return await self._request('POST', params=payload, uri=f'/guilds/{guild_id}/scheduled-events')

    async def get_guild_scheduled_event(self, guild_id, guild_scheduled_event_id, with_user_count: bool=None) -> dict:
        '''https://discord.com/developers/docs/resources/guild-scheduled-event#get-guild-scheduled-event'''
        payload = { 'with_user_count': with_user_count}
        payload = {k:v for k,v in payload.items() if v is not None}
        return await self._request('GET', params=params, uri=f'/guilds/{guild_id}/scheduled-events/{guild_scheduled_event_id}')

    async def modify_guild_scheduled_event(self, 
        guild_id, 
        guild_scheduled_event_id,
        channel_id=None,
        entity_metadata=None,
        name: str=None,
        privacy_level=None,
        scheduled_start_time=None,
        scheduled_end_time=None,
        description: str=None,
        entity_type=None,
        status=None,
        image=None
    ) -> dict:
        '''https://discord.com/developers/docs/resources/guild-scheduled-event#modify-guild-scheduled-event'''
        payload = {
            'channel_id': channel_id,
            'entity_metadata': entity_metadata,
            'name': name,
            'privacy_level': privacy_level,
            'scheduled_start_time': scheduled_start_time,
            'scheduled_end_time': scheduled_end_time,
            'description': description,
            'entity_type': entity_type,
            'status': status,
            'image': image
        }
        payload = {k:v for k,v in payload.items() if v is not None}
        return await self._request('PATCH', params=payload, uri=f'/guilds/{guild_id}/scheduled-events/{guild_scheduled_event_id}')

    async def delete_guild_scheduled_evend(self, guild_id, guild_scheduled_event_id) -> dict:
        '''https://discord.com/developers/docs/resources/guild-scheduled-event#delete-guild-scheduled-event'''
        return await self._request('DELETE', uri=f'/guilds/{guild_id}/scheduled-events/{guild_scheduled_event_id}')

    async def get_guild_scheduled_event_users(self, 
        guild_id, 
        guild_scheduled_event_id,
        limit: int=None,
        with_member: bool=None,
        before=None,
        after=None
    ) -> dict:
        '''https://discord.com/developers/docs/resources/guild-scheduled-event#get-guild-scheduled-event-users'''
        payload = {
            'limit': limit,
            'with_member': with_member,
            'before': before,
            'after': after
        }
        payload = {k:v for k,v in payload.items() if v is not None}
        return await self._request('GET', params=params, uri=f'/guilds/{guild_id}/scheduled-events/{guild_scheduled_event_id}/users')

    # -----======= T E M P L A T E S =======-----
    async def get_guild_template(self, template_code) -> dict:
        '''https://discord.com/developers/docs/resources/guild-template#get-guild-template'''
        return await self._request('GET', uri=f'/guilds/templates/{template_code}')

    async def create_guild_template(self, template_code, name: str, icon=None) -> dict:
        '''https://discord.com/developers/docs/resources/guild-template#create-guild-from-guild-template'''
        return await self._request('POST', uri=f'/guilds/templates/{template_code}')

    async def get_guild_templates(self, guild_id) -> dict:
        '''https://discord.com/developers/docs/resources/guild-template#get-guild-templates'''
        return await self._request('GET', uri=f'/guilds/{guild_id}/templates')

    async def create_guild_template(self, guild_id, name: str, description: str=None) -> dict:
        '''https://discord.com/developers/docs/resources/guild-template#create-guild-template'''
        payload = { 'name': name, 'description': description}
        payload = {k:v for k,v in payload.items() if v is not None}
        return await self._request('POST', params=payload, uri=f'/guilds/{guild_id}/templates')

    async def sync_guild_template(self, guild_id, template_code) -> dict:
        '''https://discord.com/developers/docs/resources/guild-template#sync-guild-template'''
        return await self._request('PUT',  uri=f'/guilds/{guild_id}/templates/{template_code}')

    async def modify_guild_template(self, template_code, name: str=None, description: str=None) -> dict:
        '''https://discord.com/developers/docs/resources/guild-template#modify-guild-template'''
        payload = { 'name': name, 'description': description}
        payload = {k:v for k,v in payload.items() if v is not None}
        return await self._request('PATCH', params=payload, uri=f'/guilds/{guild_id}/templates/{template_code}')

    async def delete_guild_template(self, guild_id, template_code) -> dict:
        '''https://discord.com/developers/docs/resources/guild-template#delete-guild-template'''
        return await self._request('DELETE', uri=f'/guilds/{guild_id}/templates/{template_code}')

    # -----======= E M O J I =======-----
    async def list_guild_emojis(self, guild_id) -> dict:
        '''https://discord.com/developers/docs/resources/emoji#list-guild-emojis'''
        return await self._request('GET', uri=f'/guilds/{guild_id}/emojis')
        
    async def get_guild_emoji(self, guild_id, emoji_id) -> dict:
        '''https://discord.com/developers/docs/resources/emoji#get-guild-emoji'''
        return await self._request('GET', uri=f'/guilds/{guild_id}/emojis/{emoji_id}')

    async def create_guild_emoji(self, guild_id, name: str, image, roles: list) -> dict:
        '''https://discord.com/developers/docs/resources/emoji#create-guild-emoji'''
        payload = {
            'name': name,
            'image': image,
            'roles': roles
        }
        return await self._request('POST', params=payload, uri=f'/guilds/{guild_id}/emojis')

    async def modify_guild_emoji(self, guild_id, emoji_id, name: str=None, roles: list=None) -> dict:
        '''https://discord.com/developers/docs/resources/emoji#modify-guild-emoji'''
        payload = {'name': name, 'roles': roles}
        payload = {k:v for k,v in payload.items() if v is not None}
        return await self._request('PATCH', params=payload, uri=f'/guilds/{guild_id}/emojis/{emoji_id}')

    async def delete_guild_emoji(self, guild_id, emoji_id) -> dict:
        '''https://discord.com/developers/docs/resources/emoji#delete-guild-emoji'''
        return await self._request('DELETE', uri=f'/guilds/{guild_id}/emojis/{emoji_id}')

    # -----======= S T I C K E R  =======-----
    async def get_sticker(self, sticker_id) -> dict:
        '''https://discord.com/developers/docs/resources/sticker#get-sticker'''
        return await self._request('GET', uri=f'/stickers/{sticker_id}')
        
    async def list_nitro_sticker_packs(self) -> dict:
        '''https://discord.com/developers/docs/resources/sticker#list-nitro-sticker-packs'''
        return await self._request('GET', uri=f'/sticker-packs')

    async def list_guild_stickers(self, guild_id) -> dict:
        '''https://discord.com/developers/docs/resources/sticker#list-guild-stickers'''
        return await self._request('GET', uri=f'/guilds/{guild_id}/stickers')

    async def get_guild_sticker(self, guild_id, sticker_id) -> dict:
        '''https://discord.com/developers/docs/resources/sticker#get-guild-sticker'''
        return await self._request('GET', uri=f'/guilds/{guild_id}/stickers/{sticker_id}')

    async def create_guild_sticker(self, guild_id, name: str, description: str, tags: str, file) -> dict:
        '''https://discord.com/developers/docs/resources/sticker#create-guild-sticker'''
        payload = {
            'name': name,
            'description': description,
            'tags': tags,
            'file': file
        }
        payload = {k:v for k,v in payload.items() if v is not None}
        return await self._request('POST', params=payload, uri=f'/guilds/{guild_id}/stickers')

    async def modify_guild_sticker(self, name: str=None, description: str=None, tags: str=None) -> dict:
        '''https://discord.com/developers/docs/resources/sticker#modify-guild-sticker'''
        payload = {
            'name': name,
            'description': description,
            'tags': tags
        }
        payload = {k:v for k,v in payload.items() if v is not None}
        return await self._request('PATCH', params=payload, uri=f'/guilds/{guild_id}/stickers/{sticker_id}')

    async def delete_guild_sticker(self, guild_id, sticker_id) -> dict:
        '''https://discord.com/developers/docs/resources/sticker#delete-guild-sticker'''
        return await self._request('DELETE', uri=f'/guilds/{guild_id}/stickers/{sticker_id}')
