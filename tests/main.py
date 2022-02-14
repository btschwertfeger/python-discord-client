import asyncio
import websockets as ws
import sys, os, traceback
import logging 
from dotenv import dotenv_values

sys.path.append(os.environ.get('PROJECT_ROOT_DIR'))
from discoPy.client import Application, User, Guild, Channel, Stage,  Webhook
from discoPy.ws_client import WSClient

# ----- ----- D O C U M E N T A T I O N ----- -----
# https://discord.com/developers/docs/topics/gateway


logging.basicConfig(
    #filename='example.log', filemode='w',
    level=logging.INFO, # or logging.DEBUG
    format='%(asctime)s, line: %(lineno)d \t| %(message)s'
)

token = dotenv_values('.pythonenv')['TOKEN'] # setup .pythonenv file or just type in your token 

# no channel specified
channel = Channel(token=token)

# print(channel.create_message(
#     channel_id=142319285924151308, 
#     content='Hello World!', 
#     embeds=[{
#         'title': 'Look at these',
#         'description': 'What a nice shot',
#         'thumbnail': {
#             "url": 'attachment://test.png'
#         },
#     }],
#     attachments = [{
#         'id': 0,
#         'description': "Image of a cute little cat",
#         'filename': "test.png"
#     },{
#         'id': 1,
#         'description': "Image of a cute little cat",
#         'filename': "test.png"
#     }],
#     files=['test.png', 'test.png']
# ))

# custom channel
mychannel = Channel(token, channel_id=142319285924151308)
mychannel.create_message(content='test')

exit()

# guild = Guild(token=token)
# print(guild.get_guild(guild_id='<some-guild-id>'))

# stage = Stage(token=token)
# print(stage.get_stage_instance(channel_id='<some-channel-id>'))

# app = Application(token=token)
# app.get_application_commands(application_id='<some-app-id>')

# user = User(token=token)
# print(user.get_current_user())

async def main() -> None:
    async def handle_event(data: dict):
        print(data) # <- comment this to avoid to many output
        
        if not data or 'op' not in data:
            return 

        if data['op'] == 0:  # Dispatch
            try:
                print(f'Channel: {data["d"]["channel_id"]} | {data["d"]["author"]["username"]}: {data["d"]["content"]}')
            except:
                # handle... 
                pass

        elif data['op'] == 3:  # Presence Update
            print(f'This is OP 3 - {data}')
        elif data['op'] == 4:  # Voice State Update
            print(f'This is OP 4 - {data}')
        elif data['op'] == 6:  # Resume
            print(f'This is OP 6 - {data}')
        elif data['op'] == 7:  # Reconnect
            print(f'This is OP 7 - {data}')
        elif data['op'] == 8:  # Request Guild Members
            print(f'This is OP 8 - {data}')
        elif data['op'] == 9:  # Invalid Session
            print(f'This is OP 9 - Invalid Session! {data}')
        elif data['op'] == 10:  # Hello
            print('Hearbeat interval received!')
        elif data['op'] == 11:  # Heartbeat ACK
            print('Heartbeat Received') 
        else:
            print(f'huh? {data}')

    all_intents: list = WSClient.get_intents_list()
    ws_client = WSClient(
        token=token,
        intents=all_intents,#['DIRECT_MESSAGES', 'GUILDS'],
        callback=handle_event        
    )
    while True:
        await asyncio.sleep(30) 
        

if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())