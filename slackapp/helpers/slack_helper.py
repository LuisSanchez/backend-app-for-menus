import logging
logging.basicConfig(level=logging.DEBUG)

import os
from slack import WebClient
from slack.errors import SlackApiError
from django.conf import settings

def slackTest():
    slack_token = settings.SLACK_TOKEN
    client = WebClient(token=slack_token)

    try:
        response = client.chat_postMessage(
            channel = settings.SLACK_CHANNEL,
            text="Hello again from your app! :tada:"
        )
    except SlackApiError as e:
        # You will get a SlackApiError if "ok" is False
        assert e.response["error"]  # str like 'invalid_auth', 'channel_not_found'
