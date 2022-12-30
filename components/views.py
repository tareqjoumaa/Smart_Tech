from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import customerForm, CreateUserForm, mangerForm, employeeForm
from .models import customer, manager, employee


# list of all Customers
def users(request):
    customers = customer.objects.all()
    return render(request, "pages/Users/user.html", {
        "customers": customers
    })


# for add new Customers
def new_user(request):
    form = customerForm()
    if request.method == 'POST':
        form = customerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/api/components/user/')
    return render(request, "pages/Users/newuser.html", {
        'form': form
    })


# def to update Customers info
def update_user(request, pk):
    update = customer.objects.get(id=pk)
    form = customerForm(instance=update)
    if request.method == 'POST':
        form = customerForm(request.POST, instance=update)
        if form.is_valid():
            form.save()
            return redirect('/api/components/user/')
    return render(request, "pages/Users/newuser.html", {
        'form': form
    })


# def to delete Customer
def delete_user(request, pk):
    user = customer.objects.get(id=pk)
    if request.method == 'POST':
        user.delete()
        return redirect('/api/components/user/')
    return render(request, "pages/Users/delete.html", {
        "item": user
    })


# register page to create new user to login
def register(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    return render(request, "pages/register.html", {
        "form": form
    })


# login page for users and check the password and first_name
def loginpage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('users')
        else:
            messages.info(request, "zzzzzzzzzzzzzzzz")
    return render(request, "pages/login.html")


# for add new manger
def manger(request):
    manger = manager.objects.all()
    return render(request, "pages/manger/manger.html", {
        "manger": manger
    })


# def for create new manger
def new_manger(request):
    form = customerForm()
    if request.method == 'POST':
        form = mangerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/api/components/manger/')
    return render(request, "pages/manger/newmanger.html", {
        'form': form
    })


# def fo update mangers info
def update_manger(request, pk):
    update = manager.objects.get(id=pk)
    form = mangerForm(instance=update)
    if request.method == 'POST':
        form = mangerForm(request.POST, instance=update)
        if form.is_valid():
            form.save()
            return redirect('/api/components/manger/')
    return render(request, "pages/manger/newmanger.html", {
        'form': form
    })


# def for delete mangers
def delete_manger(request, pk):
    manger = manager.objects.get(id=pk)
    if request.method == 'POST':
        manger.delete()
        return redirect('/api/components/manger/')
    return render(request, "pages/manger/delete_manger.html", {
        "item": manger
    })


# list of employees
def employees(request):
    employees = employee.objects.all()
    return render(request, "pages/employee/employee.html", {
        "employee": employees
    })


# for add new employees
def new_employee(request):
    form = employeeForm()
    if request.method == 'POST':
        form = employeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/api/components/employee/')
    return render(request, "pages/employee/newemployee.html", {
        'form': form
    })


# def for update employees
def update_employee(request, pk):
    update = employee.objects.get(id=pk)
    form = employeeForm(instance=update)
    if request.method == 'POST':
        form = employeeForm(request.POST, instance=update)
        if form.is_valid():
            form.save()
            return redirect('/api/components/employee/')
    return render(request, "pages/employee/newemployee.html", {
        'form': form
    })


# for delete employees
def delete_employee(request, pk):
    employees = employee.objects.get(id=pk)
    if request.method == 'POST':
        employees.delete()
        return redirect('/api/components/employee/')
    return render(request, "pages/employee/delete_employee.html", {
        "item": employees
    })
