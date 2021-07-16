import os
from twilio.rest import Client


def twillioSend(message, to):
    
    client = Client(account_sid, auth_token)
    message = client.messages \
                .create(
                     body=message,
                     from_='+18042774771',
                     to=to
                 )

