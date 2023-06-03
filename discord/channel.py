# -*- coding: utf-8 -*-


"""Module that implements the REST channel related functions."""

from typing import Any, List, Optional

from discord.base_request import BaseRequestAPI


class Channel(BaseRequestAPI):
    """Contains a collection of channel related methods."""

    def get_channel(self: "Channel", channel_id: str) -> dict:
        """https://discord.com/developers/docs/resources/channel#get-channel"""
        return self._request(  # type: ignore[no-any-return]
            "GET", uri=f"/channels/{channel_id}"
        )

    def modify_channel(
        self: "Channel",
        channel_id: str,
        name: Optional[str] = None,
        icon: Optional[Any] = None,
        type_: Optional[int] = None,
        position: Optional[int] = None,
        topic: Optional[str] = None,
        nsfw: Optional[bool] = None,
        rate_limit_per_user: Optional[int] = None,
        bitrate: Optional[int] = None,
        user_limit: Optional[int] = None,
        permission_overwrites: Optional[list] = None,
        parent_id: Optional[str] = None,
        rtc_region: Optional[str] = None,
        video_quality_mode: Optional[int] = None,
        default_auto_archive_duration: Optional[int] = None,
        archived: Optional[bool] = None,
        auto_archive_duration: int = None,
        locked: Optional[bool] = None,
        invitable: Optional[bool] = None,
        **kwargs: Any,
    ) -> dict:
        """https://discord.com/developers/docs/resources/channel#modify-channel"""
        payload: dict = {
            "name": name,
            "icon": icon,
            "type": type_,
            "topic": topic,
            "nsfw": nsfw,
            "position": position,
            "rate_limit_per_user": rate_limit_per_user,
            "bitrate": bitrate,
            "user_limit": user_limit,
            "permission_overwrites": permission_overwrites,
            "parent_id": parent_id,
            "rtc_region": rtc_region,
            "video_quality_mode": video_quality_mode,
            "default_auto_archive_duration": default_auto_archive_duration,
            "archived": archived,
            "auto_archive_duration": auto_archive_duration,
            "locked": locked,
            "invitable": invitable,
        }
        payload = {k: v for k, v in payload.items() if v is not None}
        payload.update(kwargs)
        return self._request(  # type: ignore[no-any-return]
            "PATCH", params=payload, uri=f"/channels/{channel_id}"
        )

    def delete_close_channel(self: "Channel", channel_id: str) -> dict:
        """https://discord.com/developers/docs/resources/channel#deleteclose-channel"""
        return self._request(  # type: ignore[no-any-return]
            "DELETE", uri=f"/channels/{channel_id}"
        )

    def get_channel_messages(
        self: "Channel",
        channel_id: str,
        around: Optional[str] = None,
        before: Optional[str] = None,
        after: Optional[str] = None,
        limit: Optional[int] = None,
    ) -> dict:
        """https://discord.com/developers/docs/resources/channel#get-channel-messages"""
        payload: dict = {
            "around": around,
            "before": before,
            "after": after,
            "limit": limit,
        }
        payload = {k: v for k, v in payload.items() if v is not None}
        return self._request(  # type: ignore[no-any-return]
            "GET", params=payload, uri=f"/channels/{channel_id}/messages"
        )

    def get_channel_message(self: "Channel", channel_id: str) -> dict:
        """https://discord.com/developers/docs/resources/channel#get-channel-message"""
        return self._request(  # type: ignore[no-any-return]
            "GET", uri=f"/channels/{channel_id}/messages"
        )

    def create_message(
        self: "Channel",
        channel_id: str,
        content: Optional[str] = None,
        tts: Optional[bool] = None,
        embeds: Optional[Any] = None,
        allowed_mentions: Optional[Any] = None,
        message_reference: Optional[Any] = None,
        components: Optional[list] = None,
        files: Optional[Any] = None,
        attachments: Optional[Any] = None,
        sticker_ids: Optional[list] = None,
        flags: Optional[int] = None,
    ) -> dict:
        """https://discord.com/developers/docs/resources/channel#create-message"""

        payload: dict = {
            "content": content,
            "tts": tts,
            "allowed_mentions": allowed_mentions,
            "message_reference": message_reference,
            "components": components,
            "sticker_ids": sticker_ids,
            "flags": flags,
            "embeds": embeds,
            "attachments": attachments,
        }
        payload = {k: v for k, v in payload.items() if v is not None}
        uri: str = f"/channels/{channel_id}/messages"
        if files is not None:
            return self._send_file_attachment(  # type: ignore[no-any-return]
                method="POST", uri=uri, file_names=files, payload=payload
            )
        return self._request(  # type: ignore[no-any-return]
            method="POST", uri=uri, params=payload
        )

    def crosspost_message(self: "Channel", message_id: str, channel_id: str) -> dict:
        """https://discord.com/developers/docs/resources/channel#crosspost-message"""
        return self._request(  # type: ignore[no-any-return]
            "POST", uri=f"/channels/{channel_id}/messages/{message_id}/crosspost"
        )

    def create_reaction(
        self: "Channel", channel_id: str, message_id: str, emoji: str
    ) -> dict:
        """https://discord.com/developers/docs/resources/channel#create-reaction
        "The emoji must be URL Encoded or the request will fail with 10014: Unknown Emoji.
        To use custom emoji, you must encode it in the format name:id with the emoji name and emoji id."
        """
        return self._request(  # type: ignore[no-any-return]
            "PUT",
            uri=f"/channels/{channel_id}/messages/{message_id}/reactions/{emoji}/@me",
        )

    def delete_own_reaction(
        self: "Channel", channel_id: str, message_id: str, emoji: str
    ) -> dict:
        """https://discord.com/developers/docs/resources/channel#delete-own-reaction
        "The emoji must be URL Encoded or the request will fail with 10014: Unknown Emoji.
        To use custom emoji, you must encode it in the format name:id with the emoji name and emoji id."
        """
        return self._request(  # type: ignore[no-any-return]
            "DELETE",
            uri=f"/channels/{channel_id}/messages/{message_id}/reactions/{emoji}/@me",
        )

    def delete_user_reaction(
        self: "Channel", channel_id: str, message_id: str, user_id: str, emoji: str
    ) -> dict:
        """https://discord.com/developers/docs/resources/channel#delete-user-reaction
        "The emoji must be URL Encoded or the request will fail with 10014: Unknown Emoji.
        To use custom emoji, you must encode it in the format name:id with the emoji name and emoji id."
        """
        return self._request(  # type: ignore[no-any-return]
            "DELETE",
            uri=f"/channels/{channel_id}/messages/{message_id}/reactions/{emoji}/{user_id}",
        )

    def get_reactions(
        self: "Channel",
        channel_id: str,
        message_id: str,
        emoji: str,
        after: Optional[Any] = None,
        limit: Optional[int] = None,
    ) -> dict:
        """https://discord.com/developers/docs/resources/channel#get-reactions
        "The emoji must be URL Encoded or the request will fail with 10014: Unknown Emoji.
        To use custom emoji, you must encode it in the format name:id with the emoji name and emoji id."
        """
        payload: dict = {}
        if after is not None:
            payload["after"] = after
        if limit is not None:
            payload["limit"] = limit

        return self._request(  # type: ignore[no-any-return]
            "GET",
            uri=f"/channels/{channel_id}/messages/{message_id}/reactions/{emoji}",
            params=payload,
        )

    def delete_all_reactions(self: "Channel", channel_id: str, message_id: str) -> dict:
        """https://discord.com/developers/docs/resources/channel#delete-all-reactions"""
        return self._request(  # type: ignore[no-any-return]
            "DELETE", uri=f"/channels/{channel_id}/messages/{message_id}/reactions"
        )

    def delete_all_reactions_for_emoji(
        self: "Channel", channel_id: str, message_id: str, emoji: str
    ) -> dict:
        """https://discord.com/developers/docs/resources/channel#delete-all-reactions-for-emoji
        "The emoji must be URL Encoded or the request will fail with 10014: Unknown Emoji.
        To use custom emoji, you must encode it in the format name:id with the emoji name and emoji id."
        """
        return self._request(  # type: ignore[no-any-return]
            "DELETE",
            uri=f"/channels/{channel_id}/messages/{message_id}/reactions/{emoji}",
        )

    def edit_message(
        self: "Channel",
        channel_id: str,
        message_id: str,
        content: Optional[str] = None,
        embeds: Optional[List[dict]] = None,
        flags: Optional[int] = None,
        allowed_mentions: Optional[Any] = None,
        components: Optional[list] = None,
        files: Optional[Any] = None,
        payload_json: Optional[str] = None,
        attachments: Optional[list] = None,
        **kwargs: Any,
    ) -> dict:
        """https://discord.com/developers/docs/resources/channel#edit-message"""
        payload: dict = {
            "content": content,
            "flags": flags,
            "allowed_mentions": allowed_mentions,
            "components": components,
            "payload_json": payload_json,
            "attachments": attachments,
            "embeds": embeds,
        }
        payload = {k: v for k, v in payload.items() if v is not None}
        payload.update(kwargs)
        uri: str = f"/channels/{channel_id}/messages/{message_id}"
        if files is not None:
            return self._send_file_attachment(  # type: ignore[no-any-return]
                method="POST", uri=uri, file_names=files, payload=payload
            )
        return self._request(  # type: ignore[no-any-return]
            method="POST", uri=uri, params=payload
        )

    def delete_message(self: "Channel", channel_id: str, message_id: str) -> dict:
        """https://discord.com/developers/docs/resources/channel#delete-message"""
        return self._request(  # type: ignore[no-any-return]
            "DELETE", uri=f"/channels/{channel_id}/messages/{message_id}"
        )

    def bulk_delete_message(self: "Channel", channel_id: str, messages: list) -> dict:
        """https://discord.com/developers/docs/resources/channel#bulk-delete-messages"""
        return self._request(  # type: ignore[no-any-return]
            "POST",
            params={"messages": messages},
            uri=f"/channels/{channel_id}/messages/bulk-delete",
        )

    def edit_channel_permissions(
        self: "Channel",
        channel_id: str,
        overwrite_id: str,
        allow: Optional[Any] = None,
        deny: Optional[Any] = None,
        type_: Optional[int] = None,
    ) -> dict:
        """https://discord.com/developers/docs/resources/channel#edit-channel-permissions"""
        payload: dict = {"allow": allow, "deny": deny, "type": type_}
        return self._request(  # type: ignore[no-any-return]
            "PUT",
            params={k: v for k, v in payload.items() if v is not None},
            uri=f"/channels/{channel_id}/permissions/{overwrite_id}",
        )

    def get_channel_invites(self: "Channel", channel_id: str) -> dict:
        """https://discord.com/developers/docs/resources/channel#get-channel-invites"""
        return self._request(  # type: ignore[no-any-return]
            "GET", uri=f"/channels/{channel_id}/invites"
        )

    def create_channel_invite(
        self: "Channel",
        channel_id: str,
        max_age: Optional[int] = None,
        max_uses: Optional[int] = None,
        temporary: Optional[bool] = None,
        unique: Optional[bool] = None,
        target_type: Optional[int] = None,
        target_user_id: Optional[Any] = None,
        target_application_id: Optional[Any] = None,
    ) -> dict:
        """https://discord.com/developers/docs/resources/channel#create-channel-invite"""
        payload: dict = {
            "max_age": max_age,
            "max_uses": max_uses,
            "temporary": temporary,
            "unique": unique,
            "target_type": target_type,
            "target_user_id": target_user_id,
            "target_application_id": target_application_id,
        }
        return self._request(  # type: ignore[no-any-return]
            "POST",
            params={k: v for k, v in payload.items() if v is not None},
            uri=f"/channels/{channel_id}/invites",
        )

    def delete_channel_permission(
        self: "Channel", channel_id: str, overwrite_id: str
    ) -> dict:
        """https://discord.com/developers/docs/resources/channel#delete-channel-permission"""
        return self._request(  # type: ignore[no-any-return]
            "DELETE", uri=f"/channels/{channel_id}/permissions/{overwrite_id}"
        )

    def follow_news_channel(
        self: "Channel", channel_id: str, webhook_channel_id: str
    ) -> dict:
        """https://discord.com/developers/docs/resources/channel#follow-news-channel"""
        return self._request(  # type: ignore[no-any-return]
            "POST",
            params={"webhook_channel_id": webhook_channel_id},
            uri=f"/channels/{channel_id}/followers",
        )

    def trigger_typing_indicatoe(self: "Channel", channel_id: str) -> dict:
        """https://discord.com/developers/docs/resources/channel#trigger-typing-indicator"""
        return self._request(  # type: ignore[no-any-return]
            "POST", uri=f"/channels/{channel_id}/typing"
        )

    def get_pinned_message(self: "Channel", channel_id: str) -> dict:
        """https://discord.com/developers/docs/resources/channel#get-pinned-messages"""
        return self._request(  # type: ignore[no-any-return]
            "GET", uri=f"/channels/{channel_id}/pins"
        )

    def pin_message(self: "Channel", channel_id: str, message_id: str) -> dict:
        """https://discord.com/developers/docs/resources/channel#pin-message"""
        return self._request(  # type: ignore[no-any-return]
            "PUT", uri=f"/channels/{channel_id}/pins/{message_id}"
        )

    def unpin_message(self: "Channel", channel_id: str, message_id: str) -> dict:
        """https://discord.com/developers/docs/resources/channel#unpin-message"""
        return self._request(  # type: ignore[no-any-return]
            "DELETE", uri=f"/channels/{channel_id}/pins/{message_id}"
        )

    def group_dm_add_recipient(
        self: "Channel", channel_id: str, user_id: str, access_token: str, nick: str
    ) -> dict:
        """https://discord.com/developers/docs/resources/channel#group-dm-add-recipient"""
        payload: dict = {"access_token": access_token, "nick": nick}
        return self._request(  # type: ignore[no-any-return]
            "PUT",
            params={k: v for k, v in payload.items() if v is not None},
            uri=f"/channels/{channel_id}/recipients/{user_id}",
        )

    def group_dm_remove_recipient(
        self: "Channel", channel_id: str, user_id: str
    ) -> dict:
        """https://discord.com/developers/docs/resources/channel#group-dm-remove-recipient"""
        return self._request(  # type: ignore[no-any-return]
            "DELETE", uri=f"/channels/{channel_id}/recipients/{user_id}"
        )

    def start_thread_with_message(
        self: "Channel",
        channel_id: str,
        message_id: str,
        name: str,
        auto_archive_duration: Optional[int] = None,
        rate_limit_per_user: Optional[int] = None,
    ) -> dict:
        """https://discord.com/developers/docs/resources/channel#start-thread-from-message"""
        payload: dict = {
            "name": name,
            "auto_archive_duration": auto_archive_duration,
            "rate_limit_per_user": rate_limit_per_user,
        }
        return self._request(  # type: ignore[no-any-return]
            "POST",
            params={k: v for k, v in payload.items() if v is not None},
            uri=f"/channels/{channel_id}/messages/{message_id}/threads",
        )

    def start_thread_without_message(
        self: "Channel",
        channel_id: str,
        name: str,
        auto_archive_duration: Optional[str] = None,
        type_: Optional[int] = None,
        invitable: Optional[bool] = None,
        rate_limit_per_user: Optional[int] = None,
    ) -> dict:
        """https://discord.com/developers/docs/resources/channel#start-thread-without-message"""
        payload: dict = {
            "name": name,
            "auto_archive_duration": auto_archive_duration,
            "type": type_,
            "invitable": invitable,
            "rate_limit_per_user": rate_limit_per_user,
        }
        return self._request(  # type: ignore[no-any-return]
            "POST",
            params={k: v for k, v in payload.items() if v is not None},
            uri=f"/channels/{channel_id}/threads",
        )

    def join_thread(self: "Channel", channel_id: str) -> dict:
        """https://discord.com/developers/docs/resources/channel#join-thread"""
        return self._request(  # type: ignore[no-any-return]
            "PUT", uri=f"/channels/{channel_id}/thread-members/@me"
        )

    def add_thread_member(self: "Channel", channel_id: str, user_id: str) -> dict:
        """https://discord.com/developers/docs/resources/channel#add-thread-member"""
        return self._request(  # type: ignore[no-any-return]
            "PUT", uri=f"/channels/{channel_id}/thread-members/{user_id}"
        )

    def leave_thread(self: "Channel", channel_id: str) -> dict:
        """https://discord.com/developers/docs/resources/channel#leave-thread"""
        return self._request(  # type: ignore[no-any-return]
            "DELETE", uri=f"/channels/{channel_id}/thread-members/@me"
        )

    def remove_thread_member(self: "Channel", channel_id: str, user_id: str) -> dict:
        """https://discord.com/developers/docs/resources/channel#remove-thread-member"""
        return self._request(  # type: ignore[no-any-return]
            "DELETE", uri=f"/channels/{channel_id}/thread-members/{user_id}"
        )

    def get_thread_member(self: "Channel", channel_id: str, user_id: str) -> dict:
        """https://discord.com/developers/docs/resources/channel#get-thread-member"""
        return self._request(  # type: ignore[no-any-return]
            "GET", uri=f"/channels/{channel_id}/thread-members/{user_id}"
        )

    def list_thread_member(self: "Channel", channel_id: str) -> dict:
        """https://discord.com/developers/docs/resources/channel#list-thread-members"""
        return self._request(  # type: ignore[no-any-return]
            "GET", uri=f"/channels/{channel_id}/thread-members"
        )

    def list_active_threads(
        self: "Channel", channel_id: str, threads: list, members: list, has_more: bool
    ) -> dict:
        """https://discord.com/developers/docs/resources/channel#list-active-threads"""
        return self._request(  # type: ignore[no-any-return]
            "GET",
            params={"threads": threads, "members": members, "has_more": has_more},
            uri=f"/channels/{channel_id}/threads/active",
        )

    def list_public_archived_threads(
        self: "Channel",
        channel_id: str,
        before: Optional[Any] = None,
        limit: Optional[int] = None,
    ) -> dict:
        """https://discord.com/developers/docs/resources/channel#list-public-archived-threads"""
        payload: dict = {"before": before, "limit": limit}
        return self._request(  # type: ignore[no-any-return]
            "GET",
            params={k: v for k, v in payload.items() if v is not None},
            uri=f"/channels/{channel_id}/threads/archived/public",
        )

    def list_private_archived_threads(
        self: "Channel",
        channel_id: str,
        before: Optional[Any] = None,
        limit: Optional[int] = None,
    ) -> dict:
        """https://discord.com/developers/docs/resources/channel#list-private-archived-threads"""
        payload: dict = {"before": before, "limit": limit}
        return self._request(  # type: ignore[no-any-return]
            "GET",
            params={k: v for k, v in payload.items() if v is not None},
            uri=f"/channels/{channel_id}/threads/archived/private",
        )

    def list_joined_private_archived_threads(
        self: "Channel",
        channel_id: str,
        before: Optional[Any] = None,
        limit: Optional[int] = None,
    ) -> dict:
        """https://discord.com/developers/docs/resources/channel#list-joined-private-archived-threads"""
        payload: dict = {"before": before, "limit": limit}
        return self._request(  # type: ignore[no-any-return]
            "GET",
            params={k: v for k, v in payload.items() if v is not None},
            uri=f"/channels/{channel_id}/users/@me/threads/archived/private",
        )
