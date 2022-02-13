from python_discord_client.base_request.base_request import BaseRequestAPI

class GuildData(BaseRequestAPI):

    def __init__(self, token: str):
        self._token = token
        self._session = self._get_session()

    def send_message(self, channel_id, message: str) -> dict:
        '''Sends a text message to a channel'''
        payload = { 'content': message }
        return self._request(method='POST', params=payload, uri=f'/channels/{channel_id}/messages')

    def create_guild(self, 
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
        '''
        https://discord.com/developers/docs/resources/guild#create-guild
        '''
        payload = { 'name': name }
        if region:
            payload['region'] = region
        if icon:
            payload['icon'] = icon
        if verification_level:
            payload['verification_level'] = verification_level
        if default_message_notifications:
            payload['default_message_notifications'] = default_message_notifications
        if explicit_content_filter:
            payload['explicit_content_filter'] = explicit_content_filter
        if roles:
            payload['roles'] = roles
        if channels:
            payload['channels'] = channels
        if afk_channel_id:
            payload['afk_channel_id'] = afk_channel_id
        if afk_timeout:
            payload['afk_timeout'] = afk_timeout
        if system_channel_id:
            payload['system_channel_id'] = system_channel_id
        if system_channel_flags:
            payload['system_channel_flags'] = system_channel_flags
            
        return self._request('POST', params = payload, uri='/guilds')

    def get_guild(self, guild_id, with_counts: bool=False) -> dict:
        '''
        https://discord.com/developers/docs/resources/guild#get-guild
        '''
        params = {
            'width_couunts': with_counts
        }
        return self._request('GET', params=params, uri=f'/guilds/{guild_id}')

    def get_guild_preview(self, guild_id) -> dict:
        '''https://discord.com/developers/docs/resources/guild#get-guild-preview'''
        return self._request(method='GET', uri=f'/guilds/{guild_id}/preview')

    def modify_guild(self,
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
        payload = { 'name': name }
        if region != None:
            payload['region'] = region
        if verification_level != None:
            payload['verification_level'] = verification_level
        if default_message_notifications != None:
            payload['default_message_notifications'] = default_message_notifications
        if explicit_content_filter != None:
            payload['explicit_content_filter'] = explicit_content_filter
        if afk_channel_id != None:
            payload['afk_channel_id'] = afk_channel_id
        if afk_timeout != None:
            payload['afk_timeout'] = afk_timeout
        if icon != None:
            payload['icon'] = icon
        if owner_id != None:
            payload['owner_id'] = owner_id
        if splash != None:
            payload['splash'] = splash
        if discovery_splash != None:
            payload['discovery_splash'] = discovery_splash
        if banner != None:
            payload['banner'] = banner
        if system_channel_id != None:
            payload['system_channel_id'] = system_channel_id
        if system_channel_flags != None:
            payload['system_channel_flags'] = system_channel_flags
        if public_updates_channel_id != None:
            payload['public_updates_channel_id'] = public_updates_channel_id
        if preferred_locale != None:
            payload['preferred_locale'] = preferred_locale
        if features != None:
            payload['features'] = features
        if description != None:
            payload['description'] = description

        return self._request(method='POST', params=payload, uri=f'/guilds/{guild_id}')

    def delete_guild(self, guild_id) -> dict:
        '''https://discord.com/developers/docs/resources/guild#delete-guild'''
        return self._request(method='DELETE', uri=f'/guilds/{guild_id}')

    def get_guild_channels(self, guild_id) -> dict:
        '''https://discord.com/developers/docs/resources/guild#get-guild-channels'''
        return self._request(method='GET', uri=f'/guilds/{guild_id}/channels')

    def create_guild_channel(self, 
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
        return self._request(method='POST', params=payload, uri=f'/guilds/{guild_id}/channels')

    def modify_channel_positions(self, 
        guild_id, id, position: int=None, lock_permissions: bool=None, parent_id=None
    ) -> dict:
        '''https://discord.com/developers/docs/resources/guild#modify-guild-channel-positions'''
        payload = { 'id': id }
        if position:
            payload['position'] = position
        if lock_permissions:
            payload['lock_permissions'] = lock_permissions
        if parent_id:
            payload['parent_id'] = parent_id
        return self._request(method='PATCH', params=payload, uri=f'/guilds/{guild_id}/channels')

    def list_active_threads(self, guild_id, threads: list, members: list) -> dict:
        '''https://discord.com/developers/docs/resources/guild#list-active-threads'''
        payload = { 'threads': threads, 'members': members }
        return self._request(method='GET', params=payload, uri=f'/guilds/{guild_id}/threads/active')

    def get_guild_member(self, guild_id, user_id) -> dict:
        '''https://discord.com/developers/docs/resources/guild#get-guild-member'''
        return self._request(method='GET', uri=f'/guilds/{guild_id}/members/{user_id}')

    def list_guild_members(self, guild_id, limit: int, after) -> dict:
        '''https://discord.com/developers/docs/resources/guild#list-guild-members'''
        params = {}
        if limit != None: 
            params['limit'] = limit
        if after != None:
            params['after'] = after
        return self._request(method='GET', params=params, uri=f'/guilds/{guild_id}/members')

    def search_guild_members(self, guild_id, query: str, limit:int=None) -> dict:
        '''https://discord.com/developers/docs/resources/guild#search-guild-members'''
        params = { 'query': query }
        if limit != None: 
            params['limit'] = limit
        return self._request(method='GET', params=params, uri=f'/guilds/{guild_id}/members/search')

    def add_guild_member(self, guild_id, user_id, access_token: str, nick: str, roles: list, mute: bool, deaf: bool) -> dict:
        '''https://discord.com/developers/docs/resources/guild#add-guild-member'''
        payload = {
            'access_token': access_token,
            'nick': nick,
            'roles': roles,
            'mute': mute,
            'deaf': deaf
        }
        return self._request(method='PUT', params=payload, uri=f'/guilds/{guild_id}/members/{user_id}')

    def modify_current_member(self, guild_id, nick: str=None) -> dict:
        '''https://discord.com/developers/docs/resources/guild#modify-current-member'''
        payload = {}
        if nick != None:
            payload['nick'] = nick
        return self._request(method='PATCH', params=payload, uri=f'/guilds/{guild_id}/members/@me')

    def add_guild_member_role(self, guild_id, user_id, role_id) -> dict:
        '''https://discord.com/developers/docs/resources/guild#add-guild-member-role'''

        return self._request(method='PUT', uri=f'/guilds/{guild_id}/members/{user_id}/roles/{role_id}')

    def remove_guild_member_role(self, guild_id, user_id, role_id) -> dict:
        '''https://discord.com/developers/docs/resources/guild#remove-guild-member-role'''
        return self._request(method='DELETE', uri=f'/guilds/{guild_id}/members/{user_id}/roles/{role_id}')

    def remove_guild_member(self, guild_id, user_id) -> dict:
        '''https://discord.com/developers/docs/resources/guild#remove-guild-member'''
        return self._request(method='DELETE', uri=f'/guilds/{guild_id}/members/{user_id}')

    def get_guild_bans(self, guild_id) -> dict:
        '''https://discord.com/developers/docs/resources/guild#get-guild-bans'''
        return self._request(method='GET', uri=f'/guilds/{guild_id}/bans')

    def get_guild_ban(self, guild_id, user_id) -> dict:
        '''https://discord.com/developers/docs/resources/guild#get-guild-ban'''
        return self._request(method='GET', uri=f'/guilds/{guild_id}/bans/{user_id}')

    def create_guild_ban(self, guild_id, user_id, delete_message_days: int=None, reason: str=None) -> dict:
        '''https://discord.com/developers/docs/resources/guild#create-guild-ban'''
        params = {}
        if delete_message_days != None:
            params['delete_message_days'] = delete_message_days
        if reason != None:
            params['reason'] = reason
        return self._request(method='PUT', params=params, uri=f'/guilds/{guild_id}/bans/{user_id}')

    def remove_guild_ban(self, guild_id, user_id) -> dict:
        '''https://discord.com/developers/docs/resources/guild#remove-guild-ban'''
        return self._request(method='DELETE', uri=f'/guilds/{guild_id}/bans/{user_id}')

    def get_guild_roles(self, guild_id) -> dict:
        '''https://discord.com/developers/docs/resources/guild#get-guild-roles'''
        return self._request(method='GET', uri=f'/guilds/{guild_id}/roles')

    def create_guild_role(self, 
        guild_id, name: str, permissions: str, 
        color: int, hoist: bool, icon, unicode_emoji: str, 
        mentionable: bool
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
        return self._request(method='POST', params=payload, uri=f'/guilds/{guild_id}/roles')

    def modify_guild_role_permissions(self, guild_id, id, position: int=None) -> dict:
        '''https://discord.com/developers/docs/resources/guild#modify-guild-role-positions'''
        payload = { 'id': id }
        if position != None:
            payload['position'] = position
        return self._request(method='PATCH', params=payload, uri=f'/guilds/{guild_id}/roles')

    def modify_guild_role(self, 
        guild_id, role_id, name: str=None, permission: str=None, 
        color: int=None, hoist: bool=None, icon=None, unicode_emoji: str=None, mentionable: bool=None
    ) -> dict:
        '''https://discord.com/developers/docs/resources/guild#modify-guild-role'''
        payload = {}
        if name != None:
            payload['name'] = name
        if permission != None:
            payload['permission'] = permission
        if color != None:
            payload['color'] = color
        if hoist != None:
            payload['hoist'] = hoist
        if icon != None:
            payload['icon'] = icon
        if unicode_emoji != None:
            payload['unicode_emoji'] = unicode_emoji
        if mentionable != None:
            payload['mentionable'] = mentionable
        return self._request(method='PATCH', params=payload, uri=f'/guilds/{guild_id}/roles/{role_id}')

    def delete_guild_role(self, guild_id, role_id) -> dict:
        '''https://discord.com/developers/docs/resources/guild#delete-guild-role'''
        return self._request(method='DELETE', uri=f'/guilds/{guild_id}/roles/{role_id}')

    def get_guild_prune_count(self, guild_id, days: int=7, include_roles: str=None) -> dict:
        '''https://discord.com/developers/docs/resources/guild#get-guild-prune-count'''
        params = {}
        if days != None:
            params['days'] = days
        if include_roles != None:
            params['include_roles'] = include_roles
        return self._request(method='GET', params=params, uri=f'/guilds/{guild_id}/prune')

    def beginn_guild_prune(self, guild_id, days: int, compute_prune_count: bool, include_roles: str, reason: str=None) -> dict:
        '''https://discord.com/developers/docs/resources/guild#begin-guild-prune'''
        payload = {
            'days': days,
            'compute_prune_count': compute_prune_count,
            'include_roles': include_roles
        }
        if reason != None:
            payload['reason'] = reason
        return self._request(method='POST', params=payload, uri=f'/guilds/{guild_id}/prune')

    def get_guild_voice_regions(self, guild_id) -> dict:
        '''https://discord.com/developers/docs/resources/guild#get-guild-voice-regions'''
        return self._request(method='GET', uri=f'/guilds/{guild_id}/regions')

    def get_guild_invites(self, guild_id) -> dict:
        '''https://discord.com/developers/docs/resources/guild#get-guild-invites'''
        return self._request(method='GET', uri=f'/guilds/{guild_id}/invites')

    def get_guild_integrations(self, guild_id) -> dict:
        '''https://discord.com/developers/docs/resources/guild#get-guild-integrations'''
        return self._request(method='GET', uri=f'/guilds/{guild_id}/integrations')

    def delete_guild_integrations(self, guild_id, integration_id) -> dict:
        '''https://discord.com/developers/docs/resources/guild#delete-guild-integration'''
        return self._request(method='DELETE', uri=f'/guilds/{guild_id}/integrations/{integration_id}')

    def get_guild_widget_settings(self, guild_id) -> dict:
        '''https://discord.com/developers/docs/resources/guild#get-guild-widget-settings'''
        return self._request(method='DELETE', uri=f'/guilds/{guild_id}/widget')

    def modify_guild_widget(self, guild_id, settings: dict) -> dict:
        '''https://discord.com/developers/docs/resources/guild#modify-guild-widget'''
        return self._request(method='PATCH', params=settings, uri=f'/guilds/{guild_id}/widget')

    def get_guild_widget(self, guild_id) -> dict:
        '''https://discord.com/developers/docs/resources/guild#get-guild-widget'''
        return self._request(method='GET', uri=f'/guilds/{guild_id}/widget.json')

    def get_guild_vanity_url(self, guild_id) -> dict:
        '''https://discord.com/developers/docs/resources/guild#get-guild-vanity-url'''
        return self._request(method='GET', uri=f'/guilds/{guild_id}/vanity-url')

    def get_guild_widget_image(self, guild_id, style: str) -> dict:
        '''https://discord.com/developers/docs/resources/guild#get-guild-widget-image
        @param style can be one of : [shield, banner1, banner2, banner3, banner4]
        '''
        params = { 'style': style }
        return self._request(method='GET', params=params, uri=f'/guilds/{guild_id}/widget.png')

    def get_guild_welcome_screen(self, guild_id) -> dict:
        '''https://discord.com/developers/docs/resources/guild#get-guild-welcome-screen'''
        return self._request(method='GET', params=params, uri=f'/guilds/{guild_id}/welcome-screen')

    def modify_guild_welcome_screen(self, guild_id, enabled: bool=None, welcome_channels: list=None, description: str=None) -> dict:
        '''https://discord.com/developers/docs/resources/guild#modify-guild-welcome-screen'''
        params = {}
        if enabled != None:
            params['enabled'] = enabled
        if welcome_channels != None:
            params['welcome_channels'] = welcome_channels
        if description != None:
            params['description'] = description
        return self._request(method='PATCH', params=params, uri=f'/guilds/{guild_id}/welcome-screen')

    def modify_current_user_voice_state(self, guild_id, channel_id, suppress: bool=None, request_to_speak_timestamp=None) -> dict:
        '''https://discord.com/developers/docs/resources/guild#modify-current-user-voice-state'''
        params = { 'channel_id': channel_id }
        if suppress != None:
            params['suppress'] = suppress
        if request_to_speak_timestamp != None:
            params['request_to_speak_timestamp'] = request_to_speak_timestamp
        return self._request(method='PATCH', params=params, uri=f'/guilds/{guild_id}/voice-states/@me')
    
    def modify_user_voice_state(self, guild_id, user_id, channel_id, suppress: bool=None) -> dict:
        '''https://discord.com/developers/docs/resources/guild#modify-user-voice-state'''
        params = { 'channel_id': channel_id }
        if suppress != None:
            params['suppress'] = suppress
        return self._request(method='PATCH', params=params, uri=f'/guilds/{guild_id}/voice-states/{user_id}e')

    