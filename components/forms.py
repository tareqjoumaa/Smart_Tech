from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import customer, manager, employee


# customer form :
class customerForm(ModelForm):
    class Meta:
        model = customer
        fields = '__all__'


# login form :
class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


# manger form :
class mangerForm(ModelForm):
    class Meta:
        model = manager
        fields = '__all__'


# employee form :
class employeeForm(ModelForm):
    class Meta:
        model = employee
        fields = '__all__'
