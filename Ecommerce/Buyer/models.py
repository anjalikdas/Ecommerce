from django.db import models
from Order import models as Omodel
from Product import models as Pmodel
from django.contrib.auth.models import User


# Create your models here.

class customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=35)
    address = models.JSONField()
    email = models.EmailField()
    ph_no = models.CharField(max_length=10)
    product = models.ForeignKey(Pmodel.Product, on_delete=models.CASCADE)
    order = models.ForeignKey(Omodel.Order, on_delete=models.CASCADE)
