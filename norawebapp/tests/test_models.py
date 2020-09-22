from django.test import TestCase
from norawebapp.models import Menu
from datetime import date


class TestNorawebappModels(TestCase):
    menu_expected_date = date(2020, 1, 1)
    menu_expected = {}

    def setUp(self):
        self.menu_expected = Menu.objects.create(
            option_one='one',
            option_two='two',
            option_three='three',
            option_four='four',
            date=self.menu_expected_date)
        
    def test_menu_str_format(self):
        expected_value = Menu.objects.filter(date=self.menu_expected_date).first()
        menu_of_the_day = (f"Hola!\n"
                           f"Dejo el menú de hoy :)\n"
                           f"Opción 1: {self.menu_expected.option_one}\n"
                           f"Opción 2: {self.menu_expected.option_two}\n"
                           f"Opción 3: {self.menu_expected.option_three}\n"
                           f"Opción 4: {self.menu_expected.option_four}\n"
                           f"Tengan lindo día!")
        self.assertEqual(menu_of_the_day, str(expected_value))
