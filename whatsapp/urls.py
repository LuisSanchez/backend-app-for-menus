from django.urls import path
from whatsapp import views

urlpatterns = [
    path("", views.MenuManagerView().as_view(), name="whatsapp"),
]
