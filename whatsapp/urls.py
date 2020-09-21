from django.urls import path
from whatsapp import views

urlpatterns = [
    path("", views.WhatsappView.as_view(), name="whatsapp"),
]
