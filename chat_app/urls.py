from django.urls import path
from . import consumers, views

# HTTP маршруты
urlpatterns = [
    path('<str:room_name>/', views.room, name='room'),  # Чат-комната
]

# WebSocket маршруты
websocket_urlpatterns = [
    path('ws/chat/<str:room_name>/', consumers.ChatConsumer.as_asgi()),
]
