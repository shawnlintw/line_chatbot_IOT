#line_chatbot_IOT/routing.py

from django.conf.urls import url

from . import rpitest

websocket_urlpatterns = [
        
        url(r'^rpitest/$',rpitest.RpiConsumer),
        
        ]
