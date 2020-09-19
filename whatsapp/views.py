from twilio.rest.api.v2010.account import message
from whatsapp.helpers.twilio import send_whatsapp_message
from django.http import HttpResponse
from rest_framework.views import APIView
from .helpers import twilio
from rest_framework.response import Response
from rest_framework import status


class MenuManagerView(APIView):
    def get (self, *args):
        return Response('<h2>whatsapp</h2>', status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        message = request.data['message']
        from_ = request.data['from']
        to_ = request.data['to']
        
        response = send_whatsapp_message(message, to_, from_)

        return Response(response, status=status.HTTP_201_CREATED)
