from django import forms
from norawebapp.models import Menu
from datetime import date

class MenuForm(forms.ModelForm):
    class Meta:
        model = Menu
        fields = '__all__'
