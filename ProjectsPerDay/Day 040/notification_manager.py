''' Notification Manager '''
import os
from twilio.rest import Client

TWILIO_SID = os.environ["TWILIO_ACCOUNT_SID"]
TWILIO_AUTH_TOKEN = os.environ["TWILIO_AUTH_TOKEN"]
TWILIO_VIRTUAL_NUMBER = '+12015146534'
TWILIO_VERIFIED_NUMBER = os.environ["PHONE"]


class NotificationManager:
    ''' Notification Manager '''
    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        ''' Send SMS '''
        print(message)
        # message = self.client.messages.create(
        #     body=message,
        #     from_=TWILIO_VIRTUAL_NUMBER,
        #     to=TWILIO_VERIFIED_NUMBER,
        # )
