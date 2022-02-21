import numpy as np


class Intents(object):
    '''Object to store and serve intents for WSClient '''

    _intents = [
        'GUILDS', 'GUILD_MEMBERS', 'GUILD_BANS', 'GUILD_EMOJIS_AND_STICKERS', 'GUILD_INTEGRATIONS', 'GUILD_WEBHOOKS',
        'GUILD_INVITES', 'GUILD_VOICE_STATES', 'GUILD_PRESENCES', 'GUILD_MESSAGES', 'GUILD_MESSAGE_REACTIONS',
        'GUILD_MESSAGE_TYPING', 'DIRECT_MESSAGES', 'DIRECT_MESSAGE_REACTIONS', 'GUILD_SCHEDULED_EVENTS', 'GUILD_SCHEDULED_EVENTS'
    ]

    def get_intents_list(self) -> [str]:
        return self._intents

    def get_intent(self, intent_name: str='') -> int:
        for i, role in enumerate(self._intents):
            if role == intent_name:
                return (1<<i)
        raise ValueError(f'Intent {intent_name} not found!')
    
    def get_intents(self, intents_list: [str]) -> int:
        return np.sum([self.get_intent(intent) for intent in intents_list])

    
    # def _get_intents(self, intents: str) -> int:
    #     # https://discord.com/developers/docs/topics/gateway#gateway-intents
    #     if intents == 'GUILDS':
    #         '''
    #             - GUILD_CREATE
    #             - GUILD_UPDATE
    #             - GUILD_DELETE
    #             - GUILD_ROLE_CREATE
    #             - GUILD_ROLE_UPDATE
    #             - GUILD_ROLE_DELETE
    #             - CHANNEL_CREATE
    #             - CHANNEL_UPDATE
    #             - CHANNEL_DELETE
    #             - CHANNEL_PINS_UPDATE
    #             - THREAD_CREATE
    #             - THREAD_UPDATE
    #             - THREAD_DELETE
    #             - THREAD_LIST_SYNC
    #             - THREAD_MEMBER_UPDATE
    #             - THREAD_MEMBERS_UPDATE
    #             - STAGE_INSTANCE_CREATE
    #             - STAGE_INSTANCE_UPDATE
    #             - STAGE_INSTANCE_DELETE
    #         '''
    #         return (1 << 0)
    #     elif intents == 'GUILD_MEMBERS':
    #         '''
    #             - GUILD_MEMBER_ADD
    #             - GUILD_MEMBER_UPDATE
    #             - GUILD_MEMBER_REMOVE
    #             - THREAD_MEMBERS_UPDATE *
    #         '''
    #         return (1 << 1)
    #     elif intents == 'GUILD_BANS':
    #         '''
    #             - GUILD_BAN_ADD
    #             - GUILD_BAN_REMOVE
    #         '''
    #         return (1 << 2)
    #     elif intents == 'GUILD_EMOJIS_AND_STICKERS':
    #         '''
    #             - GUILD_EMOJIS_UPDATE
    #             - GUILD_STICKERS_UPDATE
    #         '''
    #         return (1 << 3)
    #     elif intents == 'GUILD_INTEGRATIONS': 
    #         '''
    #             - GUILD_INTEGRATIONS_UPDATE
    #             - INTEGRATION_CREATE
    #             - INTEGRATION_UPDATE
    #             - INTEGRATION_DELETE
    #         '''
    #         return (1 << 4)
    #     elif intents == 'GUILD_WEBHOOKS':
    #         '''
    #             - WEBHOOKS_UPDATE
    #         '''
    #         return (1 << 5)
    #     elif intents == 'GUILD_INVITES':
    #         '''
    #             - INVITE_CREATE
    #             - INVITE_DELETE
    #         '''
    #         return (1 << 6)
    #     elif intents == 'GUILD_VOICE_STATES': 
    #         '''
    #             - VOICE_STATE_UPDATE
    #         '''
    #         return (1 << 7)
    #     elif intents == 'GUILD_PRESENCES': 
    #         '''
    #             - PRESENCE_UPDATE
    #         '''
    #         return (1 << 8)
    #     elif intents == 'GUILD_MESSAGES':
    #         '''
    #             - MESSAGE_CREATE
    #             - MESSAGE_UPDATE
    #             - MESSAGE_DELETE
    #             - MESSAGE_DELETE_BULK
    #         '''
    #         return  (1 << 9)
    #     elif intents == 'GUILD_MESSAGE_REACTIONS':
    #         '''
    #             - MESSAGE_REACTION_ADD
    #             - MESSAGE_REACTION_REMOVE
    #             - MESSAGE_REACTION_REMOVE_ALL
    #             - MESSAGE_REACTION_REMOVE_EMOJI
    #         '''
    #         return  (1 << 10)
    #     elif intents == 'GUILD_MESSAGE_TYPING': 
    #         '''
    #             - TYPING_START
    #         '''
    #         return (1 << 11)
    #     elif intents == 'DIRECT_MESSAGES':
    #         '''
    #             - MESSAGE_CREATE
    #             - MESSAGE_UPDATE
    #             - MESSAGE_DELETE
    #             - CHANNEL_PINS_UPDATE
    #         '''
    #         return (1 << 12)
    #     elif intents == 'DIRECT_MESSAGE_REACTIONS': 
    #         '''
    #             - MESSAGE_REACTION_ADD
    #             - MESSAGE_REACTION_REMOVE
    #             - MESSAGE_REACTION_REMOVE_ALL
    #             - MESSAGE_REACTION_REMOVE_EMOJI
    #         '''
    #         return (1 << 13)
    #     elif intents == 'DIRECT_MESSAGE_TYPING': 
    #         '''
    #             - TYPING_START
    #         '''
    #         return (1 << 14)
    #     elif intents == 'GUILD_SCHEDULED_EVENTS': 
    #         '''
    #             - GUILD_SCHEDULED_EVENT_CREATE
    #             - GUILD_SCHEDULED_EVENT_UPDATE
    #             - GUILD_SCHEDULED_EVENT_DELETE
    #             - GUILD_SCHEDULED_EVENT_USER_ADD
    #             - GUILD_SCHEDULED_EVENT_USER_REMOVE
    #         '''
    #         return (1 << 16)
    #     else:
    #         raise Exception('Uknown Intent!')
