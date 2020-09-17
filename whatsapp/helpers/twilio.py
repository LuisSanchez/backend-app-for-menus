from twilio.rest import Client
from django.conf import settings
from norawebapp.models import Menu


def sendTestMessage(menu: Menu, numbers, url):
    account_sid = settings.TWILIO_ACCOUNT_SID
    auth_token = settings.TWILIO_AUTH_TOKEN
    client = Client(account_sid, auth_token) 
    
    menu_of_the_day = (f"Hola!\n"
                       f"Dejo el menú de hoy :)\n"
                       f"Opción 1: {menu.option_one}\n"
                       f"Opción 2: {menu.option_two}\n"
                       f"Opción 3: {menu.option_three}\n"
                       f"Opción 4: {menu.option_four}\n"
                       f"Tengan lindo día!")

    message = client.messages.create( 
                                from_=settings.TWILIO_FROM_WHATSAPP,  
                                body=menu_of_the_day,      
                                to=settings.TWILIO_TO_WHATSAPP) 
    
    return message.sid
