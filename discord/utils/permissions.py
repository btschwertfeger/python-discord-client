# -*- coding: utf-8 -*-


"""Module that implements the permissions related functions for the websocket client."""

from typing import List


class Permissions:
    """Object to store and access User and Bot Permissions"""

    ROLES = [
        "CREATE_INSTANT_INVITE",
        "KICK_MEMBERS",
        "BAN_MEMBERS",
        "ADMINISTRATOR",
        "MANAGE_CHANNELS",
        "MANAGE_GUILD",
        "ADD_REACTIONS",
        "VIEW_AUDIT_LOG",
        "PRIORITY_SPEAKER",
        "STREAM",
        "VIEW_CHANNEL",
        "SEND_MESSAGES",
        "SEND_TTS_MESSAGES",
        "MANAGE_MESSAGES",
        "EMBED_LINKS",
        "ATTACH_FILES",
        "READ_MESSAGE_HISTORY",
        "MENTION_EVERYONE",
        "USE_EXTERNAL_EMOJIS",
        "VIEW_GUILD_INSIGHTS",
        "CONNECT",
        "SPEAK",
        "MUTE_MEMBERS",
        "DEAFEN_MEMBERS",
        "MOVE_MEMBERS",
        "USE_VAD",
        "CHANGE_NICKNAME",
        "MANAGE_NICKNAMES",
        "MANAGE_ROLES",
        "MANAGE_WEBHOOKS",
        "MANAGE_EMOJIS_AND_STICKERS",
        "USE_APPLICATION_COMMANDS",
        "REQUEST_TO_SPEAK",
        "MANAGE_EVENTS",
        "MANAGE_THREADS",
        "CREATE_PUBLIC_THREADS",
        "CREATE_PRIVATE_THREADS",
        "USE_EXTERNAL_STICKERS",
        "SEND_MESSAGES_IN_THREADS",
        "START_EMBEDDED_ACTIVITIES",
        "MODERATE_MEMBERS",
    ]

    @classmethod
    def list_roles(cls) -> List[str]:
        """Return the roles"""
        return cls.ROLES

    def get_role(self, role_name: str = "") -> int:
        """Retrieve a specific role"""
        for i, role in enumerate(self.ROLES):
            if role == role_name:
                return 1 << i
        raise ValueError(f"Role {role_name} not found!")

    def get_roles(self, roles_list: List[str]) -> int:
        """Get the integer value of roles"""
        return sum(self.get_role(role) for role in roles_list)
