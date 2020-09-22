from django.test import SimpleTestCase
from django.urls import reverse, resolve, exceptions
from norawebapp.views import menu_employees_list, admin_nora, admin_nora_create_dummy_users, admin_nora_send_slack_message, admin_nora_send_whatapp_message, MenuFormView, index, EmployeeView, menu_list, MenuView, EmployeeMenuView


class TestNorawebappUrls(SimpleTestCase):
    def test_index_resolves(self):
        url = reverse('index')
        self.assertEquals(resolve(url).func, index)

    def test_menu_list_should_not_resolve_due_decorator_staff(self):
        url = reverse('menulist')
        self.assertNotEqual(resolve(url).func, menu_list)

    def test_create_menu_resolves(self):
        url = reverse('createmenu')
        self.assertEquals(resolve(url).func.view_class, MenuFormView)

    def test_edit_menu_resolves(self):
        url = reverse('editmenu', kwargs={'id': 'aac0a02c-4af7-41a6-984e-e590db2ccc80'})
        self.assertEquals(resolve(url).func.view_class, MenuFormView)

    def test_edit_menu_should_not_resolve(self):
        try:
            url = reverse('editmenu', kwargs={'id': 'aac0a02c4af741a6984ee590db2ccc80'})
        except exceptions.NoReverseMatch:
            self.assertRaises(exceptions.NoReverseMatch)

    def test_menu_should_not_resolve(self):
        try:
            url = reverse('menu', kwargs={'id': 'aac0a02c4af741a6984ee590db2ccc80'})
        except exceptions.NoReverseMatch:
            self.assertRaises(exceptions.NoReverseMatch)

    def test_menu_resolves(self):
        url = reverse('menu', kwargs={'id': 'aac0a02c-4af7-41a6-984e-e590db2ccc80'})
        self.assertEquals(resolve(url).func.view_class, MenuView)

    def test_menu_employee_list_should_not_resolve_due_decorator_staff(self):
        url = reverse('menu_employee_list')
        self.assertNotEqual(resolve(url).func, menu_employees_list)

    def test_create_employee_resolves(self):
        url = reverse('createemployee')
        self.assertEquals(resolve(url).func.view_class, EmployeeView)

    def test_create_employee_menu_resolves(self):
        url = reverse('employeemenu')
        self.assertEquals(resolve(url).func.view_class, EmployeeMenuView)

    def test_admin_nora_should_not_resolve_due_decorator_staff(self):
        url = reverse('adminnora')
        self.assertNotEqual(resolve(url).func, admin_nora)

    def test_admin_nora_dummy_should_not_resolve_due_decorator_staff(self):
        url = reverse('adminnora_dummy')
        self.assertNotEqual(resolve(url).func, admin_nora_create_dummy_users)

    def test_admin_nora_broadcast_should_not_resolve_due_decorator_staff(self):
        url = reverse('adminnora_broadcast')
        self.assertNotEqual(resolve(url).func, admin_nora_send_slack_message)

    def test_admin_nora_whatsapp_should_not_resolve_due_decorator_staff(self):
        url = reverse('adminnora_menu')
        self.assertNotEqual(resolve(url).func, admin_nora_send_whatapp_message)
