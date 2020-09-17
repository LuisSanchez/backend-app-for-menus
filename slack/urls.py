from django.urls import path
from slack import views


urlpatterns = [
    path("", views.index, name="slack"),
]
