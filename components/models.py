from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


# Create your models here.


class manager(models.Model):
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    birthday = models.DateField()

    def __str__(self):
        return self.firstname


class employee(models.Model):
    manager = models.ForeignKey(manager, null=True, on_delete=models.SET_NULL)
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    birthday = models.DateField()

    def __str__(self):
        return self.firstname


class customer(models.Model):
    manager = models.ForeignKey(manager, null=True, on_delete=models.SET_NULL)
    employee = models.ForeignKey(employee, null=True, on_delete=models.SET_NULL)
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    birthday = models.DateField()
    grade = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])

    def __str__(self):
        return self.firstname
