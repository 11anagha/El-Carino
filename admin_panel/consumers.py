import json
from channels.generic.websocket import AsyncWebsocketConsumer

active_streams = {}  # Store active stream sessions

class WebRTCConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.stream_id = self.scope["url_route"]["kwargs"].get("stream_id")
        if not self.stream_id:
            self.stream_id = str(self.channel_name)  # Unique identifier for the stream
            active_streams[self.stream_id] = self.channel_name

        await self.channel_layer.group_add(self.stream_id, self.channel_name)
        await self.accept()

        # Send back stream ID if it's a new stream
        if self.stream_id not in active_streams:
            await self.send(json.dumps({"type": "stream_id", "stream_id": self.stream_id}))

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.stream_id, self.channel_name)
        active_streams.pop(self.stream_id, None)

    async def receive(self, text_data):
        data = json.loads(text_data)
        await self.channel_layer.group_send(
            self.stream_id,
            {
                "type": "send_sdp",
                "message": data,
            },
        )

    async def send_sdp(self, event):
        await self.send(text_data=json.dumps(event["message"]))



class LiveStreamConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
    
    async def disconnect(self, close_code):
        pass
    
    async def receive(self, text_data):
        data = json.loads(text_data)
        await self.send(text_data=json.dumps(data))