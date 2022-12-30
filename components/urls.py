from django.urls import path
from . import views

urlpatterns = [
    # !!!!!! Customer paths !!!!!

    # list of Customers
    path('user/', views.users, name="users"),
    # add of Customer
    path('add_user/', views.new_user, name="add_user"),
    # update customer info
    path('update_user/<str:pk>/', views.update_user, name="update_user"),
    # delete Customers
    path('delete_user/<str:pk>/', views.delete_user, name="delete_user"),
    # !!!!!! login paths !!!!!

    # register new user
    path('register/', views.register, name="register"),
    # login page
    path('login/', views.loginpage, name="login"),

    # !!!!!! manger paths !!!!!

    # list of mangers
    path('manger/', views.manger, name="manger"),
    # create new mangers
    path('add_manger/', views.new_manger, name="add_manger"),
    # update mangers info
    path('update_manger/<str:pk>/', views.update_manger, name="update_manger"),
    # delete mangers
    path('delete_manger/<str:pk>/', views.delete_manger, name="delete_manger"),

    # !!!!!! manger paths !!!!!

    # list of employees
    path('employee/', views.employees, name="employee"),
    # create new employees
    path('add_employee/', views.new_employee, name="add_employee"),
    # update employees info
    path('update_employee/<str:pk>/', views.update_employee, name="update_employee"),
    # delete employees
    path('delete_employee/<str:pk>/', views.delete_employee, name="delete_employee"),
]
