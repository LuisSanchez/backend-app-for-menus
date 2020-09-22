from twilio.rest import Client
from django.conf import settings


def send_whatsapp_message(message, from_, to_):
    account_sid = settings.TWILIO_ACCOUNT_SID
    auth_token = settings.TWILIO_AUTH_TOKEN
    client = Client(account_sid, auth_token)

    message = client.messages.create(
                                from_=from_,
                                body=message,
                                to=to_)
    return message.sid
