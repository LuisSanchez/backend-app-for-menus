import requests
from django.conf import settings
from django.urls import reverse
from norawebapp.models import Menu

def broadcast_message_on_slack_channel(menu: Menu):
    ''' 
        Sends the reminder to the channel configured on slack
    '''
    url = reverse('slackapp')
    url_to_menu = reverse('menu', kwargs={'id': menu.id})
    link_to_menu = settings.BASE_URL_SERVER + url_to_menu
    message = f"Hola! Recuerda seleccionar tu opción de menú antes de las 11am! :hamburger: :avocado: :taco: :tada: \n {link_to_menu}"
    payload = dict(message=message, channel=settings.SLACK_CHANNEL)
    response = requests.post(settings.BASE_URL_SERVER + url, data=payload)
    print(response)

    return response
