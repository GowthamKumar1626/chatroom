import json
from channels.generic.websocket import AsyncWebsocketConsumer


class ChatRoomConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = f'chat_{self.room_name}'

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'tester_message',
                'tester': 'tester'
            }
        )

    # async def receive(self, text_data=None):

    #     text_data_json = json.loads(text_data)
    #     tester = text_data_json['tester']
    
    async def tester_message(self, event):
        tester = event['tester']

        await self.send(text_data=json.dumps({
            'tester': tester
        }))
    
    async def disconnect(self, code):
        return await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )