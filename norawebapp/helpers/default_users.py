from django.contrib.auth.models import User

users = ['luis', 'manuel', 'pedro', 'juan', 'diego']

for user in users:
    user = User.objects.create_user(user, f'{user}@nora.luis.cornershopapp.com', f'{user}2020')
    user.save()

print(f'default users added, phone numbers and authorization\n'
      f'in whatsapp sandbox needs to be added, \n'
      f'just send a WhatsApp message to +1 415 523 8886 with code "join worry-hello"')
