import asyncio
import websockets as ws
import sys, os, traceback
import logging 
from dotenv import dotenv_values

sys.path.append(os.environ.get('PROJECT_ROOT_DIR'))
from discoPy.rest.client import Application, User, Guild, Channel, Stage,  Webhook
from discoPy.rest.ws_client import WSClient

logging.basicConfig(
    #filename='example.log', filemode='w',
    level=logging.INFO, # or logging.DEBUG
    format='%(asctime)s, line: %(lineno)d \t| %(message)s'
)


def main() -> None:

    token = dotenv_values('.pythonenv')['TOKEN'] # setup .pythonenv file or just type in your token 

    # no channel specified
    channel = Channel(token=token)

    print(channel.create_message(
        channel_id=142319285924151308, 
        content='Hello World!', 
        embeds=[{
            'title': 'Look at these',
            'description': 'What a nice shot',
            'thumbnail': {
                "url": 'attachment://test.png'
            },
        }],
        attachments = [{
            'id': 0,
            'description': "Image of a cute little cat",
            'filename': "test.png"
        }],
        files=['test.png']
    ))

    # custom channel
    mychannel = Channel(token, channel_id=142319285924151308)
    mychannel.create_message(content='Hello')

    guild = Guild(token=token)
    print(guild.get_guild(guild_id='<some-guild-id>'))

    stage = Stage(token=token)
    print(stage.get_stage_instance(channel_id='<some-channel-id>'))

    app = Application(token=token)
    app.get_application_commands(application_id='<some-app-id>')

    user = User(token=token)
    print(user.get_current_user())

if __name__ == '__main__':
    main()