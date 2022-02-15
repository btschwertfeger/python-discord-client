# Discord Channel Endpoints

# Important notes

The implementation of the methods was based on the official documentation of the Discord API. Parameters and endpoints have been adapted to it.
On the official page of the Discord API documentation you can see which requirements and parameters are needed for the respective methods.

Note: We have nothing to do with Discord and have not contributed to the Discord documentation!

## Available Methods:

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
