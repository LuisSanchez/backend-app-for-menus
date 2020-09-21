from whatsapp.helpers.twilio import send_whatsapp_message
from rest_framework.views import APIView
from .helpers import twilio
from rest_framework.response import Response
from rest_framework import status


class WhatsappView(APIView):
    def post(self, request, *args, **kwargs):
        message = request.data['message']
        from_ = request.data['from']
        to_ = request.data['to']
        
        response = send_whatsapp_message(message, to_, from_)

        return Response(response, status=status.HTTP_200_OK)
