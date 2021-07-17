from twilio.rest import Client


def twillioSend(message, to):
    #add account information here
    # account_sid =
    # auth_token =
    account_sid = "AC6740392069dc8e4d4175d1c17bee3748"
    auth_token = "a0c3d0cd9db753d63f1f1cf32d4520d8"
    client = Client(account_sid, auth_token)
    message = client.messages \
                .create(
                     body=message,
                     from_='+18042774771',
                     to=to
                 )

