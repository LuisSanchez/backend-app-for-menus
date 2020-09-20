from django.conf import settings
from django.shortcuts import render
from norawebapp.forms import MenuForm
from norawebapp.models import Menu as MenuModel
from rest_framework.views import APIView
from whatsapp.views import MenuManagerView
from datetime import date

from slackapp.helpers.slack_helper import slackTest

def index(request):
    #send_whatsapp_message_with_menu(None, "", "")
    return render(request, "norawebapp/index.html")

def send_whatsapp_message_with_menu(menu: MenuModel, from_, to_):
    if (len(menu) != 0):
        menu_of_the_day = (f"Hola!\n"
                        f"Dejo el menú de hoy :)\n"
                        f"Opción 1: {menu.option_one}\n"
                        f"Opción 2: {menu.option_two}\n"
                        f"Opción 3: {menu.option_three}\n"
                        f"Opción 4: {menu.option_four}\n"
                        f"Tengan lindo día!")
        request = {
            'message': menu_of_the_day, 
            'from': settings.TWILIO_TO_WHATSAPP, 
            'to': settings.TWILIO_FROM_WHATSAPP
        }

    #menu_view = MenuManagerView()
    #response = menu_view.post(request)
    ##return response
    return None

def get_menu_of_the_day(date_of_menu):
    return MenuModel.objects.filter(date=date_of_menu)

class Menu(APIView):
    ''' Retrieve menu of the day by its uuid '''
    def get(self, request, **kwargs):
        id = kwargs.get('id', None)
        if id == None:
            context = { "message": "Menú inválido..." }

        try:
            menu_instance = MenuModel.objects.get(id=id)
            context = {
                "op1": menu_instance.option_one,
                "op2": menu_instance.option_two,
                "op3": menu_instance.option_three,
                "op4": menu_instance.option_four,
            }
        except MenuModel.DoesNotExist:
            context = { "message": "Menú inválido..." }

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

            # need to check if the menu exists for that day
            if (len(get_menu_of_the_day(menu_instance.date)) != 0):
                message = "El menú ya existe para ese día"
                return render(request, "norawebapp/createMenu.html", {"form": form, "message": message})
            else:
                menu_instance.save()
                context = {
                    "message": "Menu ingresado!",
                }
                return render(request, "norawebapp/index.html", context)
        else:
            render(request, self.template_name)

        return render(request, "norawebapp/index.html")

    def put(self, request, *args, **kwargs):
        menu_of_the_day = get_menu_of_the_day(date.today())
        form = self.form_class(request.POST or None)
