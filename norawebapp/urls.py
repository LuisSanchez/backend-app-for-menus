from django.urls import path
from norawebapp import views

urlpatterns = [
    path("", views.index, name="index"),
    path("menu/create", views.createMenu, name="createmenu"),
    path("menu/<uuid:id>", views.Menu.as_view(), name="menu"),
]