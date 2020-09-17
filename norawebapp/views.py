from django.shortcuts import render
from django.http import HttpResponse
from norawebapp.forms import MenuForm
from norawebapp.models import Menu
from datetime import date

def index(request):
    return render(request, "norawebapp/index.html")

def createMenu(request):
    form = MenuForm(request.POST or None)
    menu_instance = Menu()

    if request.method == "POST":
        if form.is_valid():
            message = "Los días de plazo no pueden ser mayores al cálculo de la tmc, intente nuevamente"
            menu_instance.option_one = form.cleaned_data['option_one']
            menu_instance.option_two = form.cleaned_data['option_two']
            menu_instance.option_three = form.cleaned_data['option_three']
            menu_instance.option_four = form.cleaned_data['option_four']
            menu_instance.date = form.cleaned_data['date']
            menu_instance.save()
            # need to check if the menu exists for that date
            # message = "El menú ya existe para ese día"
            # return render(request, "norawebapp/createMenu.html", {"form": form, "message": message})

            context = {
                "message": "Menu ingresado!",
            }
            return render(request, "norawebapp/index.html", context)
        else:
            render(request, "norawebapp/createMenu.html")
    else:
        return render(request, "norawebapp/createMenu.html", {"form": form})

    