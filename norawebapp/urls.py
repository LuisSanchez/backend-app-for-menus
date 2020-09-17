from django.urls import path
from norawebapp import views

urlpatterns = [
    path("", views.index, name="index"),
]
