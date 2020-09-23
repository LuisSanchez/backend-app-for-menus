from norawebapp.helpers.slack_manager import broadcast_message_on_slack_channel
from norawebapp.models import Menu
from datetime import date
from awesomemenu.celery import app

@app.task
def send_slack_reminder():
    menu = Menu.objects.filter(date=date.today())
    print(menu)

    if (len(menu) > 0):
        response = broadcast_message_on_slack_channel(menu.first())
        pass
    else:
        response = 'No existe aún menú del día'
        print(response)

    return response
