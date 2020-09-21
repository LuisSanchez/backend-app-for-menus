from django.urls import path
from norawebapp import views

urlpatterns = [
    path('', views.index, name='index'),
    path('menu/create/', views.MenuFormView.as_view(), name='createmenu'),
    path('menu/<uuid:id>/', views.MenuView.as_view(), name='menu'),
    path('menu/', views.menu_list, name='menulist'),
    path('employee/create/', views.EmployeeView.as_view(), name='createemployee'),
]
