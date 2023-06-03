from discord.rest.base_request import BaseRequestAPI

from typing import Optional, Any


class Guild(BaseRequestAPI):
    """Contains a collection of guild/server related methods."""

    def create_guild(
        self: "Guild",
        name: str,
        region: Optional[str] = None,
        icon: Optional[Any] = None,
        verification_level: Optional[int] = None,
        default_message_notifications: Optional[int] = None,
        explicit_content_filter: Optional[int] = None,
        roles: Optional[list] = None,
        channels: Optional[list] = None,
        afk_channel_id: Optional[str] = None,
        afk_timeout: Optional[int] = None,
        system_channel_id: Optional[str] = None,
        system_channel_flags: Optional[int] = None,
    ) -> dict:
        """https://discord.com/developers/docs/resources/guild#create-guild"""
        payload: dict = {
            "name": name,
            "region": region,
            "icon": icon,
            "verification_level": verification_level,
            "default_message_notifications": default_message_notifications,
            "explicit_content_filter": explicit_content_filter,
            "roles": roles,
            "channels": channels,
            "afk_channel_id": afk_channel_id,
            "afk_timeout": afk_timeout,
            "system_channel_id": system_channel_id,
            "system_channel_flags": system_channel_flags,
        }
        return self._request(  # type: ignore[no-any-return]
            "POST",
            params={k: v for k, v in payload.items() if v is not None},
            uri="/guilds",
        )

    def get_guild(self: "Guild", guild_id: str, with_counts: bool = False) -> dict:
        """https://discord.com/developers/docs/resources/guild#get-guild"""
        return self._request(  # type: ignore[no-any-return]
            "GET", params={"width_couunts": with_counts}, uri=f"/guilds/{guild_id}"
        )

    def get_guild_preview(self: "Guild", guild_id: str) -> dict:
        """https://discord.com/developers/docs/resources/guild#get-guild-preview"""
        return self._request(  # type: ignore[no-any-return]
            method="GET", uri=f"/guilds/{guild_id}/preview"
        )

    def modify_guild(
        self: "Guild",
        guild_id: str,
        name: str,
        region: Optional[str] = None,
        verification_level: Optional[int] = None,
        default_message_notifications: Optional[int] = None,
        explicit_content_filter: Optional[int] = None,
        afk_channel_id: Optional[str] = None,
        afk_timeout: Optional[int] = None,
        icon: Optional[Any] = None,
        owner_id: Optional[str] = None,
        splash: Optional[Any] = None,
        discovery_splash: Optional[Any] = None,
        banner: Optional[Any] = None,
        system_channel_id: Optional[Any] = None,
        system_channel_flags: Optional[int] = None,
        rules_channel_id: Optional[str] = None,
        public_updates_channel_id: Optional[str] = None,
        preferred_locale: Optional[str] = None,
        features: Optional[list] = None,
        description: Optional[str] = None,
        premium_progress_bar_enabled: Optional[bool] = None,
    ) -> dict:
        """https://discord.com/developers/docs/resources/guild#modify-guild"""
        payload: dict = {
            "name": name,
            "region": region,
            "verification_level": verification_level,
            "default_message_notifications": default_message_notifications,
            "explicit_content_filter": explicit_content_filter,
            "afk_channel_id": afk_channel_id,
            "afk_timeout": afk_timeout,
            "icon": icon,
            "owner_id": owner_id,
            "splash": splash,
            "discovery_splash": discovery_splash,
            "banner": banner,
            "system_channel_id": system_channel_id,
            "system_channel_flags": system_channel_flags,
            "public_updates_channel_id": public_updates_channel_id,
            "preferred_locale": preferred_locale,
            "features": features,
            "description": description,
            "rules_channel_id": rules_channel_id,
            "premium_progress_bar_enabled": premium_progress_bar_enabled,
        }
        return self._request(  # type: ignore[no-any-return]
            method="POST",
            params={k: v for k, v in payload.items() if v is not None},
            uri=f"/guilds/{guild_id}",
        )

    def delete_guild(self: "Guild", guild_id: str) -> dict:
        """https://discord.com/developers/docs/resources/guild#delete-guild"""
        return self._request(  # type: ignore[no-any-return]
            method="DELETE", uri=f"/guilds/{guild_id}"
        )

    def get_guild_channels(self: "Guild", guild_id: str) -> dict:
        """https://discord.com/developers/docs/resources/guild#get-guild-channels"""
        return self._request(  # type: ignore[no-any-return]
            method="GET", uri=f"/guilds/{guild_id}/channels"
        )

    def create_guild_channel(
        self: "Guild",
        guild_id: str,
        name: str,
        type: int,
        topic: str,
        bitrate: int,
        user_limit: int,
        rate_limit_per_user: int,
        position: int,
        permission_overwrites: list,
        parent_id: str,
        nsfw: bool,
    ) -> dict:
        """https://discord.com/developers/docs/resources/guild#create-guild-channel"""
        payload: dict = {
            "guild_id": guild_id,
            "name": name,
            "type": type,
            "topic": topic,
            "bitrate": bitrate,
            "user_limit": user_limit,
            "rate_limit_per_user": rate_limit_per_user,
            "position": position,
            "permission_overwrites": permission_overwrites,
            "parent_id": parent_id,
            "nsfw": nsfw,
        }
        return self._request(  # type: ignore[no-any-return]
            method="POST",
            params={k: v for k, v in payload.items() if v is not None},
            uri=f"/guilds/{guild_id}/channels",
        )

    def modify_channel_positions(
        self: "Guild",
        guild_id: str,
        id: str,
        position: Optional[int] = None,
        lock_permissions: Optional[bool] = None,
        parent_id: Optional[Any] = None,
    ) -> dict:
        """https://discord.com/developers/docs/resources/guild#modify-guild-channel-positions"""
        payload: dict = {
            "id": id,
            "position": position,
            "lock_permissions": lock_permissions,
            "parent_id": parent_id,
        }
        return self._request(  # type: ignore[no-any-return]
            method="PATCH",
            params={k: v for k, v in payload.items() if v is not None},
            uri=f"/guilds/{guild_id}/channels",
        )

    def list_active_threads(self: "Guild", guild_id: str) -> dict:
        """https://discord.com/developers/docs/resources/guild#list-active-threads"""
        return self._request(  # type: ignore[no-any-return]
            method="GET", uri=f"/guilds/{guild_id}/threads/active"
        )

    def get_guild_member(self: "Guild", guild_id: str, user_id: str) -> dict:
        """https://discord.com/developers/docs/resources/guild#get-guild-member"""
        return self._request(  # type: ignore[no-any-return]
            method="GET", uri=f"/guilds/{guild_id}/members/{user_id}"
        )

    def list_guild_members(
        self: "Guild", guild_id: str, limit: int, after: Any
    ) -> dict:
        """https://discord.com/developers/docs/resources/guild#list-guild-members"""
        payload: dict = {"limit": limit, "after": after}
        return self._request(  # type: ignore[no-any-return]
            method="GET",
            params={k: v for k, v in payload.items() if v is not None},
            uri=f"/guilds/{guild_id}/members",
        )

    def search_guild_members(
        self: "Guild", guild_id: str, query: str, limit: int = None
    ) -> dict:
        """https://discord.com/developers/docs/resources/guild#search-guild-members"""
        payload: dict = {"query": query, "limit": limit}
        return self._request(  # type: ignore[no-any-return]
            method="GET",
            params={k: v for k, v in payload.items() if v is not None},
            uri=f"/guilds/{guild_id}/members/search",
        )

    def add_guild_member(
        self: "Guild",
        guild_id: str,
        user_id: str,
        access_token: str,
        nick: str,
        roles: list,
        mute: bool,
        deaf: bool,
    ) -> dict:
        """https://discord.com/developers/docs/resources/guild#add-guild-member"""
        payload: dict = {
            "access_token": access_token,
            "nick": nick,
            "roles": roles,
            "mute": mute,
            "deaf": deaf,
        }

        return self._request(  # type: ignore[no-any-return]
            method="PUT",
            params={k: v for k, v in payload.items() if v is not None},
            uri=f"/guilds/{guild_id}/members/{user_id}",
        )

    def modify_current_member(
        self: "Guild", guild_id: str, nick: Optional[str] = None
    ) -> dict:
        """https://discord.com/developers/docs/resources/guild#modify-current-member"""
        payload: dict = {"nick": nick}
        return self._request(  # type: ignore[no-any-return]
            method="PATCH",
            params={k: v for k, v in payload.items() if v is not None},
            uri=f"/guilds/{guild_id}/members/@me",
        )

    def add_guild_member_role(
        self: "Guild", guild_id: str, user_id: str, role_id: str
    ) -> dict:
        """https://discord.com/developers/docs/resources/guild#add-guild-member-role"""
        return self._request(  # type: ignore[no-any-return]
            method="PUT", uri=f"/guilds/{guild_id}/members/{user_id}/roles/{role_id}"
        )

    def remove_guild_member_role(
        self: "Guild", guild_id: str, user_id: str, role_id: str
    ) -> dict:
        """https://discord.com/developers/docs/resources/guild#remove-guild-member-role"""
        return self._request(  # type: ignore[no-any-return]
            method="DELETE", uri=f"/guilds/{guild_id}/members/{user_id}/roles/{role_id}"
        )

    def remove_guild_member(self: "Guild", guild_id: str, user_id: str) -> dict:
        """https://discord.com/developers/docs/resources/guild#remove-guild-member"""
        return self._request(  # type: ignore[no-any-return]
            method="DELETE", uri=f"/guilds/{guild_id}/members/{user_id}"
        )

    def get_guild_bans(self: "Guild", guild_id: str) -> dict:
        """https://discord.com/developers/docs/resources/guild#get-guild-bans"""
        return self._request(  # type: ignore[no-any-return]
            method="GET", uri=f"/guilds/{guild_id}/bans"
        )

    def get_guild_ban(self: "Guild", guild_id: str, user_id: str) -> dict:
        """https://discord.com/developers/docs/resources/guild#get-guild-ban"""
        return self._request(  # type: ignore[no-any-return]
            method="GET", uri=f"/guilds/{guild_id}/bans/{user_id}"
        )

    def create_guild_ban(
        self: "Guild",
        guild_id: str,
        user_id: str,
        delete_message_days: Optional[int] = None,
        reason: Optional[str] = None,
    ) -> dict:
        """https://discord.com/developers/docs/resources/guild#create-guild-ban"""
        payload: dict = {"delete_message_days": delete_message_days, "reason": reason}
        return self._request(  # type: ignore[no-any-return]
            method="PUT",
            params={k: v for k, v in payload.items() if v is not None},
            uri=f"/guilds/{guild_id}/bans/{user_id}",
        )

    def remove_guild_ban(self: "Guild", guild_id: str, user_id: str) -> dict:
        """https://discord.com/developers/docs/resources/guild#remove-guild-ban"""
        return self._request(  # type: ignore[no-any-return]
            method="DELETE", uri=f"/guilds/{guild_id}/bans/{user_id}"
        )

    def get_guild_roles(self: "Guild", guild_id: str) -> dict:
        """https://discord.com/developers/docs/resources/guild#get-guild-roles"""
        return self._request(  # type: ignore[no-any-return]
            method="GET", uri=f"/guilds/{guild_id}/roles"
        )

    def create_guild_role(
        self: "Guild",
        guild_id: str,
        name: str,
        permissions: str,
        color: int = 0,
        hoist: bool = False,
        icon: Optional[Any] = None,
        unicode_emoji: Optional[str] = None,
        mentionable: bool = False,
    ) -> dict:
        """https://discord.com/developers/docs/resources/guild#create-guild-role"""
        payload: dict = {
            "name": name,
            "permissions": permissions,
            "color": color,
            "hoist": hoist,
            "icon": icon,
            "unicode_emoji": unicode_emoji,
            "mentionable": mentionable,
        }

        return self._request(  # type: ignore[no-any-return]
            method="POST",
            params={k: v for k, v in payload.items() if v is not None},
            uri=f"/guilds/{guild_id}/roles",
        )

    def modify_guild_role_permissions(
        self: "Guild", guild_id: str, id: str, position: Optional[int] = None
    ) -> dict:
        """https://discord.com/developers/docs/resources/guild#modify-guild-role-positions"""
        payload: dict = {"id": id, "position": position}
        return self._request(  # type: ignore[no-any-return]
            method="PATCH",
            params={k: v for k, v in payload.items() if v is not None},
            uri=f"/guilds/{guild_id}/roles",
        )

    def modify_guild_role(
        self: "Guild",
        guild_id: str,
        role_id: str,
        name: Optional[str] = None,
        permission: Optional[str] = None,
        color: Optional[int] = None,
        hoist: Optional[bool] = None,
        icon: Optional[Any] = None,
        unicode_emoji: Optional[str] = None,
        mentionable: Optional[bool] = None,
    ) -> dict:
        """https://discord.com/developers/docs/resources/guild#modify-guild-role"""
        payload: dict = {
            "name": name,
            "permission": permission,
            "color": color,
            "hoist": hoist,
            "icon": icon,
            "unicode_emoji": unicode_emoji,
            "mentionable": mentionable,
        }
        return self._request(  # type: ignore[no-any-return]
            method="PATCH",
            params={k: v for k, v in payload.items() if v is not None},
            uri=f"/guilds/{guild_id}/roles/{role_id}",
        )

    def delete_guild_role(self: "Guild", guild_id: str, role_id: str) -> dict:
        """https://discord.com/developers/docs/resources/guild#delete-guild-role"""
        return self._request(  # type: ignore[no-any-return]
            method="DELETE", uri=f"/guilds/{guild_id}/roles/{role_id}"
        )

    def get_guild_prune_count(
        self: "Guild", guild_id: str, days: int = 7, include_roles: Optional[str] = None
    ) -> dict:
        """https://discord.com/developers/docs/resources/guild#get-guild-prune-count"""
        payload: dict = {"days": days, "include_roles": include_roles}
        return self._request(  # type: ignore[no-any-return]
            method="GET",
            params={k: v for k, v in payload.items() if v is not None},
            uri=f"/guilds/{guild_id}/prune",
        )

    def beginn_guild_prune(
        self: "Guild",
        guild_id: str,
        days: int,
        compute_prune_count: bool,
        include_roles: str,
        reason: Optional[str] = None,
    ) -> dict:
        """https://discord.com/developers/docs/resources/guild#begin-guild-prune"""
        payload: dict = {
            "days": days,
            "compute_prune_count": compute_prune_count,
            "include_roles": include_roles,
            "reason": reason,
        }
        return self._request(  # type: ignore[no-any-return]
            method="POST",
            params={k: v for k, v in payload.items() if v is not None},
            uri=f"/guilds/{guild_id}/prune",
        )

    def get_guild_voice_regions(self: "Guild", guild_id: str) -> dict:
        """https://discord.com/developers/docs/resources/guild#get-guild-voice-regions"""
        return self._request(  # type: ignore[no-any-return]
            method="GET", uri=f"/guilds/{guild_id}/regions"
        )

    def get_guild_invites(self: "Guild", guild_id: str) -> dict:
        """https://discord.com/developers/docs/resources/guild#get-guild-invites"""
        return self._request(  # type: ignore[no-any-return]
            method="GET", uri=f"/guilds/{guild_id}/invites"
        )

    def get_guild_integrations(self: "Guild", guild_id: str) -> dict:
        """https://discord.com/developers/docs/resources/guild#get-guild-integrations"""
        return self._request(  # type: ignore[no-any-return]
            method="GET", uri=f"/guilds/{guild_id}/integrations"
        )

    def delete_guild_integrations(
        self: "Guild", guild_id: str, integration_id: str
    ) -> dict:
        """https://discord.com/developers/docs/resources/guild#delete-guild-integration"""
        return self._request(  # type: ignore[no-any-return]
            method="DELETE", uri=f"/guilds/{guild_id}/integrations/{integration_id}"
        )

    def get_guild_widget_settings(self: "Guild", guild_id: str) -> dict:
        """https://discord.com/developers/docs/resources/guild#get-guild-widget-settings"""
        return self._request(  # type: ignore[no-any-return]
            method="DELETE", uri=f"/guilds/{guild_id}/widget"
        )

    def modify_guild_widget(self: "Guild", guild_id: str, settings: dict) -> dict:
        """https://discord.com/developers/docs/resources/guild#modify-guild-widget"""
        return self._request(  # type: ignore[no-any-return]
            method="PATCH", params=settings, uri=f"/guilds/{guild_id}/widget"
        )

    def get_guild_widget(self: "Guild", guild_id: str) -> dict:
        """https://discord.com/developers/docs/resources/guild#get-guild-widget"""
        return self._request(  # type: ignore[no-any-return]
            method="GET", uri=f"/guilds/{guild_id}/widget.json"
        )

    def get_guild_vanity_url(self: "Guild", guild_id: str) -> dict:
        """https://discord.com/developers/docs/resources/guild#get-guild-vanity-url"""
        return self._request(  # type: ignore[no-any-return]
            method="GET", uri=f"/guilds/{guild_id}/vanity-url"
        )

    def get_guild_widget_image(self: "Guild", guild_id: str, style: str) -> dict:
        """https://discord.com/developers/docs/resources/guild#get-guild-widget-image
        @param style can be one of : [shield, banner1, banner2, banner3, banner4]
        """
        return self._request(  # type: ignore[no-any-return]
            method="GET",
            uri=f"/guilds/{guild_id}/widget.png",
            params={"style": style},
        )

    def get_guild_welcome_screen(self: "Guild", guild_id: str) -> dict:
        """https://discord.com/developers/docs/resources/guild#get-guild-welcome-screen"""
        return self._request(  # type: ignore[no-any-return]
            method="GET", uri=f"/guilds/{guild_id}/welcome-screen"
        )

    def modify_guild_welcome_screen(
        self: "Guild",
        guild_id: str,
        enabled: Optional[bool] = None,
        welcome_channels: Optional[list] = None,
        description: Optional[str] = None,
    ) -> dict:
        """https://discord.com/developers/docs/resources/guild#modify-guild-welcome-screen"""
        payload: dict = {
            "enabled": enabled,
            "welcome_channels": welcome_channels,
            "description": description,
        }
        return self._request(  # type: ignore[no-any-return]
            method="PATCH",
            params={k: v for k, v in payload.items() if v is not None},
            uri=f"/guilds/{guild_id}/welcome-screen",
        )

    def modify_current_user_voice_state(
        self: "Guild",
        guild_id: str,
        channel_id: str,
        suppress: Optional[bool] = None,
        request_to_speak_timestamp: Optional[Any] = None,
    ) -> dict:
        """https://discord.com/developers/docs/resources/guild#modify-current-user-voice-state"""
        payload: dict = {
            "channel_id": channel_id,
            "suppress": suppress,
            "request_to_speak_timestamp": request_to_speak_timestamp,
        }
        return self._request(  # type: ignore[no-any-return]
            method="PATCH",
            params={k: v for k, v in payload.items() if v is not None},
            uri=f"/guilds/{guild_id}/voice-states/@me",
        )

    def modify_user_voice_state(
        self: "Guild",
        guild_id: str,
        user_id: str,
        channel_id: str,
        suppress: Optional[bool] = None,
    ) -> dict:
        """https://discord.com/developers/docs/resources/guild#modify-user-voice-state"""
        payload: dict = {"channel_id": channel_id, "suppress": suppress}
        return self._request(  # type: ignore[no-any-return]
            method="PATCH",
            params={k: v for k, v in payload.items() if v is not None},
            uri=f"/guilds/{guild_id}/voice-states/{user_id}e",
        )

    def get_guild_audit_log(
        self: "Guild",
        guild_id: str,
        user_id: str,
        action_type: int,
        before: Optional[Any] = None,
        limit: int = 50,
    ) -> dict:
        """https://discord.com/developers/docs/resources/audit-log#get-guild-audit-log"""
        payload: dict = {
            "user_id": user_id,
            "action_type": action_type,
            "before": before,
            "limit": limit,
        }
        return self._request(  # type: ignore[no-any-return]
            "GET",
            params={k: v for k, v in payload.items() if v is not None},
            uri=f"/guilds/{guild_id}/audit-logs",
        )

    # -----======= S H E D U L E D - E V E N T S =======-----
    def list_scheduled_events_for_guild(
        self: "Guild", guild_id: str, with_user_count: Optional[bool] = None
    ) -> dict:
        """https://discord.com/developers/docs/resources/guild-scheduled-event#list-scheduled-events-for-guild"""
        payload: dict = {"with_user_count": with_user_count}
        return self._request(  # type: ignore[no-any-return]
            "GET",
            params={k: v for k, v in payload.items() if v is not None},
            uri=f"/guilds/{guild_id}/scheduled-events",
        )

    def create_guild_scheduled_event(
        self: "Guild",
        guild_id: str,
        name: str,
        entity_type: Any,
        privacy_level: Any,
        scheduled_start_time: Any,
        scheduled_end_time: Any,
        channel_id: Optional[Any] = None,
        entity_metadata: Optional[Any] = None,
        description: Optional[str] = None,
        image: Optional[Any] = None,
    ) -> dict:
        """https://discord.com/developers/docs/resources/guild-scheduled-event#create-guild-scheduled-event"""
        payload: dict = {
            "name": name,
            "entity_type": entity_type,
            "privacy_level": privacy_level,
            "scheduled_start_time": scheduled_start_time,
            "scheduled_end_time": scheduled_end_time,
            "channel_id": channel_id,
            "entity_metadata": entity_metadata,
            "description": description,
            "image": image,
        }
        return self._request(  # type: ignore[no-any-return]
            "POST",
            params={k: v for k, v in payload.items() if v is not None},
            uri=f"/guilds/{guild_id}/scheduled-events",
        )

    def get_guild_scheduled_event(
        self: "Guild",
        guild_id: str,
        guild_scheduled_event_id: str,
        with_user_count: Optional[bool] = None,
    ) -> dict:
        """https://discord.com/developers/docs/resources/guild-scheduled-event#get-guild-scheduled-event"""
        payload: dict = {"with_user_count": with_user_count}
        return self._request(  # type: ignore[no-any-return]
            "GET",
            params={k: v for k, v in payload.items() if v is not None},
            uri=f"/guilds/{guild_id}/scheduled-events/{guild_scheduled_event_id}",
        )

    def modify_guild_scheduled_event(
        self: "Guild",
        guild_id: str,
        guild_scheduled_event_id: str,
        channel_id: Optional[Any] = None,
        entity_metadata: Optional[Any] = None,
        name: Optional[str] = None,
        privacy_level: Optional[Any] = None,
        scheduled_start_time: Optional[Any] = None,
        scheduled_end_time: Optional[Any] = None,
        description: Optional[str] = None,
        entity_type: Optional[Any] = None,
        status: Optional[Any] = None,
        image: Optional[Any] = None,
    ) -> dict:
        """https://discord.com/developers/docs/resources/guild-scheduled-event#modify-guild-scheduled-event"""
        payload: dict = {
            "channel_id": channel_id,
            "entity_metadata": entity_metadata,
            "name": name,
            "privacy_level": privacy_level,
            "scheduled_start_time": scheduled_start_time,
            "scheduled_end_time": scheduled_end_time,
            "description": description,
            "entity_type": entity_type,
            "status": status,
            "image": image,
        }
        return self._request(  # type: ignore[no-any-return]
            "PATCH",
            params={k: v for k, v in payload.items() if v is not None},
            uri=f"/guilds/{guild_id}/scheduled-events/{guild_scheduled_event_id}",
        )

    def delete_guild_scheduled_evend(
        self: "Guild", guild_id: str, guild_scheduled_event_id: str
    ) -> dict:
        """https://discord.com/developers/docs/resources/guild-scheduled-event#delete-guild-scheduled-event"""
        return self._request(  # type: ignore[no-any-return]
            "DELETE",
            uri=f"/guilds/{guild_id}/scheduled-events/{guild_scheduled_event_id}",
        )

    def get_guild_scheduled_event_users(
        self: "Guild",
        guild_id: str,
        guild_scheduled_event_id: str,
        limit: Optional[int] = None,
        with_member: Optional[bool] = None,
        before: Optional[Any] = None,
        after: Optional[Any] = None,
    ) -> dict:
        """https://discord.com/developers/docs/resources/guild-scheduled-event#get-guild-scheduled-event-users"""
        payload: dict = {
            "limit": limit,
            "with_member": with_member,
            "before": before,
            "after": after,
        }
        return self._request(  # type: ignore[no-any-return]
            "GET",
            params={k: v for k, v in payload.items() if v is not None},
            uri=f"/guilds/{guild_id}/scheduled-events/{guild_scheduled_event_id}/users",
        )

    # -----======= T E M P L A T E S =======-----
    def get_guild_template(self: "Guild", template_code: str) -> dict:
        """https://discord.com/developers/docs/resources/guild-template#get-guild-template"""
        return self._request(  # type: ignore[no-any-return]
            "GET", uri=f"/guilds/templates/{template_code}"
        )

    def create_guild_from_template(
        self: "Guild", template_code: str, name: str, icon: Optional[Any] = None
    ) -> dict:
        """https://discord.com/developers/docs/resources/guild-template#create-guild-from-guild-template"""
        payload: dict = {"name": name, "icon": icon}
        return self._request(  # type: ignore[no-any-return]
            "POST",
            uri=f"/guilds/templates/{template_code}",
            params={k: v for k, v in payload.items() if v is not None},
        )

    def get_guild_templates(self: "Guild", guild_id: str) -> dict:
        """https://discord.com/developers/docs/resources/guild-template#get-guild-templates"""
        return self._request(  # type: ignore[no-any-return]
            "GET", uri=f"/guilds/{guild_id}/templates"
        )

    def create_guild_template(
        self: "Guild", guild_id: str, name: str, description: Optional[str] = None
    ) -> dict:
        """https://discord.com/developers/docs/resources/guild-template#create-guild-template"""
        payload: dict = {"name": name, "description": description}
        return self._request(  # type: ignore[no-any-return]
            "POST",
            params={k: v for k, v in payload.items() if v is not None},
            uri=f"/guilds/{guild_id}/templates",
        )

    def sync_guild_template(self: "Guild", guild_id: str, template_code: str) -> dict:
        """https://discord.com/developers/docs/resources/guild-template#sync-guild-template"""
        return self._request(  # type: ignore[no-any-return]
            "PUT", uri=f"/guilds/{guild_id}/templates/{template_code}"
        )

    def modify_guild_template(
        self: "Guild",
        template_code: str,
        guild_id: str,
        name: str = None,
        description: Optional[str] = None,
    ) -> dict:
        """https://discord.com/developers/docs/resources/guild-template#modify-guild-template"""
        payload: dict = {"name": name, "description": description}
        return self._request(  # type: ignore[no-any-return]
            "PATCH",
            params={k: v for k, v in payload.items() if v is not None},
            uri=f"/guilds/{guild_id}/templates/{template_code}",
        )

    def delete_guild_template(self: "Guild", guild_id: str, template_code: str) -> dict:
        """https://discord.com/developers/docs/resources/guild-template#delete-guild-template"""
        return self._request(  # type: ignore[no-any-return]
            "DELETE", uri=f"/guilds/{guild_id}/templates/{template_code}"
        )

    # -----======= E M O J I =======-----
    def list_guild_emojis(self: "Guild", guild_id: str) -> dict:
        """https://discord.com/developers/docs/resources/emoji#list-guild-emojis"""
        return self._request(  # type: ignore[no-any-return]
            "GET", uri=f"/guilds/{guild_id}/emojis"
        )

    def get_guild_emoji(self: "Guild", guild_id: str, emoji_id: str) -> dict:
        """https://discord.com/developers/docs/resources/emoji#get-guild-emoji"""
        return self._request(  # type: ignore[no-any-return]
            "GET", uri=f"/guilds/{guild_id}/emojis/{emoji_id}"
        )

    def create_guild_emoji(
        self: "Guild", guild_id: str, name: str, image: Any, roles: list
    ) -> dict:
        """https://discord.com/developers/docs/resources/emoji#create-guild-emoji"""
        return self._request(  # type: ignore[no-any-return]
            "POST",
            params={"name": name, "image": image, "roles": roles},
            uri=f"/guilds/{guild_id}/emojis",
        )

    def modify_guild_emoji(
        self: "Guild",
        guild_id: str,
        emoji_id: str,
        name: Optional[str] = None,
        roles: Optional[list] = None,
    ) -> dict:
        """https://discord.com/developers/docs/resources/emoji#modify-guild-emoji"""
        payload: dict = {"name": name, "roles": roles}
        return self._request(  # type: ignore[no-any-return]
            "PATCH",
            params={k: v for k, v in payload.items() if v is not None},
            uri=f"/guilds/{guild_id}/emojis/{emoji_id}",
        )

    def delete_guild_emoji(self: "Guild", guild_id: str, emoji_id: str) -> dict:
        """https://discord.com/developers/docs/resources/emoji#delete-guild-emoji"""
        return self._request(  # type: ignore[no-any-return]
            "DELETE", uri=f"/guilds/{guild_id}/emojis/{emoji_id}"
        )

    # -----======= S T I C K E R  =======-----
    def get_sticker(self: "Guild", sticker_id: str) -> dict:
        """https://discord.com/developers/docs/resources/sticker#get-sticker"""
        return self._request(  # type: ignore[no-any-return]
            "GET", uri=f"/stickers/{sticker_id}"
        )

    def list_nitro_sticker_packs(self: "Guild") -> dict:
        """https://discord.com/developers/docs/resources/sticker#list-nitro-sticker-packs"""
        return self._request("GET", uri="/sticker-packs")  # type: ignore[no-any-return]

    def list_guild_stickers(self: "Guild", guild_id: str) -> dict:
        """https://discord.com/developers/docs/resources/sticker#list-guild-stickers"""
        return self._request(  # type: ignore[no-any-return]
            "GET", uri=f"/guilds/{guild_id}/stickers"
        )

    def get_guild_sticker(self: "Guild", guild_id: str, sticker_id: str) -> dict:
        """https://discord.com/developers/docs/resources/sticker#get-guild-sticker"""
        return self._request(  # type: ignore[no-any-return]
            "GET", uri=f"/guilds/{guild_id}/stickers/{sticker_id}"
        )

    def create_guild_sticker(
        self: "Guild", guild_id: str, name: str, description: str, tags: str, file: Any
    ) -> dict:
        """https://discord.com/developers/docs/resources/sticker#create-guild-sticker"""
        payload: dict = {
            "name": name,
            "description": description,
            "tags": tags,
            "file": file,
        }
        return self._request(  # type: ignore[no-any-return]
            "POST",
            params={k: v for k, v in payload.items() if v is not None},
            uri=f"/guilds/{guild_id}/stickers",
        )

    def modify_guild_sticker(
        self: "Guild",
        guild_id: str,
        sticker_id: str,
        name: Optional[str] = None,
        description: Optional[str] = None,
        tags: Optional[str] = None,
    ) -> dict:
        """https://discord.com/developers/docs/resources/sticker#modify-guild-sticker"""
        payload: dict = {"name": name, "description": description, "tags": tags}
        return self._request(  # type: ignore[no-any-return]
            "PATCH",
            params={k: v for k, v in payload.items() if v is not None},
            uri=f"/guilds/{guild_id}/stickers/{sticker_id}",
        )

    def delete_guild_sticker(self: "Guild", guild_id: str, sticker_id: str) -> dict:
        """https://discord.com/developers/docs/resources/sticker#delete-guild-sticker"""
        return self._request(  # type: ignore[no-any-return]
            "DELETE", uri=f"/guilds/{guild_id}/stickers/{sticker_id}"
        )
