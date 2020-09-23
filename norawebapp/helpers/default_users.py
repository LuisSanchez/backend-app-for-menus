from django.conf import settings
from django.contrib.auth.models import User
import random

def persist_random_users():
    """
        Creates dummy users on the database without phone number
    """
    users_list = ['luis', 'manuel', 'pedro', 'juan', 'diego']
    
    for user_name in users_list:
        suffix = random.randint(10, 9999)
        username = user_name + str(suffix)
        user = User.objects.create_user(username, f'{username}@nora.luis.cornershopapp.com', f'{username}2020')
        user.save()

    message = (f'Default users added.\n'
               f'Phone numbers and authorization for whatsapp sandbox(twilio) needs to be configured. \n'
               f'Send the WhatsApp message "join worry-hello" from your phone to {settings.TWILIO_FROM_WHATSAPP}')
    print(message)

    return message
