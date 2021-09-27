from django.db import models
from Product import models as Pmodel


# Create your models here.

class price(models.Model):
    product = models.ForeignKey(Pmodel.Product, on_delete=models.CASCADE)
