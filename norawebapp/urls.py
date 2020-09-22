from os import name
from django.urls import path
from norawebapp import views
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required


urlpatterns = [
    path('', views.index, name='index'),
    path('menu/', staff_member_required(views.menu_list, login_url='employeemenu'), name='menulist'),
    path('menu/create/', staff_member_required(views.MenuFormView.as_view(), login_url='employeemenu'), name='createmenu'),
    path('menu/edit/<uuid:id>/', staff_member_required(views.MenuFormView.as_view(), login_url='employeemenu'), name='editmenu'),
    path('menu/<uuid:id>/', views.MenuView.as_view(), name='menu'),
    path('employee/create/', staff_member_required(views.EmployeeView.as_view(), login_url='employeemenu'), name='createemployee'),
    path('employee/menu/', login_required(views.EmployeeMenuView.as_view(), login_url='employeemenu'), name='employeemenu'),
]
