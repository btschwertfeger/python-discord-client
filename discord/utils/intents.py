# -*- coding: utf-8 -*-


"""Module that implements the intent related functions for use in the websocket client."""

from typing import List


class Intents:
    """Object to store and serve intents for WSClient"""

    # https://discord.com/developers/docs/topics/gateway#gateway-intents
    INTENTS: List[str] = [
        "GUILDS",
        "GUILD_MEMBERS",
        "GUILD_BANS",
        "GUILD_EMOJIS_AND_STICKERS",
        "GUILD_INTEGRATIONS",
        "GUILD_WEBHOOKS",
        "GUILD_INVITES",
        "GUILD_VOICE_STATES",
        "GUILD_PRESENCES",
        "GUILD_MESSAGES",
        "GUILD_MESSAGE_REACTIONS",
        "GUILD_MESSAGE_TYPING",
        "DIRECT_MESSAGES",
        "DIRECT_MESSAGE_REACTIONS",
        "GUILD_SCHEDULED_EVENTS",
        "GUILD_SCHEDULED_EVENTS",
    ]

    @classmethod
    def get_intents_list(cls) -> List[str]:
        """Return the available intents"""
        return cls.INTENTS

    def get_intent(self: "Intents", intent_name: str = "") -> int:
        """Return the intent value for a specific intention"""
        for i, role in enumerate(self.INTENTS):
            if role == intent_name:
                return 1 << i
        raise ValueError(f"Intent {intent_name} not found!")

    def _get_intents(self: "Intents", intents_list: List[str]) -> int:
        """Return the accumulated intent value"""
        return sum(self.get_intent(intent) for intent in intents_list)
