from discoPy.base_request.base_request import BaseRequestAPI

class ApplicationData(BaseRequestAPI):
    '''Contains a collection of application related methods.'''

    def __init__(self, token: str, url: str=None):
        super().__init__(token, url)

    def get_application_commands(self, application_id) -> dict:
        '''https://discord.com/developers/docs/interactions/application-commands#get-global-application-commands'''
        return self._request('GET', uri=f'/applications/{application_id}/commands')

    def create_application_command(self,
        application_id,
        name: str,
        description: str,
        options: list=None,
        default_permission: bool=None,
        type=None
    ) -> dict:
        '''https://discord.com/developers/docs/interactions/application-commands#create-global-application-command'''
        payload = {
            'name': name,
            'description': description
        }
        if options != None:
            payload['options'] = options
        if default_permission != None:
            payload['default_permission'] = default_permission
        if type != None:
            payload['type'] = type
        return self._request('POST', params=payload, uri=f'/applications/{application_id}/commands')

    def get_global_application_command(self, application_id, command_id) -> dict:
        '''https://discord.com/developers/docs/interactions/application-commands#get-global-application-command'''
        return self._request('GET', uri=f'/applications/{application_id}/commands/{command_id}')

    def edit_global_application_command(self, 
        application_id,
        command_id,
        name: str=None,
        description: str=None,
        options: list=None,
        default_permission: bool=None
    ) -> dict:
        '''https://discord.com/developers/docs/interactions/application-commands#edit-global-application-command'''
        payload = {}
        if name != None:
            payload['name'] = name
        if description != None:
            payload['description'] = description
        if options != None:
            payload['options'] = options
        if default_permission != None:
            payload['default_permission'] = default_permission
        return self._request('PATCH', params=payload, uri=f'/applications/{application_id}/commands/{command_id}')

    def delete_global_application_command(self, application_id, command_id) -> dict:
        '''https://discord.com/developers/docs/interactions/application-commands#delete-global-application-command'''
        return self._request('DELETE', uri=f'/applications/{application_id}/commands/{command_id}')

    def bulk_overwrite_global_application_command(self, application_id) -> dict:
        '''https://discord.com/developers/docs/interactions/application-commands#bulk-overwrite-global-application-commands'''
        return self._request('PUT', uri=f'/applications/{application_id}/commands')

    def get_guild_application_commands(self, application_id, guild_id) -> dict:
        '''https://discord.com/developers/docs/interactions/application-commands#get-guild-application-commands'''
        return self._request('GET', uri=f'/applications/{application_id}/guilds/{guild_id}/commands')

    def create_guild_application_command(self, 
        application_id,
        guild_id,
        name: str,
        description: str,
        options: list=None,
        default_permission: bool=None,
        type=None
    ) -> dict:
        '''https://discord.com/developers/docs/interactions/application-commands#create-guild-application-command'''
        payload = {
            'name': name,
            'description': description
        }
        if options != None:
            payload['options'] = options
        if default_permission != None:
            payload['default_permission'] = default_permission
        if type != None:
            payload['type'] = type
        return self._request('POST', params=payload,uri=f'/applications/{application_id}/guilds/{guild_id}/commands')

    def get_guild_application_command(self, application_id, guild_id, command_id) -> dict:
        '''https://discord.com/developers/docs/interactions/application-commands#get-guild-application-command'''
        return self._request('GET', uri=f'/applications/{application_id}/guilds/{guild_id}/commands/{command_id}')

    def edit_guild_application_command(self,
        application_id, 
        guild_id,
        command_id,
        name: str=None,
        description: str=None,
        options: list=None,
        default_permission: bool=None
    ) -> dict:
        '''https://discord.com/developers/docs/interactions/application-commands#edit-guild-application-command'''
        payload = {}
        if name != None:
            payload['name'] = name
        if description != None:
            payload['description'] = description
        if options != None:
            payload['options'] = options
        if default_permission != None:
            payload['default_permission'] = default_permission
        if type != None:
            payload['type'] = type
        return self._request('PATCH', params=payload, uri=f'/applications/{application_id}/guilds/{guild_id}/commands/{command_id}')

    def delete_guild_application_command(self, application_id, guild_id, command_id) -> dict:
        '''https://discord.com/developers/docs/interactions/application-commands#delete-guild-application-command'''
        return self._request('DELETE', uri=f'/applications/{application_id}/guilds/{guild_id}/commands/{command_id}')

    def bulk_overwrite_guild_application_command(self, application_id, guild_id, new_commands: list=None) -> dict:
        '''https://discord.com/developers/docs/interactions/application-commands#bulk-overwrite-guild-application-commands'''
        params = {}
        if new_commands != None:
            params['new_commands'] = new_commands
        return self._request('PUT', params=params, uri=f'/applications/{application_id}/guilds/{guild_id}/commands')

    def get_guild_application_command_permissions(self, application_id, guild_id) -> dict:
        '''https://discord.com/developers/docs/interactions/application-commands#get-guild-application-command-permissions'''
        return self._request('GET', uri=f'/applications/{application_id}/guilds/{guild_id}/commands/permissions')

    def get_application_comman_permissions(self, application_id, guild_id, command_id) -> dict:
        '''https://discord.com/developers/docs/interactions/application-commands#get-application-command-permissions'''
        return self._request('GET', uri=f'/applications/{application_id}/guilds/{guild_id}/commands/{command_id}/permissions')

    def edit_application_command_permissions(self, application_id, guild_id, command_id, permissions: list) -> dict:
        '''https://discord.com/developers/docs/interactions/application-commands#edit-application-command-permissions'''
        payload = { 'permissions': permissions }
        return self._request('PUT', uri=f'/applications/{application_id}/guilds/{guild_id}/commands/{command_id}/permissions')

    def batch_edit_application_command_permissions(self, application_id, guild_id, commands: [dict]) -> dict:
        '''https://discord.com/developers/docs/interactions/application-commands#batch-edit-application-command-permissions'''
        return self._request('PUT', params=commands, uri=f'/applications/{application_id}/guilds/{guild_id}/commands/permissions')



