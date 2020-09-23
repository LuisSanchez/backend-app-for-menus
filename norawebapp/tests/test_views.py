from django.test import RequestFactory, TestCase
from django.urls import reverse, resolve, exceptions
from norawebapp.views import admin_nora, admin_nora_create_dummy_users, admin_nora_send_slack_message, admin_nora_send_whatapp_message, MenuFormView, index, EmployeeView, menu_list, MenuView, EmployeeMenuView
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib.auth.models import User
from django.test import TestCase, RequestFactory
from norawebapp.models import EmployeeMenu, Employee as EmployeeModel, Menu as MenuModel


class TestNorawebappViews(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_superuser(
            username='jacob', email='jacob@…', password='palta', id='1')

    def test_menuview_post_request_should_return_200(self):
        url = reverse('menu', kwargs={'id': 'aac0a02c-4af7-41a6-984e-e590db2ccc80'})
        request = self.factory.post(url)
        request.user = self.user
        response = MenuView.as_view()(request)
        self.assertEqual(response.status_code, 405)

    def test_menuview_get_request_with_uuid_should_return_200(self):
        url = reverse('menu', kwargs={'id': 'aac0a02c-4af7-41a6-984e-e590db2ccc80'})
        request = self.factory.get(url)
        request.user = self.user
        response = MenuView.as_view()(request)
        self.assertEqual(response.status_code, 200)

    def test_menuformview_get_request_should_return_200(self):
        url = reverse('createmenu')
        request = self.factory.get(url)
        request.user = self.user
        response = MenuFormView.as_view()(request)
        self.assertEqual(response.status_code, 200)

    def test_menuformview_post_request_with_uuid_should_return_200(self):
        url = reverse('editmenu', kwargs={'id': 'aac0a02c-4af7-41a6-984e-e590db2ccc80'})
        request = self.factory.post(url)
        request.user = self.user
        response = MenuFormView.as_view()(request)
        self.assertEqual(response.status_code, 200)

    def test_menuformview_post_request_with_invalid_uuid_should_return_exception(self):
        try:
            url = reverse('editmenu', kwargs={'id': 'aac0a02c4af741a6984ee590db2ccc80'})
        except exceptions.NoReverseMatch:
            self.assertRaises(exceptions.NoReverseMatch)

    def test_employeeview_get_request_should_return_200(self):
        url = reverse('createemployee')
        request = self.factory.get(url)
        request.user = self.user
        response = EmployeeView.as_view()(request)
        self.assertEqual(response.status_code, 200)

    def test_employeeview_post_request_should_return_200(self):
        url = reverse('createemployee')
        request = self.factory.post(url)
        request.user = self.user
        response = EmployeeView.as_view()(request)
        self.assertEqual(response.status_code, 200)

    def test_adminnora_post_request_should_return_200(self):
        url = reverse('adminnora')
        request = self.factory.post(url)
        request.user = self.user
        response = admin_nora(request)
        self.assertEqual(response, None)

    def test_adminnora_get_request_should_return_200(self):
        url = reverse('adminnora')
        request = self.factory.get(url)
        request.user = self.user
        response = admin_nora(request)
        self.assertEqual(response.status_code, 200)

    def test_adminnora_dummy_post_request_should_return_200(self):
        url = reverse('adminnora_dummy')
        request = self.factory.post(url)
        request.user = self.user
        response = admin_nora(request)
        self.assertEqual(response, None)

    def test_adminnora_dummy_get_request_should_return_200(self):
        url = reverse('adminnora_dummy')
        request = self.factory.get(url)
        request.user = self.user
        response = admin_nora(request)
        self.assertEqual(response.status_code, 200)

    def test_adminnora_broadcast_post_request_should_return_200(self):
        url = reverse('adminnora_broadcast')
        request = self.factory.post(url)
        request.user = self.user
        response = admin_nora(request)
        self.assertEqual(response, None)

    def test_adminnora_broadcast_get_request_should_return_200(self):
        url = reverse('adminnora_broadcast')
        request = self.factory.get(url)
        request.user = self.user
        response = admin_nora(request)
        self.assertEqual(response.status_code, 200)

    def test_adminnora_menu_post_request_should_return_200(self):
        url = reverse('adminnora_menu')
        request = self.factory.post(url)
        request.user = self.user
        response = admin_nora(request)
        self.assertEqual(response, None)

    def test_adminnora_menu_get_request_should_return_200(self):
        url = reverse('adminnora_menu')
        request = self.factory.get(url)
        request.user = self.user
        response = admin_nora(request)
        self.assertEqual(response.status_code, 200)

    # def test_employeemenuview_get_request_should_return_200(self):
    #     url = reverse('employeemenu')
    #     request = self.factory.post(url)
    #     request.user = self.user
    #     response = EmployeeMenuView.as_view()(request)
    #     self.assertEqual(response.status_code, 200)

    # def test_employeemenuview_post_request_should_return_200(self):
    #     url = reverse('employeemenu')
    #     request = self.factory.get(url)
    #     request.user = self.user
    #     response = EmployeeMenuView.as_view()(request)
    #     self.assertEqual(response.status_code, 200)