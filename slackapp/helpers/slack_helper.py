import logging
from django.core.checks import messages
logging.basicConfig(level=logging.DEBUG)

from slack import WebClient
from slack.errors import SlackApiError
from django.conf import settings

def send_slack_message(message, channel):
    slack_token = settings.SLACK_TOKEN
    client = WebClient(token=slack_token)

    try:
        response = client.chat_postMessage(
            channel = channel,
            text=message
        )
        return response.data
    except SlackApiError as e:
        # You will get a SlackApiError if "ok" is False
        return e.response["error"]  # str like 'invalid_auth', 'channel_not_found'
