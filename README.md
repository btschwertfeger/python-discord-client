# Welcome to python-discord-client

[![Generic badge](https://img.shields.io/badge/license-MIT-green.svg)](https://shields.io/)
[![Generic badge](https://img.shields.io/badge/python-3.7+-blue.svg)](https://shields.io/)
[![PyPI download month](https://img.shields.io/pypi/dm/python-discord-client.svg)](https://pypi.python.org/pypi/python-discord-client/)
[![GitHub](https://badgen.net/badge/icon/github?icon=github&label)](https://github.com/btschwertfeger/python-discord-client)

Unofficial Python Discord SDK

📍 Note: We have nothing to do with Discord and have not contributed to the Discord documentation!

### 📍 This project is worked on daily. The releases available on PyPi may differ from those in the Github repository. So please see PyPi for working examples.

# Features

- Connect to your Discord account
- Simple handling of authentication
- Access nearly all Discord REST endpoints (synchron and asynchron)
- Websocket Client to receive almost all events
- Create your custom Bots and manage your Guilds

# Quick Start

- Register at [Discord](https://discord.com/)
- Create a new app or use an existing one at https://discord.com/developers/applications
- Create a bot, set permissions and save your token

```bash
python3 -m pip install python-discord-client
```

## Synchron REST Clients

```python
from discoPy.rest.client import Application, User, Guild, Channel, Stage, Webhook

token = 'your-discord-token'
channel = Channel(token=token, channel_id='<some-channel-id>')
channel.create_message(content='Hello World!')

guild = Guild(token=token)
print(guild.get_guild(guild_id='<some-guild-id>'))

stage = Stage(token=token)
print(stage.get_stage_instance(channel_id='<some-channel-id>'))

app = Application(token=token)
print(app.get_application_commands(application_id='<some-app-id>'))

user = User(token=token)
print(user.get_current_user())

# ...

```

## Websockets / WS Client (asynchron)

```python

from discoPy.core.WSClient import WSClient
import asyncio

class CustomClient(WSClient):

    async def on_event(self, event) -> None:
        print(event) # <- comment this out
        if not event or 'op' not in event:
            return

        if event['op'] == 0:  # Dispatch
            try:
                print(f'Channel: {data["d"]["channel_id"]} | {data["d"]["author"]["username"]}: {data["d"]["content"]}')
                # if condition:
                #    await self.create_message(
                #           channel_id=channel_id, content='I love it!'
                #    )
            except:
                # handle...
                pass

        elif event['op'] == 3:  # Presence Update
            print(f'This is OP 3 - {event}')
        elif event['op'] == 4:  # Voice State Update
            print(f'This is OP 4 - {event}')
        elif event['op'] == 6:  # Resume
            print(f'This is OP 6 - {event}')
        elif event['op'] == 7:  # Reconnect
            print(f'This is OP 7 - {event}')
        elif event['op'] == 8:  # Request Guild Members
            print(f'This is OP 8 - {event}')
        elif event['op'] == 9:  # Invalid Session
            print(f'This is OP 9 - Invalid Session! {event}')
        elif event['op'] == 10:  # Hello
            print('Hearbeat interval received!')
        elif event['op'] == 11:  # Heartbeat ACK
            print('Heartbeat Received')
        else:
            print(f"huh? {event}")


async def main() -> None:
    token = '<discord-bot-token>'

    #all_intents: list = WSClient.get_intents_list()
    ws_client = CustomClient(
        token=token,
        intents=['DIRECT_MESSAGES', 'GUILDS'],
    )

    # Almost every endpoint can be accessed via the websocket client.
    print(await myclient.get_current_user())
    print(await myclient.get_channel('<some-channel-id>'))
    # ...

    myclient.run() # opens the websocket connection to receive events

    while True:
        await asyncio.sleep(30)

if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())

```

# Important notes

The implementation of the methods was based on the official documentation of the Discord API. Parameters and endpoints have been adapted to it.
On the official page of the Discord API documentation you can see which requirements and parameters are needed for the respective methods.

Note: We have nothing to do with Discord and have not contributed to the Discord documentation!

# Methods

All methods below are available via the Rest and Websocket Clients.

## Application

| Method                                     | Documentation                                                                                                    |
| ------------------------------------------ | ---------------------------------------------------------------------------------------------------------------- |
| get_application_commands                   | https://discord.com/developers/docs/interactions/application-commands#get-global-application-commands            |
| create_application_command                 | https://discord.com/developers/docs/interactions/application-commands#create-global-application-command          |
| get_global_application_command             | https://discord.com/developers/docs/interactions/application-commands#get-global-application-command             |
| edit_global_application_command            | https://discord.com/developers/docs/interactions/application-commands#edit-global-application-command            |
| delete_global_application_command          | https://discord.com/developers/docs/interactions/application-commands#delete-global-application-command          |
| bulk_overwrite_global_application_command  | https://discord.com/developers/docs/interactions/application-commands#bulk-overwrite-global-application-commands |
| get_guild_application_commands             | https://discord.com/developers/docs/interactions/application-commands#get-guild-application-commands             |
| create_guild_application_command           | https://discord.com/developers/docs/interactions/application-commands#create-guild-application-command           |
| get_guild_application_command              | https://discord.com/developers/docs/interactions/application-commands#get-guild-application-command              |
| edit_guild_application_command             | https://discord.com/developers/docs/interactions/application-commands#edit-guild-application-command             |
| delete_guild_application_command           | https://discord.com/developers/docs/interactions/application-commands#delete-guild-application-command           |
| bulk_overwrite_guild_application_command   | https://discord.com/developers/docs/interactions/application-commands#bulk-overwrite-guild-application-commands  |
| get_guild_application_command_permissions  | https://discord.com/developers/docs/interactions/application-commands#get-guild-application-command-permissions  |
| get_application_comman_permissions         | https://discord.com/developers/docs/interactions/application-commands#get-application-command-permissions        |
| edit_application_command_permissions       | https://discord.com/developers/docs/interactions/application-commands#edit-application-command-permissions       |
| batch_edit_application_command_permissions | https://discord.com/developers/docs/interactions/application-commands#batch-edit-application-command-permissions |

## User

| Method                        | Documentation                                                                    |
| ----------------------------- | -------------------------------------------------------------------------------- |
| get_current_user              | https://discord.com/developers/docs/resources/user#get-current-user              |
| get_user                      | https://discord.com/developers/docs/resources/user#get-user                      |
| modify_current_user           | https://discord.com/developers/docs/resources/user#modify-current-user           |
| get_current_user_guilds       | https://discord.com/developers/docs/resources/user#get-current-user-guilds       |
| get_current_user_guild_member | https://discord.com/developers/docs/resources/user#get-current-user-guild-member |
| leave_guild                   | https://discord.com/developers/docs/resources/user#leave-guild                   |
| create_dm                     | https://discord.com/developers/docs/resources/user#create-dm                     |
| create_group_dm               | https://discord.com/developers/docs/resources/user#create-group-dm               |
| get_user_connections          | https://discord.com/developers/docs/resources/user#get-user-connections          |
| list_voice_regions            | https://discord.com/developers/docs/resources/voice#list-voice-regions           |
| get_invite                    | https://discord.com/developers/docs/resources/invite#get-invite                  |
| delete_invite                 | https://discord.com/developers/docs/resources/invite#delete-invite               |

## Guild

### General

| Method                        | Documentation                                                                      |
| ----------------------------- | ---------------------------------------------------------------------------------- |
| create_guild                  | https://discord.com/developers/docs/resources/guild#create-guild                   |
| get_guild                     | https://discord.com/developers/docs/resources/guild#get-guild                      |
| get_guild_preview             | https://discord.com/developers/docs/resources/guild#get-guild-preview              |
| modify_guild                  | https://discord.com/developers/docs/resources/guild#modify-guild                   |
| delete_guild                  | https://discord.com/developers/docs/resources/guild#delete-guild                   |
| get_guild_channels            | https://discord.com/developers/docs/resources/guild#get-guild-channels             |
| create_guild_channel          | https://discord.com/developers/docs/resources/guild#create-guild-channel           |
| modify_channel_positions      | https://discord.com/developers/docs/resources/guild#modify-guild-channel-positions |
| list_active_threads           | https://discord.com/developers/docs/resources/guild#list-active-threads            |
| get_guild_member              | https://discord.com/developers/docs/resources/guild#get-guild-member               |
| list_guild_members            | https://discord.com/developers/docs/resources/guild#list-guild-members             |
| search_guild_members          | https://discord.com/developers/docs/resources/guild#search-guild-members           |
| add_guild_member              | https://discord.com/developers/docs/resources/guild#add-guild-member               |
| modify_current_member         | https://discord.com/developers/docs/resources/guild#modify-current-member          |
| add_guild_member_role         | https://discord.com/developers/docs/resources/guild#add-guild-member-role          |
| remove_guild_member_role      | https://discord.com/developers/docs/resources/guild#remove-guild-member-role       |
| remove_guild_member           | https://discord.com/developers/docs/resources/guild#remove-guild-member            |
| get_guild_bans                | https://discord.com/developers/docs/resources/guild#get-guild-bans                 |
| get_guild_ban                 | https://discord.com/developers/docs/resources/guild#get-guild-ban                  |
| create_guild_ban              | https://discord.com/developers/docs/resources/guild#create-guild-ban               |
| remove_guild_ban              | https://discord.com/developers/docs/resources/guild#remove-guild-ba                |
| get_guild_roles               | https://discord.com/developers/docs/resources/guild#get-guild-roles                |
| create_guild_role             | https://discord.com/developers/docs/resources/guild#create-guild-role              |
| modify_guild_role_permissions | https://discord.com/developers/docs/resources/guild#modify-guild-role-positions    |
| modify_guild_role             | https://discord.com/developers/docs/resources/guild#modify-guild-role              |
| delete_guild_role             | https://discord.com/developers/docs/resources/guild#delete-guild-role              |
| get_guild_prune_count         | https://discord.com/developers/docs/resources/guild#get-guild-prune-count          |
| beginn_guild_prune            | https://discord.com/developers/docs/resources/guild#begin-guild-prune              |
| get_guild_voice_regions       | https://discord.com/developers/docs/resources/guild#get-guild-voice-regions        |
| get_guild_invites             | https://discord.com/developers/docs/resources/guild#get-guild-invites              |
| get_guild_integrations        | https://discord.com/developers/docs/resources/guild#get-guild-integrations         |
| delete_guild_integrations     | https://discord.com/developers/docs/resources/guild#delete-guild-integration       |
|                               |                                                                                    |
|                               |                                                                                    |

### Widgets and Styles

| Method                          | Documentation                                                                       |
| ------------------------------- | ----------------------------------------------------------------------------------- |
| get_guild_widget_settings       | https://discord.com/developers/docs/resources/guild#get-guild-widget-settings       |
| modify_guild_widget             | https://discord.com/developers/docs/resources/guild#modify-guild-widget             |
| get_guild_widget                | https://discord.com/developers/docs/resources/guild#get-guild-widget                |
| get_guild_vanity_url            | https://discord.com/developers/docs/resources/guild#get-guild-vanity-url            |
| get_guild_widget_image          | https://discord.com/developers/docs/resources/guild#get-guild-widget-image          |
| get_guild_welcome_screen        | https://discord.com/developers/docs/resources/guild#get-guild-welcome-screen        |
| modify_guild_welcome_screen     | https://discord.com/developers/docs/resources/guild#modify-guild-welcome-screen     |
| modify_current_user_voice_state | https://discord.com/developers/docs/resources/guild#modify-guild-welcome-screen     |
| modify_current_user_voice_state | https://discord.com/developers/docs/resources/guild#modify-current-user-voice-state |
| modify_user_voice_state         | https://discord.com/developers/docs/resources/guild#modify-user-voice-state         |
| get_guild_audit_log             | https://discord.com/developers/docs/resources/audit-log#get-guild-audit-log         |

### Scheduled Events

| Method                          | Documentation                                                                                       |
| ------------------------------- | --------------------------------------------------------------------------------------------------- |
| list_scheduled_events_for_guild | https://discord.com/developers/docs/resources/guild-scheduled-event#list-scheduled-events-for-guild |
| create_guild_scheduled_event    | https://discord.com/developers/docs/resources/guild-scheduled-event#create-guild-scheduled-event    |
| get_guild_scheduled_event       | https://discord.com/developers/docs/resources/guild-scheduled-event#get-guild-scheduled-event       |
| modify_guild_scheduled_event    | https://discord.com/developers/docs/resources/guild-scheduled-event#modify-guild-scheduled-event    |
| delete_guild_scheduled_evend    | https://discord.com/developers/docs/resources/guild-scheduled-event#delete-guild-scheduled-event    |
| get_guild_scheduled_event_users | https://discord.com/developers/docs/resources/guild-scheduled-event#get-guild-scheduled-event-users |

### Guild Templates

| Method                | Documentation                                                                                 |
| --------------------- | --------------------------------------------------------------------------------------------- |
| get_guild_template    | https://discord.com/developers/docs/resources/guild-template#get-guild-template               |
| create_guild_template | https://discord.com/developers/docs/resources/guild-template#create-guild-from-guild-template |
| get_guild_templates   | https://discord.com/developers/docs/resources/guild-template#get-guild-templates              |
| create_guild_template | https://discord.com/developers/docs/resources/guild-template#create-guild-template            |
| sync_guild_template   | https://discord.com/developers/docs/resources/guild-template#sync-guild-template              |
| modify_guild_template | https://discord.com/developers/docs/resources/guild-template#modify-guild-template            |
| delete_guild_template | https://discord.com/developers/docs/resources/guild-template#delete-guild-template            |

### Emoji

| Method             | Documentation                                                          |
| ------------------ | ---------------------------------------------------------------------- |
| list_guild_emojis  | https://discord.com/developers/docs/resources/emoji#list-guild-emojis  |
| get_guild_emoji    | https://discord.com/developers/docs/resources/emoji#get-guild-emoji    |
| create_guild_emoji | https://discord.com/developers/docs/resources/emoji#create-guild-emoji |
| modify_guild_emoji | https://discord.com/developers/docs/resources/emoji#modify-guild-emoji |
| delete_guild_emoji | https://discord.com/developers/docs/resources/emoji#delete-guild-emoji |

### Sticker

| Method                   | Documentation                                                                  |
| ------------------------ | ------------------------------------------------------------------------------ |
| get_sticker              | https://discord.com/developers/docs/resources/sticker#get-sticker              |
| list_nitro_sticker_packs | https://discord.com/developers/docs/resources/sticker#list-nitro-sticker-packs |
| list_guild_stickers      | https://discord.com/developers/docs/resources/sticker#list-guild-stickers      |
| get_guild_sticker        | https://discord.com/developers/docs/resources/sticker#get-guild-sticker        |
| create_guild_sticker     | 'https://discord.com/developers/docs/resources/sticker#create-guild-sticker    |
| modify_guild_sticker     | https://discord.com/developers/docs/resources/sticker#modify-guild-sticker     |
| delete_guild_sticker     | https://discord.com/developers/docs/resources/sticker#delete-guild-sticker     |

## Channel

### General

| Method                         | Documentation                                                                        |
| ------------------------------ | ------------------------------------------------------------------------------------ |
| get_channel                    | https://discord.com/developers/docs/resources/channel#get-channel                    |
| modify_channel                 | https://discord.com/developers/docs/resources/channel#modify-channel                 |
| delete_close_channel           | https://discord.com/developers/docs/resources/channel#deleteclose-channel            |
| get_channel_messages           | https://discord.com/developers/docs/resources/channel#get-channel-messages           |
| get_channel_message            | https://discord.com/developers/docs/resources/channel#get-channel-message            |
| create_message                 | https://discord.com/developers/docs/resources/channel#create-message                 |
| crosspost_message              | https://discord.com/developers/docs/resources/channel#crosspost-message              |
| create_reaction                | https://discord.com/developers/docs/resources/channel#create-reaction                |
| delete_own_reaction            | https://discord.com/developers/docs/resources/channel#delete-own-reaction            |
| delete_user_reaction           | https://discord.com/developers/docs/resources/channel#delete-user-reaction           |
| get_reactions                  | https://discord.com/developers/docs/resources/channel#delete-user-reaction           |
| get_reactions                  | https://discord.com/developers/docs/resources/channel#get-reactions                  |
| delete_all_reactions           | https://discord.com/developers/docs/resources/channel#delete-all-reactions           |
| delete_all_reactions_for_emoji | https://discord.com/developers/docs/resources/channel#delete-all-reactions-for-emoji |
| edit_message                   | https://discord.com/developers/docs/resources/channel#edit-message                   |
| delete_message                 | https://discord.com/developers/docs/resources/channel#delete-message                 |
| bulk_delete_message            | https://discord.com/developers/docs/resources/channel#bulk-delete-messages           |
| edit_channel_permissions       | https://discord.com/developers/docs/resources/channel#edit-channel-permissions       |
| get_channel_invites            | https://discord.com/developers/docs/resources/channel#get-channel-invites            |
| create_channel_invite          | https://discord.com/developers/docs/resources/channel#create-channel-invite          |
| delete_channel_permission      | https://discord.com/developers/docs/resources/channel#delete-channel-permission      |
| follow_news_channel            | https://discord.com/developers/docs/resources/channel#follow-news-channel            |
| trigger_typing_indicatoe       | https://discord.com/developers/docs/resources/channel#trigger-typing-indicator       |
| get_pinned_message             | https://discord.com/developers/docs/resources/channel#get-pinned-messages            |
| pin_message                    | https://discord.com/developers/docs/resources/channel#pin-message                    |
| unpin_message                  | https://discord.com/developers/docs/resources/channel#unpin-message                  |
| group_dm_add_recipient         | https://discord.com/developers/docs/resources/channel#group-dm-add-recipient         |
| group_dm_remove_recipient      | https://discord.com/developers/docs/resources/channel#group-dm-remove-recipient      |

### Threads

| Method                               | Documentation                                                                              |
| ------------------------------------ | ------------------------------------------------------------------------------------------ |
| start_thread_with_message            | https://discord.com/developers/docs/resources/channel#start-thread-with-message            |
| start_thread_without_message         | https://discord.com/developers/docs/resources/channel#start-thread-without-message         |
| join_thread                          | https://discord.com/developers/docs/resources/channel#join-thread                          |
| add_thread_member                    | https://discord.com/developers/docs/resources/channel#add-thread-member                    |
| leave_thread                         | https://discord.com/developers/docs/resources/channel#leave-thread                         |
| remove_thread_member                 | https://discord.com/developers/docs/resources/channel#remove-thread-member                 |
| get_thread_member                    | https://discord.com/developers/docs/resources/channel#get-thread-member                    |
| list_thread_member                   | https://discord.com/developers/docs/resources/channel#list-thread-members                  |
| list_active_threads                  | https://discord.com/developers/docs/resources/channel#list-active-threads                  |
| list_public_archived_threads         | https://discord.com/developers/docs/resources/channel#list-public-archived-threads         |
| list_private_archived_threads        | https://discord.com/developers/docs/resources/channel#list-private-archived-threads        |
| list_joined_private_archived_threads | https://discord.com/developers/docs/resources/channel#list-joined-private-archived-threads |

## Stage

| Method                | Documentation                                                                      |
| --------------------- | ---------------------------------------------------------------------------------- |
| create_stage_instance | https://discord.com/developers/docs/resources/stage-instance#create-stage-instance |
| get_stage_instance    | https://discord.com/developers/docs/resources/stage-instance#get-stage-instance    |
| modify_stage_instance | https://discord.com/developers/docs/resources/stage-instance#modify-stage-instance |
| delete_stage_instance | https://discord.com/developers/docs/resources/stage-instance#delete-stage-instance |

## Webhook

| Method                               | Documentation                                                                                                  |
| ------------------------------------ | -------------------------------------------------------------------------------------------------------------- |
| create_webhook                       | https://discord.com/developers/docs/resources/webhook#create-webhook                                           |
| get_channel_webhooks                 | https://discord.com/developers/docs/resources/webhook#create-webhook                                           |
| get_guild_webhooks                   | https://discord.com/developers/docs/resources/webhook#get-guild-webhooks                                       |
| get_webhook                          | https://discord.com/developers/docs/resources/webhook#get-webhook                                              |
| get_webhook_with_token               | https://discord.com/developers/docs/resources/webhook#get-webhook-with-token                                   |
| modify_webhook                       | https://discord.com/developers/docs/resources/webhook#modify-webhook                                           |
| modify_webhook_with_token            | https://discord.com/developers/docs/resources/webhook#modify-webhook-with-token                                |
| delete_webhook                       | https://discord.com/developers/docs/resources/webhook#delete-webhook                                           |
| delete_webhook_with_token            | https://discord.com/developers/docs/resources/webhook#delete-webhook-with-token                                |
| execute_webhook                      | https://discord.com/developers/docs/resources/webhook#execute-webhook                                          |
| delete_webhook_messages              | https://discord.com/developers/docs/resources/webhook#delete-webhook-message                                   |
| get_original_interaction_response    | https://discord.com/developers/docs/interactions/receiving-and-responding#get-original-interaction-response    |
| delete_original_interaction_response | https://discord.com/developers/docs/interactions/receiving-and-responding#delete-original-interaction-response |
| create_followup_message              | https://discord.com/developers/docs/interactions/receiving-and-responding#create-followup-message              |
| get_followup_message                 | https://discord.com/developers/docs/interactions/receiving-and-responding#get-followup-message                 |
| edit_followup_message                | https://discord.com/developers/docs/interactions/receiving-and-responding#edit-followup-message                |
| delete_followup_message              | https://discord.com/developers/docs/interactions/receiving-and-responding#delete-followup-message              |

### Not implemented:

| Method                             | Documentation                                                                                                |
| ---------------------------------- | ------------------------------------------------------------------------------------------------------------ |
| execute_webhook                    | https://discord.com/developers/docs/resources/webhook#execute-webhook                                        |
| execute_github_compatible_webhook  | https://discord.com/developers/docs/resources/webhook#execute-slackcompatible-webhook                        |
| get_webhook_messages               | https://discord.com/developers/docs/resources/webhook#execute-githubcompatible-webhook                       |
| edit_webhook_messages              | https://discord.com/developers/docs/resources/webhook#edit-webhook-message                                   |
| edit_original_interaction_response | https://discord.com/developers/docs/interactions/receiving-and-responding#edit-original-interaction-response |

# Todo

- Testing
