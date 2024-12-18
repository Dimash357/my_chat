import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from chat_app.urls import websocket_urlpatterns  # Импорт WebSocket маршрутов

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_settings.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),  # HTTP запросы
    "websocket": AuthMiddlewareStack(
        URLRouter(
            websocket_urlpatterns  # Маршруты WebSocket
        )
    ),
})
