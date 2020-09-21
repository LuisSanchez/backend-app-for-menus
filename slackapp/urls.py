from django.urls import path
from slackapp import views


urlpatterns = [
    path("", views.SlackView.as_view(), name="slackapp"),
]
