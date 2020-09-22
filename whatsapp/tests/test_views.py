from django.urls import reverse
from django.contrib.auth.models import User
from django.test import TestCase, RequestFactory
from whatsapp.views import WhatsappView

class TestWhatsappViews(TestCase):

    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            username='luis', email='luis@…', password='palta')

    def test_whatsapp_GET_request_should_return_405(self):
        url = reverse('whatsapp')
        request = self.factory.get(url)
        request.user = self.user
        response = WhatsappView.as_view()(request)
        self.assertEqual(response.status_code, 405)

    def test_whatsapp_POST_request_should_return_403(self):
        url = reverse('whatsapp')
        request = self.factory.post(url)
        request.user = self.user
        response = WhatsappView.as_view()(request)
        self.assertEqual(response.status_code, 403)
