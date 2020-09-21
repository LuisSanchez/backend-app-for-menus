from django.urls import path
from norawebapp import views

urlpatterns = [
    path('', views.index, name='index'),
    path('menu/', views.menu_list, name='menulist'),
    path('menu/create/', views.MenuFormView.as_view(), name='createmenu'),
    path('menu/edit/<uuid:id>/', views.MenuFormView.as_view(), name='editmenu'),
    path('menu/<uuid:id>/', views.MenuView.as_view(), name='menu'),
    path('employee/create/', views.EmployeeView.as_view(), name='createemployee'),
]
