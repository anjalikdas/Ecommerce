from django.db import models
from Seller import models as Smodel


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    p_name = models.CharField(max_length=25)
    p_code=
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    p_dimension = models.JSONField()
    price = models.FloatField()
    stock = models.PositiveIntegerField()
    employee = models.ForeignKey(Smodel.Employee, on_delete=models.SET_NULL)
    seller = models.ForeignKey(Smodel.Company, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.p_name

    def seller_name(self):
        return self.seller.c_name
    class meta:
        un
