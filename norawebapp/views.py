from django.shortcuts import render
from norawebapp.forms import MenuForm
from norawebapp.models import Menu as MenuModel
from rest_framework.views import APIView


def index(request):
    return render(request, "norawebapp/index.html")


class Menu(APIView):
    ''' Retrieve menu of the day by its uuid '''
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

class MenuFormView(APIView):
    form_class = MenuForm
    template_name = "norawebapp/createMenu.html"

    def get(self, request):
        form = self.form_class(request.GET or None)
        return render(request, self.template_name, {'form': form})

    ''' Creates the menu '''
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST or None)
        menu_instance = MenuModel()
        
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
            render(request, self.template_name)

        return render(request, "norawebapp/index.html")
