from discoPy.core.WSClient import WSClient
import asyncio 

from dotenv import dotenv_values

class objectview(object):
    def __init__(self, d: dict={}):
        self.__dict__ = d

class TestClient(WSClient):
    async def on_event(self, event) -> None:
        # print(event) 
        if not event or 'op' not in event:
            return

        if event['op'] == 0:  # Dispatch
            try:
                print(f'Channel: {data["d"]["channel_id"]} | {data["d"]["author"]["username"]}: {data["d"]["content"]}')
            except:
                # handle...
                pass

        elif event['op'] == 3:  # Presence Update
            print(f'This is OP 3 - {event}')
        elif event['op'] == 4:  # Voice State Update
            print(f'This is OP 7 - {event}')
        elif event['op'] == 8:  # Request Guild Members
            print(f'This is OP 8 - {event}')


async def main() -> None:
    config = objectview(dotenv_values('.pythonenv'))
    token = config.TOKEN
    default_channel_id = config.DEFAULT_CHANNEL_ID
    default_guild_id = config.DEFAULT_GUILD_ID

    myclient = TestClient( 
        token = token,
        intents=WSClient.get_intents_list(),
    )

    # ---===== CREATE GUILD =====---
    # print( await myclient.create_guild(
    #     name = 'SomeNiceTestingGuild1',
    #     verification_level=3, # member longer than 10 minutes
    #     default_message_notifications=0, # default messagin
    #     explicit_content_filter=0, # no filteriing
    #     roles=[{
    #         'id': 12345,
    #         'name': 'somtestrole',
    #         'hoist': True,
    #         'color': 3447003,
    #         'position': 0,
    #         'unicode_emoji': None,
    #         'icon': None,
    #         "permissions": "66321471",
    #         "managed": False,
    #         "mentionable": False
    #     }]
    # ))

    # print(await myclient.get_guild_preview(default_guild_id))
    # print(await myclient.get_guild(default_guild_id))

    # =========----> print(await myclient.modify_guild(
    #   uild_id=default_guild_id
    #   name='somenewname'
    # )

    # print(await delete_guild(guild_id=default_guild_id))
    # print(await myclient.get_guild_channels(default_guild_id))
    
    # print(await myclient.create_guild_channel(
    #     guild_id=default_guild_id,
    #     name='someTestChannel',
    #     topic='FunTopic',
    #     bitrate=8000,
    #     user_limit=99,
    #     rate_limit_per_user=5,
    #     permission_overwrites=[],
    #     parent_id=143909225313210399,
    #     type=0, # test channell for users
    #     position=2,
    #     nsfw=False
    # ))

    # =======----> print(await myclient.modify_channel_positions(default_guild_id,position=2,lock_permissions=False)

    # =======---->  print(await myclient.list_active_threads(default_guild_id, [],[]))

    # =======----> print(await myclient.get_guild_member(guild_id=default_guild_id, user_id=xxx))
    
    # print(await myclient.search_guild_members(default_guild_id,query='user', limit=10))

    # =======----> print(await myclientadd_guild_member(
    #     guild_id=default_guild_id, 
    #     user_id='hjbdf', 
    #     access_token= 'OAuth2token', 
    #     nick='value to set users name to', 
    #     roles= [(1<<0)], 
    #     mute=True,
    #     deaf=True
    # ))
    # myclient.run()

    # while True:
    #     await asyncio.sleep(30)

if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())