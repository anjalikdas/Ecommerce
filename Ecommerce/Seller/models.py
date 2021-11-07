from django.db import models


# Create your models here.
class Company(models.Model):
    c_name = models.CharField(max_length=100, unique=True)
    address = models.JSONField()
    email = models.EmailField(max_length=70, unique=True)
    Phone_no = models.CharField(max_length=10)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)


class Employee(models.Model):
    first_name = models.CharField(max_length=35)
    last_name = models.CharField(max_length=35)
    address = models.JSONField()
    email = models.EmailField(max_length=70,unique=True)
    Phone_no = models.CharField(max_length=10)
    department = models.CharField(max_length=30)
    Company = models.ForeignKey(Company, on_delete=models.CASCADE)
