import asyncio
import websockets as ws
import sys, os, traceback
import logging 


from dotenv import dotenv_values

sys.path.append(os.environ.get('PROJECT_ROOT_DIR'))
from python_discord_client.ws_client import WSClient
from python_discord_client.client import Guild
#from python_discord_client.ws_client import WSClient
#from python_discord_client.client import Guild

# ----- ----- D O C U M E N T A T I O N ----- -----
# https://discord.com/developers/docs/topics/gateway


logging.basicConfig(
    #filename='example.log', filemode='w',
    level=logging.INFO, # or logging.DEBUG
    format='%(asctime)s, line: %(lineno)d \t| %(message)s'
)

token = dotenv_values('.pythonenv')['TOKEN'] # setup .pythonenv file or just type in your token 
client = Guild(token=token)
client.send_message(942319916005097472, 'Hello!')
# print(client.get_guild(2909267986263572999))
exit()
async def main():
    async def handle_event(data: dict):
        print(data) # <- comment this to avoid to many output
        print('_____________________\n\n\n--------------------')
        if not data or 'op' not in data:
            return 

        if data['op'] == 0:  # Dispatch
            try:
                print(f'{data["d"]["channel_id"]} | {data["d"]["author"]["username"]}: {data["d"]["content"]}')
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

    ws_client = WSClient(
        token=token,
        intents=['DIRECT_MESSAGES', 'GUILDS'],
        callback=handle_event        
    )

    
    while True:
        await asyncio.sleep(30) 
        

if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())