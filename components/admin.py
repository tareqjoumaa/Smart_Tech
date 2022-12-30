from django.contrib import admin

# Register your models here.
from .models import customer, employee, manager

admin.site.register(customer)
admin.site.register(manager)
admin.site.register(employee)
