from django.db import models
from Product import models as Pmodel
from Buyer import models as Bmodel


# Create your models here.

class Order(models.Model):
    product = models.ForeignKey(Pmodel.Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Bmodel.Customer, on_delete=models.CASCADE)
    o_date = models.DateField(auto_now=True)
    total_paid = models.DecimalField(max_digits=5, decimal_places=2)
    quantity = models.PositiveBigIntegerField(default=1)
    status = models.CharField(max_length=10)



