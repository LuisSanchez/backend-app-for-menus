from django.test import SimpleTestCase
from django.urls import reverse, resolve
from whatsapp.views import WhatsappView


class TestUrls(SimpleTestCase):

    def test_whatsapp_view_resolves(self):
        url = reverse('whatsapp')
        self.assertEquals(resolve(url).func.view_class, WhatsappView)
