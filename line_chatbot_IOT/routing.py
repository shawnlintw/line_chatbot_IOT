#line_chatbot_IOT/routing.py
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
import RPiGpio.routing

application = ProtocolTypeRouter ({
    #(http -> django view is added by default)
    'websocket' : AuthMiddlewareStack(
        URLRouter(
            RPiGpio.routing.websocket_urlpatterns
            )
        ),
    })
