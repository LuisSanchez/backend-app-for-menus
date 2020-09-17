from twilio.rest import Client
from django.conf import settings


def sendTestMessage():
    account_sid = settings.TWILIO_ACCOUNT_SID
    auth_token = settings.TWILIO_AUTH_TOKEN
    client = Client(account_sid, auth_token) 
    
    menu_of_the_day = '''Hola!
Dejo el menú de hoy :)
Opción 1: Pastel de choclo, Ensalada y Postre
Opción 2. Arroz con nugget de pollo, Ensalada y Postre
Opción 3: Arroz con hamburguesa, Ensalada y Postre
Opción 4: Ensalada premium de pollo y Postre
Tengan lindo día!
'''

    message = client.messages.create( 
                                from_=settings.TWILIO_FROM_WHATSAPP,  
                                body=menu_of_the_day,      
                                to=settings.TWILIO_TO_WHATSAPP
                            ) 
    
    return message.sid
