from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .helpers.slack_helper import send_slack_message


class SlackView(APIView):
    def post(self, request, *args, **kwargs):
        message = request.data.get("message")
        channel = request.data.get("channel")
        response = send_slack_message(message, channel) 
        return Response(response, status=status.HTTP_200_OK)
