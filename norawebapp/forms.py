from django import forms
from django.db.models import fields
from django.forms.models import model_to_dict
from norawebapp.models import Employee, Menu, EmployeeMenu


class MenuForm(forms.ModelForm):
    class Meta:
        model = Menu
        fields = '__all__'

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'

class EmployeeMenuForm(forms.ModelForm):
    class Meta:
        model = EmployeeMenu
        fields = '__all__'
