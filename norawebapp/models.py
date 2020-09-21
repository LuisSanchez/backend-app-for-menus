import uuid
from django.db import models
from django.contrib.auth.models import User


class Menu(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    option_one = models.CharField(max_length=100)
    option_two = models.CharField(max_length=100)
    option_three = models.CharField(max_length=100)
    option_four = models.CharField(max_length=100)
    date = models.DateField()
    creation_date = models.DateField(auto_now=True)

    def get_menu_by_date(self, date_of_menu):
        return Menu.objects.filter(date=date_of_menu)

    def __str__(self):
        return (f"Hola!\n"
                f"Dejo el menú de hoy :)\n"
                f"Opción 1: {self.option_one}\n"
                f"Opción 2: {self.option_two}\n"
                f"Opción 3: {self.option_three}\n"
                f"Opción 4: {self.option_four}\n"
                f"Tengan lindo día!")


class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=100)


class EmployeeMenu(models.Model):
    employee = models.ForeignKey('Employee', on_delete=models.DO_NOTHING)
    menu = models.ForeignKey('Menu', on_delete=models.DO_NOTHING)
    comment = models.CharField(max_length=100)
    option_selected = models.CharField(max_length=100)
    date = models.DateField(auto_now=True)

    def get_menus_of_employee_by_menu_id(self, menu_id):
        return EmployeeMenu.objects.filter(menu=menu_id)
