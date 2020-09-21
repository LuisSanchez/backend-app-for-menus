from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('', include('norawebapp.urls')),
    path('api/whatsapp/', include('whatsapp.urls')),
    path('api/slack/', include('slackapp.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
]

urlpatterns += staticfiles_urlpatterns()
