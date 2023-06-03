# -*- coding: utf-8 -*-


"""Module that implements the REST user related functions."""

from typing import Any, Optional

from discord.base_request import BaseRequestAPI


class User(BaseRequestAPI):
    """Contains a collection of user related methods."""

    def get_current_user(self: "User") -> dict:
        """https://discord.com/developers/docs/resources/user#get-current-user"""
        return self._request(  # type: ignore[no-any-return]
            method="GET", uri="/users/@me"
        )

    def get_user(self: "User", user_id: str) -> dict:
        """https://discord.com/developers/docs/resources/user#get-user"""
        return self._request(  # type: ignore[no-any-return]
            method="GET", uri=f"/users/{user_id}"
        )

    def modify_current_user(
        self: "User", username: Optional[str] = None, avatar: Optional[Any] = None
    ) -> dict:
        """https://discord.com/developers/docs/resources/user#modify-current-user"""
        payload: dict = {"username": username, "avatar": avatar}
        return self._request(  # type: ignore[no-any-return]
            method="PATCH",
            params={k: v for k, v in payload.items() if v is not None},
            uri="/users/@me",
        )

    def get_current_user_guilds(
        self: "User",
        before: Optional[Any] = None,
        after: Optional[Any] = None,
        limit: Optional[int] = None,
    ) -> dict:
        """https://discord.com/developers/docs/resources/user#get-current-user-guilds"""
        payload: dict = {
            "before": before,
            "after": after,
            "limit": limit,
        }
        return self._request(  # type: ignore[no-any-return]
            method="GET",
            params={k: v for k, v in payload.items() if v is not None},
            uri="/users/@me/guilds",
        )

    def get_current_user_guild_member(self: "User", guild_id: str) -> dict:
        """https://discord.com/developers/docs/resources/user#get-current-user-guild-member"""
        return self._request(  # type: ignore[no-any-return]
            method="GET", uri=f"/users/@me/guilds/{guild_id}/member"
        )

    def leave_guild(self: "User", guild_id: str) -> dict:
        """https://discord.com/developers/docs/resources/user#leave-guild"""
        return self._request(  # type: ignore[no-any-return]
            method="DELETE", uri=f"/users/@me/guilds/{guild_id}"
        )

    def create_dm(self: "User", recipient_id: str) -> dict:
        """https://discord.com/developers/docs/resources/user#create-dm"""
        payload: dict = {"recipient_id": recipient_id}
        return self._request(  # type: ignore[no-any-return]
            method="POST", params=payload, uri="/users/@me/channels"
        )

    def create_group_dm(self: "User", access_tokens: list, nicks: dict) -> dict:
        """https://discord.com/developers/docs/resources/user#create-group-dm"""
        payload: dict = {"access_tokens": access_tokens, "nicks": nicks}
        return self._request(  # type: ignore[no-any-return]
            method="POST", params=payload, uri="/users/@me/channels"
        )

    def get_user_connections(self: "User") -> dict:
        """https://discord.com/developers/docs/resources/user#get-user-connections"""
        return self._request(  # type: ignore[no-any-return]
            method="GET", uri="/users/@me/connections"
        )

    def list_voice_regions(self: "User") -> dict:
        """https://discord.com/developers/docs/resources/voice#list-voice-regions"""
        return self._request(  # type: ignore[no-any-return]
            method="GET", uri="/voice/regions"
        )

    def get_invite(
        self: "User",
        invite_code: str,
        with_counts: Optional[bool] = None,
        with_expiration: Optional[bool] = None,
        guild_scheduled_event_id: Optional[Any] = None,
    ) -> dict:
        """https://discord.com/developers/docs/resources/invite#get-invite"""
        payload: dict = {
            "with_counts": with_counts,
            "with_expiration": with_expiration,
            "guild_scheduled_event_id": guild_scheduled_event_id,
        }
        return self._request(  # type: ignore[no-any-return]
            method="GET",
            params={k: v for k, v in payload.items() if v is not None},
            uri=f"/invites/{invite_code}",
        )

    def delete_invite(self: "User", invite_code: str) -> dict:
        """https://discord.com/developers/docs/resources/invite#delete-invite"""
        return self._request(  # type: ignore[no-any-return]
            method="DELETE", uri=f"/invites/{invite_code}"
        )
