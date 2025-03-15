from django.urls import re_path
from admin_panel.consumers import LiveStreamConsumer

websocket_urlpatterns = [
    re_path(r"ws/webrtc/$", LiveStreamConsumer.as_asgi()),
]
