from django.urls import path
from whatsapp import views

urlpatterns = [
    path("", views.index, name="index"),
]
