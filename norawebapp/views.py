from django.shortcuts import render
from norawebapp.forms import MenuForm
from norawebapp.models import Menu as MenuModel
from rest_framework.views import APIView

def index(request):
    return render(request, "norawebapp/index.html")

def createMenu(request):
    form = MenuForm(request.POST or None)
    menu_instance = MenuModel()

    if request.method == "POST":
        if form.is_valid():
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

class Menu(APIView):
    """ Retrieve the TMC year and month """
    def get(self, request, **kwargs):
        id = kwargs.get('id', None)
        if id == None:
            context = {
                "message": "Menú inválido...",
            }
            return render(request, "norawebapp/index.html", context)

        menu_instance = MenuModel.objects.get(id=id)
        context = {
            "op1": menu_instance.option_one,
            "op2": menu_instance.option_two,
            "op3": menu_instance.option_three,
            "op4": menu_instance.option_four,
        }
        return render(request, "norawebapp/menu.html", context)