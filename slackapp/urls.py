from django.urls import path
from slackapp import views


urlpatterns = [
    path("", views.index, name="slackapp"),
]
