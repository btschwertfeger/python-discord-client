# Discord Webhook Endpoints

# Important notes

The implementation of the methods was based on the official documentation of the Discord API. Parameters and endpoints have been adapted to it.
On the official page of the Discord API documentation you can see which requirements and parameters are needed for the respective methods.

Note: We have nothing to do with Discord and have not contributed to the Discord documentation!

## Available methods:

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

## Not implemented:

| Method                             | Documentation                                                                                                |
| ---------------------------------- | ------------------------------------------------------------------------------------------------------------ |
| execute_webhook                    | https://discord.com/developers/docs/resources/webhook#execute-webhook                                        |
| execute_github_compatible_webhook  | https://discord.com/developers/docs/resources/webhook#execute-slackcompatible-webhook                        |
| get_webhook_messages               | https://discord.com/developers/docs/resources/webhook#execute-githubcompatible-webhook                       |
| edit_webhook_messages              | https://discord.com/developers/docs/resources/webhook#edit-webhook-message                                   |
| edit_original_interaction_response | https://discord.com/developers/docs/interactions/receiving-and-responding#edit-original-interaction-response |
