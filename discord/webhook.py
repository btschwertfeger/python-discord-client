# -*- coding: utf-8 -*-


"""Module that implements the REST webhook related functions."""

from typing import Any, Optional

from discord.base_request import BaseRequestAPI


class Webhook(BaseRequestAPI):
    """Contains a collection of webhook related methods."""

    def create_webhook(
        self: "Webhook", channel_id: str, name: str, avatar: Optional[Any] = None
    ) -> dict:
        """https://discord.com/developers/docs/resources/webhook#create-webhook"""
        payload: dict = {"name": name, "avatar": avatar}
        return self._request(  # type: ignore[no-any-return]
            "POST",
            params={k: v for k, v in payload.items() if v is not None},
            uri=f"/channels/{channel_id}/webhooks",
        )

    def get_channel_webhooks(self: "Webhook", channel_id: str) -> dict:
        """https://discord.com/developers/docs/resources/webhook#create-webhook"""
        return self._request(  # type: ignore[no-any-return]
            "GET", uri=f"/channels/{channel_id}/webhooks"
        )

    def get_guild_webhooks(self: "Webhook", guild_id: str) -> dict:
        """https://discord.com/developers/docs/resources/webhook#get-guild-webhooks"""
        return self._request(  # type: ignore[no-any-return]
            "GET", uri=f"/guilds/{guild_id}/webhooks"
        )

    def get_webhook(self: "Webhook", webhook_id: str) -> dict:
        """https://discord.com/developers/docs/resources/webhook#get-webhook"""
        return self._request(  # type: ignore[no-any-return]
            "GET", uri=f"/webhooks/{webhook_id}"
        )

    def get_webhook_with_token(
        self: "Webhook", webhook_id: str, webhook_token: str
    ) -> dict:
        """https://discord.com/developers/docs/resources/webhook#get-webhook-with-token"""
        return self._request(  # type: ignore[no-any-return]
            "GET", uri=f"/webhooks/{webhook_id}/{webhook_token}"
        )

    def modify_webhook(
        self: "Webhook",
        webhook_id: str,
        name: Optional[str] = None,
        avatar: Optional[Any] = None,
        channel_id: Optional[Any] = None,
    ) -> dict:
        """https://discord.com/developers/docs/resources/webhook#modify-webhook"""
        payload: dict = {"name": name, "avatar": avatar, "channel_id": channel_id}
        return self._request(  # type: ignore[no-any-return]
            "PATCH",
            params={k: v for k, v in payload.items() if v is not None},
            uri=f"/webhooks/{webhook_id}",
        )

    def modify_webhook_with_token(
        self: "Webhook",
        webhook_id: str,
        webhook_token: str,
        name: Optional[str] = None,
        avatar: Optional[str] = None,
    ) -> dict:
        """https://discord.com/developers/docs/resources/webhook#modify-webhook-with-token"""
        payload: dict = {"name": name, "avatar": avatar}
        return self._request(  # type: ignore[no-any-return]
            "PATCH",
            params={k: v for k, v in payload.items() if v is not None},
            uri=f"/webhooks/{webhook_id}/{webhook_token}",
        )

    def delete_webhook(self: "Webhook", webhook_id: str) -> dict:
        """https://discord.com/developers/docs/resources/webhook#delete-webhook"""
        return self._request(  # type: ignore[no-any-return]
            "DELETE", uri=f"/webhooks/{webhook_id}"
        )

    def delete_webhook_with_token(
        self: "Webhook", webhook_id: str, webhook_token: str
    ) -> dict:
        """https://discord.com/developers/docs/resources/webhook#delete-webhook-with-token"""
        return self._request(  # type: ignore[no-any-return]
            "DELETE", uri=f"/webhooks/{webhook_id}/{webhook_token}"
        )

    def execute_webhook(
        self: "Webhook",
        webhook_id: str,
        webhook_token: str,
        wait: bool = False,
        thread_id: Optional[Any] = None,
        content: Optional[str] = None,
        username: Optional[str] = None,
        avatar_url: Optional[str] = None,
        tts: Optional[bool] = None,
        embeds: Optional[list] = None,
        allowed_mentions: Optional[Any] = None,
        components: Optional[list] = None,
        files: Optional[Any] = None,
        payload_json: Optional[dict] = None,
        attachments: Optional[list] = None,
        flags: Optional[int] = None,
    ) -> dict:
        """https://discord.com/developers/docs/resources/webhook#execute-webhook
        ! Note that when sending a message, you must provide a value for at least one of content, embeds, or file.
        """
        payload: dict = {
            "content": content,
            "username": username,
            "avatar_url": avatar_url,
            "tts": tts,
            "allowed_mentions": allowed_mentions,
            "components": components,
            "files": files,
            "payload_json": payload_json,
            "attachments": attachments,
            "flags": flags,
            "embeds": embeds,
        }
        uri: str = f"/webhooks/{webhook_id}/{webhook_token}"
        if wait or thread_id is not None:
            uri = f"{uri}?{wait}&thread_id={thread_id}"
        return self._request(  # type: ignore[no-any-return]
            "POST", params={k: v for k, v in payload.items() if v is not None}, uri=uri
        )

    def execute_slack_compatible_webhook(self) -> dict:
        """https://discord.com/developers/docs/resources/webhook#execute-slackcompatible-webhook"""
        raise NotImplementedError()

    def execute_github_compatible_webhook(self) -> dict:
        """https://discord.com/developers/docs/resources/webhook#execute-githubcompatible-webhook"""
        raise NotImplementedError()

    def get_webhook_messages(
        self: "Webhook",
        webhook_id: str,
        webhook_token: str,
        message_id: str,
        thread_id: Optional[str] = None,
    ) -> dict:
        """https://discord.com/developers/docs/resources/webhook#get-webhook-message"""
        payload: dict = {"thread_id": thread_id}
        return self._request(  # type: ignore[no-any-return]
            "GET",
            params={k: v for k, v in payload.items() if v is not None},
            uri=f"/webhooks/{webhook_id}/{webhook_token}/messages/{message_id}",
        )

    def edit_webhook_messages(self: "Webhook") -> dict:
        """https://discord.com/developers/docs/resources/webhook#edit-webhook-message"""
        raise NotImplementedError()

    def delete_webhook_messages(
        self: "Webhook", webhook_id: str, webhook_token: str, message_id: str
    ) -> dict:
        """https://discord.com/developers/docs/resources/webhook#delete-webhook-message"""
        return self._request(  # type: ignore[no-any-return]
            "DELETE",
            uri=f"/webhooks/{webhook_id}/{webhook_token}/messages/{message_id}",
        )

    def get_original_interaction_response(
        self: "Webhook",
        application_id: str,
        interaction_token: str,
        thread_id: Optional[str] = None,
    ) -> dict:
        """https://discord.com/developers/docs/interactions/receiving-and-responding#get-original-interaction-response"""
        payload: dict = {"thread_id": thread_id}
        return self._request(  # type: ignore[no-any-return]
            "GET",
            params={k: v for k, v in payload.items() if v is not None},
            uri=f"/webhooks/{application_id}/{interaction_token}/messages/@original",
        )

    def edit_original_interaction_response(
        self: "Webhook", application_id: str, interaction_token: str
    ) -> dict:
        """https://discord.com/developers/docs/interactions/receiving-and-responding#edit-original-interaction-response"""
        raise NotImplementedError()
        # return self._request('PATCH', uri=f'/webhooks/{application_id}/{interaction_token}/messages/@original')

    def delete_original_interaction_response(
        self: "Webhook", application_id: str, interaction_token: str
    ) -> dict:
        """https://discord.com/developers/docs/interactions/receiving-and-responding#delete-original-interaction-response"""
        return self._request(  # type: ignore[no-any-return]
            "DELETE",
            uri=f"/webhooks/{application_id}/{interaction_token}/messages/@original",
        )

    def create_followup_message(
        self: "Webhook",
        application_id: str,
        interaction_token: str,
        content: Optional[str] = None,
        tts: Optional[bool] = None,
        embeds: Optional[list] = None,
        allowed_mentions: Optional[Any] = None,
        components: Optional[list] = None,
        files: Optional[Any] = None,
        payload_json: Optional[dict] = None,
        attachments: Optional[list] = None,
        flags: Optional[int] = None,
    ) -> dict:
        """https://discord.com/developers/docs/interactions/receiving-and-responding#create-followup-message"""
        payload: dict = {
            "content": content,
            "tts": tts,
            "allowed_mentions": allowed_mentions,
            "components": components,
            "files": files,
            "payload_json": payload_json,
            "attachments": attachments,
            "flags": flags,
            "embeds": embeds,
        }
        return self._request(  # type: ignore[no-any-return]
            "POST",
            params={k: v for k, v in payload.items() if v is not None},
            uri=f"/webhooks/{application_id}/{interaction_token}",
        )

    def get_followup_message(
        self: "Webhook",
        application_id: str,
        interaction_token: str,
        message_id: str,
        thread_id: Optional[str] = None,
    ) -> dict:
        """https://discord.com/developers/docs/interactions/receiving-and-responding#get-followup-message"""
        payload: dict = {"thread_id": thread_id}
        return self._request(  # type: ignore[no-any-return]
            "GET",
            params={k: v for k, v in payload.items() if v is not None},
            uri=f"/webhooks/{application_id}/{interaction_token}/messages/{message_id}",
        )

    def edit_followup_message(
        self: "Webhook", application_id: str, interaction_token: str, message_id: str
    ) -> dict:
        """https://discord.com/developers/docs/interactions/receiving-and-responding#edit-followup-message"""
        raise NotImplementedError()
        # return self._request('PATCH', uri=f'/webhooks/{application_id}/{interaction_token}/messages/{message_id}')

    def delete_followup_message(
        self: "Webhook", application_id: str, interaction_token: str, message_id: str
    ) -> dict:
        """https://discord.com/developers/docs/interactions/receiving-and-responding#delete-followup-message"""
        return self._request(  # type: ignore[no-any-return]
            "DELETE",
            uri=f"/webhooks/{application_id}/{interaction_token}/messages/{message_id}",
        )
