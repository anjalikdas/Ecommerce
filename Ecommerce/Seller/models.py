from django.db import models
from Order import models as Omodel
from Transaction import models as Tmodel


# Create your models here.


class Company(models.Model):
    c_name = models.CharField(max_length=25)
    address = models.JSONField()
    email = models.EmailField()
    Phone_no = models.CharField(max_length=10)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)


class Employee(models.Model):
    first_name = models.CharField(max_length=35)
    last_name = models.CharField(max_length=35)
    address = models.JSONField()
    email = models.EmailField()
    Phone_no = models.CharField(max_length=10)
    department = models.CharField(max_length=30)
    order = models.ForeignKey(Omodel.Order, on_delete=models.CASCADE)
    transaction = models.ForeignKey(Tmodel.Transaction, on_delete=models.CASCADE)
