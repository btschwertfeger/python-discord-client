# Discord Guild Endpoints

# Important notes

The implementation of the methods was based on the official documentation of the Discord API. Parameters and endpoints have been adapted to it.
On the official page of the Discord API documentation you can see which requirements and parameters are needed for the respective methods.

Note: We have nothing to do with Discord and have not contributed to the Discord documentation!

## Available Methods:

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
