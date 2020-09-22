from django.urls import reverse
from django.contrib.auth.models import User
from django.test import TestCase, RequestFactory
from slackapp.views import SlackView

class TestSlackappViews(TestCase):
    
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            username='luis', email='luis@…', password='palta')

    def test_slackapp_GET_request_should_return_405(self):
        url = reverse('slackapp')
        request = self.factory.get(url)
        request.user = self.user
        response = SlackView.as_view()(request)
        self.assertEqual(response.status_code, 405)

    def test_slackapp_POST_request_should_return_403(self):
        url = reverse('slackapp')
        request = self.factory.post(url)
        request.user = self.user
        response = SlackView.as_view()(request)
        self.assertEqual(response.status_code, 403)
