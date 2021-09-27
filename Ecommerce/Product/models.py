from django.db import models
from Seller import models as Smodel


# Create your models here.

class Product(models.Model):
    p_name = models.CharField(max_length=25)
    p_type = models.CharField(max_length=25)
    p_dimension = models.JSONField()
    seller = models.ForeignKey(Smodel.Company, on_delete=models.CASCADE)
    employee = models.ForeignKey(Smodel.Employee, on_delete=models.CASCADE)
