from django.conf import settings
from django.shortcuts import redirect, render
from norawebapp.forms import EmployeeForm, MenuForm, EmployeeMenuForm
from norawebapp.models import EmployeeMenu, Employee, Menu as MenuModel
from rest_framework.views import View
from whatsapp.views import WhatsappView
from datetime import date


def index(request):
    menu = MenuModel()
    menu = menu.get_menu_by_date(date.today())
    return render(request, "norawebapp/index.html", { 'menu': menu.first() })

def menu_list(request):
    menus = EmployeeMenu.objects.all()
    return render(request, 'norawebapp/menu-list.html', { 'menus': menus })

def send_whatsapp_message_with_menu(menu: MenuModel, from_, to_):
    if (len(menu) != 0):
        request = {
            'message': str(menu), 
            'from': settings.TWILIO_TO_WHATSAPP, 
            'to': settings.TWILIO_FROM_WHATSAPP
        }

    menu_view = MenuManagerView()
    response = menu_view.post(request)
    return response


class MenuView(View):
    template_name = "norawebapp/menu.html"

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

        return render(request, self.template_name, context)


class MenuFormView(View):
    form_class = MenuForm
    template_name = "norawebapp/create-menu.html"
    
    def get(self, request, **kwargs):
        ''' Sets a particular menu or initializes it for creation '''
        menu_id = kwargs.get('id', None)

        if menu_id == None:
            form = self.form_class(request.GET or None)    
        else:
            menu = MenuModel.objects.get(id=menu_id)
            form = MenuForm(instance=menu)
        
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        ''' Saves the menu '''
        menu = MenuModel()
        menu_id = kwargs.get('id', None)
        
        if (menu_id is not None):
            menu = MenuModel.objects.get(id=menu_id)

        form = self.form_class(request.POST, instance=menu)
    
        if form.is_valid():
            # need to check if the menu exists for that day
            if (len(menu.get_menu_by_date(form.cleaned_data['date'])) > 0) and (menu_id is None):
                message = "El menú ya existe para ese día"
                return render(request, self.template_name, {"form": form, "message": message})
            else:
                form.save()
                return redirect("index")
        else:
            return render(request, self.template_name)

class EmployeeView(View):
    form_class = EmployeeForm
    template_name = "norawebapp/employee.html"

    def get(self, request):
        form = self.form_class(request.GET or None)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST or None)
        
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            return render(request, self.template_name)

class EmployeeMenuView(View):
    form_class = EmployeeMenuForm
    template_name = "norawebapp/employee-menu.html"

    def get(self, request):
        form = self.form_class(request.GET or None)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST or None)
        
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            return render(request, self.template_name)
