from django.contrib.auth.models import User
import random

def persist_random_users():
    users_list = ['luis', 'manuel', 'pedro', 'juan', 'diego']
    
    for user_name in users_list:
        suffix = random.randint(10, 9999)
        username = user_name + str(suffix)
        user = User.objects.create_user(user_name, f'{username}@nora.luis.cornershopapp.com', f'{username}2020')
        user.save()

    message = (f'default users added, phone numbers and authorization\n'
               f'in whatsapp sandbox needs to be added, \n'
               f'just send a WhatsApp message to +1 415 523 8886 with code "join worry-hello"')
    print(message)

    return message
