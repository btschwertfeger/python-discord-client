# -*- coding: utf-8 -*-


"""Module that implements the REST application related functions."""


from typing import Optional, Union

from discord.base_request import BaseRequestAPI


class Application(BaseRequestAPI):
    """Contains a collection of application related methods."""

    def get_application_commands(self: "Application", application_id: str) -> dict:
        """https://discord.com/developers/docs/interactions/application-commands#get-global-application-commands"""
        return self._request(  # type: ignore[no-any-return]
            "GET", uri=f"/applications/{application_id}/commands"
        )

    def create_application_command(
        self: "Application",
        application_id: str,
        name: str,
        description: str,
        options: Optional[list] = None,
        default_permission: Optional[bool] = None,
        type_: Optional[Union[str, int]] = None,
    ) -> dict:
        """https://discord.com/developers/docs/interactions/application-commands#create-global-application-command"""
        payload: dict = {
            "name": name,
            "description": description,
            "options": options,
            "default_permission": default_permission,
            "type": type_,
        }
        return self._request(  # type: ignore[no-any-return]
            "POST",
            params={k: v for k, v in payload.items() if v is not None},
            uri=f"/applications/{application_id}/commands",
        )

    def get_global_application_command(
        self: "Application", application_id: str, command_id: str
    ) -> dict:
        """https://discord.com/developers/docs/interactions/application-commands#get-global-application-command"""
        return self._request(  # type: ignore[no-any-return]
            "GET", uri=f"/applications/{application_id}/commands/{command_id}"
        )

    def edit_global_application_command(
        self: "Application",
        application_id: str,
        command_id: str,
        name: Optional[str] = None,
        description: Optional[str] = None,
        options: Optional[list] = None,
        default_permission: Optional[bool] = None,
    ) -> dict:
        """https://discord.com/developers/docs/interactions/application-commands#edit-global-application-command"""
        payload: dict = {
            "name": name,
            "description": description,
            "options": options,
            "default_permission": default_permission,
        }
        return self._request(  # type: ignore[no-any-return]
            "PATCH",
            params={k: v for k, v in payload.items() if v is not None},
            uri=f"/applications/{application_id}/commands/{command_id}",
        )

    def delete_global_application_command(
        self: "Application", application_id: str, command_id: str
    ) -> dict:
        """https://discord.com/developers/docs/interactions/application-commands#delete-global-application-command"""
        return self._request(  # type: ignore[no-any-return]
            "DELETE", uri=f"/applications/{application_id}/commands/{command_id}"
        )

    def bulk_overwrite_global_application_command(
        self: "Application", application_id: str
    ) -> dict:
        """https://discord.com/developers/docs/interactions/application-commands#bulk-overwrite-global-application-commands"""
        return self._request(  # type: ignore[no-any-return]
            "PUT", uri=f"/applications/{application_id}/commands"
        )

    def get_guild_application_commands(
        self: "Application", application_id: str, guild_id: str
    ) -> dict:
        """https://discord.com/developers/docs/interactions/application-commands#get-guild-application-commands"""
        return self._request(  # type: ignore[no-any-return]
            "GET", uri=f"/applications/{application_id}/guilds/{guild_id}/commands"
        )

    def create_guild_application_command(
        self: "Application",
        application_id: str,
        guild_id: str,
        name: str,
        description: str,
        options: Optional[list] = None,
        default_permission: Optional[bool] = None,
        type_: Optional[str] = None,
    ) -> dict:
        """https://discord.com/developers/docs/interactions/application-commands#create-guild-application-command"""
        payload: dict = {
            "name": name,
            "description": description,
            "options": options,
            "default_permission": default_permission,
            "type": type_,
        }
        return self._request(  # type: ignore[no-any-return]
            "POST",
            params={k: v for k, v in payload.items() if v is not None},
            uri=f"/applications/{application_id}/guilds/{guild_id}/commands",
        )

    def get_guild_application_command(
        self: "Application", application_id: str, guild_id: str, command_id: str
    ) -> dict:
        """https://discord.com/developers/docs/interactions/application-commands#get-guild-application-command"""
        return self._request(  # type: ignore[no-any-return]
            "GET",
            uri=f"/applications/{application_id}/guilds/{guild_id}/commands/{command_id}",
        )

    def edit_guild_application_command(
        self: "Application",
        application_id: str,
        guild_id: str,
        command_id: str,
        name: Optional[str] = None,
        description: Optional[str] = None,
        options: Optional[list] = None,
        default_permission: Optional[bool] = None,
    ) -> dict:
        """https://discord.com/developers/docs/interactions/application-commands#edit-guild-application-command"""
        payload: dict = {
            "name": name,
            "description": description,
            "options": options,
            "default_permission": default_permission,
            "type": type,
        }
        return self._request(  # type: ignore[no-any-return]
            "PATCH",
            params={k: v for k, v in payload.items() if v is not None},
            uri=f"/applications/{application_id}/guilds/{guild_id}/commands/{command_id}",
        )

    def delete_guild_application_command(
        self: "Application", application_id: str, guild_id: str, command_id: str
    ) -> dict:
        """https://discord.com/developers/docs/interactions/application-commands#delete-guild-application-command"""
        return self._request(  # type: ignore[no-any-return]
            "DELETE",
            uri=f"/applications/{application_id}/guilds/{guild_id}/commands/{command_id}",
        )

    def bulk_overwrite_guild_application_command(
        self: "Application",
        application_id: str,
        guild_id: str,
        new_commands: Optional[list] = None,
    ) -> dict:
        """https://discord.com/developers/docs/interactions/application-commands#bulk-overwrite-guild-application-commands"""
        payload: dict = {"new_commands": new_commands}
        return self._request(  # type: ignore[no-any-return]
            "PUT",
            params={k: v for k, v in payload.items() if v is not None},
            uri=f"/applications/{application_id}/guilds/{guild_id}/commands",
        )

    def get_guild_application_command_permissions(
        self: "Application", application_id: str, guild_id: str
    ) -> dict:
        """https://discord.com/developers/docs/interactions/application-commands#get-guild-application-command-permissions"""
        return self._request(  # type: ignore[no-any-return]
            "GET",
            uri=f"/applications/{application_id}/guilds/{guild_id}/commands/permissions",
        )

    def get_application_comman_permissions(
        self: "Application", application_id: str, guild_id: str, command_id: str
    ) -> dict:
        """https://discord.com/developers/docs/interactions/application-commands#get-application-command-permissions"""
        return self._request(  # type: ignore[no-any-return]
            "GET",
            uri=f"/applications/{application_id}/guilds/{guild_id}/commands/{command_id}/permissions",
        )

    def edit_application_command_permissions(
        self: "Application",
        application_id: str,
        guild_id: str,
        command_id: str,
        permissions: list,
    ) -> dict:
        """https://discord.com/developers/docs/interactions/application-commands#edit-application-command-permissions"""
        return self._request(  # type: ignore[no-any-return]
            "PUT",
            uri=f"/applications/{application_id}/guilds/{guild_id}/commands/{command_id}/permissions",
            params={"permissions": permissions},
        )
