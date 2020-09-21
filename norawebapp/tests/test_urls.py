from django.test import SimpleTestCase
from django.urls import reverse, resolve, exceptions
from norawebapp.views import MenuFormView, EmployeeView, menu_list, MenuView


class TestUrls(SimpleTestCase):

    def test_menu_list_resolves(self):
        url = reverse('menulist')
        self.assertEquals(resolve(url).func, menu_list)

    def test_create_menu_resolves(self):
        url = reverse('createmenu')
        self.assertEquals(resolve(url).func.view_class, MenuFormView)

    def test_menu_resolves(self):
        url = reverse('menu', kwargs={'id': 'aac0a02c-4af7-41a6-984e-e590db2ccc80'})
        self.assertEquals(resolve(url).func.view_class, MenuView)

    def test_menu_should_not_resolve(self):
        try:
            url = reverse('menu', kwargs={'id': 'aac0a02c4af741a6984ee590db2ccc80'})
        except exceptions.NoReverseMatch:
            self.assertRaises(exceptions.NoReverseMatch)

    def test_create_employee_resolves(self):
        url = reverse('createemployee')
        self.assertEquals(resolve(url).func.view_class, EmployeeView)
