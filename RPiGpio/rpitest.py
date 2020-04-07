# RPiGpio/consumer.py

#from asgiref.sync import async_to_sync 
from channels.generic.websocket import WebsocketConsumer
from RPiGpio.models import RPiGpio_model 
import json

class RpiConsumer(WebsocketConsumer):

    def connect(self):
        self.accept()

    def disconnect(self, close_code):
        pass

    def receive(self, text_data):
        
        text_data_json = json.loads(text_data)

        message = text_data_json['message']

        if message != "get gpio":
            message = "No echo"

            self.send(text_data=json.dumps
                    ({
                        'message' : message,
                }))
        else:
            data = list(RPiGpio_model.objects.values_list('cPinNum','cGPIO_Value'))

            self.send(text_data=json.dumps({
                'message' : data,
                }))
