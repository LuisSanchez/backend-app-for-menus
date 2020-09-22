from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .helpers.twilio import send_whatsapp_message


class WhatsappView(APIView):
    
    def post(self, request, *args, **kwargs):
        message = request.data['message']
        from_ = request.data['from_']
        to_ = request.data['to_']

        response = send_whatsapp_message(message, from_, to_)
        return Response(response, status=status.HTTP_200_OK)
