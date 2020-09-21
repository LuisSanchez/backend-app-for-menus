import uuid
from django.db import models


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

class Employee(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)

class EmployeeMenu(models.Model):
    employee = models.ForeignKey('Employee', on_delete=models.DO_NOTHING)
    menu = models.ForeignKey('Menu', on_delete=models.DO_NOTHING)
    comment = models.CharField(max_length=100)
    option_selected = models.CharField(max_length=100)
    date = models.DateField(auto_now=True) 
