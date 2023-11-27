from django.urls import path
from . import consumers

websocket_urlpatterns = [
    path('chat/messages/', consumers.ChatConsumer.as_asgi()),
    path('chat/user_login/', consumers.LoginConsumer.as_asgi()),
    ]
