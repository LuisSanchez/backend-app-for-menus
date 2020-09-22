from django.conf import settings
from django.core.checks import messages
from django.shortcuts import redirect, render
from norawebapp.forms import EmployeeForm, MenuForm, EmployeeMenuForm
from norawebapp.models import EmployeeMenu, Employee as EmployeeModel, Menu as MenuModel
from norawebapp.helpers.whatsapp_manager import send_whatsapp_message_with_menu
from norawebapp.helpers.default_users import persist_random_users
from norawebapp.helpers.slack_manager import broadcast_message_on_slack_channel
from rest_framework.views import View
from datetime import date
from django.contrib.auth.models import User


def index(request):
    menu = MenuModel()
    menu = menu.get_menu_by_date(date.today())
    return render(request, "norawebapp/index.html", { 'menu': menu.first() })

def menu_list(request):
    menus = EmployeeMenu.objects.all()
    return render(request, 'norawebapp/menu-list.html', { 'menus': menus })

def admin_nora(request):
    return render(request, 'norawebapp/admin-nora.html')

def admin_nora_create_dummy_users(request):
    message = persist_random_users()
    print(message)
    return render(request, 'norawebapp/admin-nora.html', { 'message': message })

def admin_nora_send_whatapp_message(request):
    menu = MenuModel()
    menu = menu.get_menu_by_date(date.today())
    response = send_whatsapp_message_with_menu(menu.first())
    print(response)
    return render(request, 'norawebapp/admin-nora.html', { 'message': response })

def admin_nora_send_slack_message(request):
    menu = MenuModel()
    menu = menu.get_menu_by_date(date.today())
    response = broadcast_message_on_slack_channel(menu.first())
    print(response)
    return render(request, 'norawebapp/admin-nora.html', { 'message': response })


class MenuView(View):
    template_name = "norawebapp/menu.html"

    def get(self, request, **kwargs):
        ''' Retrieve menu of the day by its uuid '''
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
                # if the menu was saved today, a whatsapp message is sent
                if (settings.TWILIO_SEND_MESSAGE_ON_SAVE_MENU and form.cleaned_data['date'] == date.today()):
                    send_whatsapp_message_with_menu(form.instance)
                
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
        menu = MenuModel.objects.filter(date=date.today())
        employee = EmployeeModel.objects.get(user_id=request.user.id)
        employeeMenu = EmployeeMenu.objects.filter(date=date.today(), employee_id=employee.id)

        if (len(menu) == 0):
            return render(request, self.template_name, {'message': 'No se ha creado menú del día'})
        elif (len(employeeMenu)) :
            return render(request, self.template_name, {'message': 'Ya tiene un menú seleccionado para hoy'})
        else:
            form = self.form_class(request.GET or None, initial={'employee': employee, 'menu': menu.first()})
            return render(request, self.template_name, {'form': form, 'menu': menu.first()})

    def post(self, request, *args, **kwargs):
        menu = MenuModel.objects.filter(date=date.today())
        employee = EmployeeModel.objects.get(user_id=request.user.id)

        form = self.form_class(request.POST or None, initial={'employee': employee, 'menu': menu.first()})
        
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            return render(request, self.template_name)
