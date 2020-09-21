from django.urls import path
from norawebapp import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', views.index, name='index'),
    path('menu/', views.menu_list, name='menulist'),
    path('menu/create/', login_required(views.MenuFormView.as_view()), name='createmenu'),
    path('menu/edit/<uuid:id>/', login_required(views.MenuFormView.as_view()), name='editmenu'),
    path('menu/<uuid:id>/', views.MenuView.as_view(), name='menu'),
    path('employee/create/', login_required(views.EmployeeView.as_view()), name='createemployee'),
]
