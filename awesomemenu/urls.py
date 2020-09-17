from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('', include('norawebapp.urls')),
    path('whatsapp/', include('whatsapp.urls')),
    path('slack/', include('slack.urls')),
]

urlpatterns += staticfiles_urlpatterns()
