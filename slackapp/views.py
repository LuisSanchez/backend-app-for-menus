from django.http import HttpResponse


def index(context):
    return HttpResponse('<h2>Slack</h2>')
