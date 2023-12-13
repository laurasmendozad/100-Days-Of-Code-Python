''' Notification Manager '''
from twilio.rest import Client

TWILIO_SID = 'ACe528d6d1e05084df6b094a4a31483798'
TWILIO_AUTH_TOKEN = '8afe64d1934234777ed7589c880a30f1'
TWILIO_VIRTUAL_NUMBER = '+13613384592'
TWILIO_VERIFIED_NUMBER = '+573178923835'


class NotificationManager:
    ''' Notification Manager '''
    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        ''' Send SMS '''
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        print(message.sid)
