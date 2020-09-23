import requests
from django.conf import settings
from norawebapp.models import Menu
from django.urls import reverse

def send_whatsapp_message_with_menu(menu: Menu):
    """
        Helper to send the whatsapp message to the employees on the sandbox
    """
    url = reverse('whatsapp')
    payload = dict(message=str(menu), from_=settings.TWILIO_FROM_WHATSAPP, to_=settings.TWILIO_TO_WHATSAPP)
    response = requests.post(settings.BASE_URL_SERVER + url, data=payload)
    print(response)
    
    return response
