import requests
from django.conf import settings
from django.urls import reverse
from norawebapp.models import Menu
from datetime import date

def send_slack_reminder():
    menu = Menu()
    menu = menu.get_menu_by_date(date.today())

    if (len(menu) > 0):
        url = reverse('slackapp')
        url_to_menu = reverse('menu', kwargs={'id': menu.first().id})
        link_to_menu = settings.BASE_URL_SERVER + url_to_menu
        message = f"Hola! Recuerda seleccionar tu opción de menú antes de las 11am! :hamburger: :taco: :tada: \n {link_to_menu}"
        payload = dict(message=message, channel=settings.SLACK_CHANNEL)
        response = requests.post(settings.BASE_URL_SERVER + url, data=payload)
    else:
        response = 'No existe aún menú del día'
        print(response)

    return response
