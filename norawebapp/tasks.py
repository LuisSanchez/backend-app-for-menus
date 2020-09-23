from norawebapp.helpers.slack_manager import broadcast_message_on_slack_channel
from norawebapp.models import Menu
from datetime import date
from awesomemenu.celery import app

# For some reason on windows 10 I cannot put this file in a tasks folder

@app.task
def send_slack_reminder():
    """
        Task to send the slack message
    """
    menu = Menu.objects.filter(date=date.today())

    if (len(menu) > 0):
        response = broadcast_message_on_slack_channel(menu.first())
    else:
        response = 'No existe aún menú del día'
        print(response)

    return response
