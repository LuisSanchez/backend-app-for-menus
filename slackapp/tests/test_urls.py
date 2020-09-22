from django.test import SimpleTestCase
from django.urls import reverse, resolve
from slackapp.views import SlackView


class TestUrls(SimpleTestCase):
    def test_slack_view_resolves(self):
        url = reverse('slackapp')
        self.assertEquals(resolve(url).func.view_class, SlackView)
