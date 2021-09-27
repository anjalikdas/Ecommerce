from django.db import models
from Order import models as Omodel
from Seller import models as Smodel
from Buyer import models as Bmodel


# Create your models here.

class Transaction(models.Model):
    order = models.ForeignKey(Omodel.Order, on_delete=models.CASCADE)
    seller = models.ForeignKey(Smodel.Company, on_delete=models.CASCADE)
    status = models.CharField(max_length=10)


class Payment(models.Model):
    order = models.ForeignKey(Omodel.Order, on_delete=models.CASCADE)
    customer = models.ForeignKey(Bmodel.Customer, on_delete=models.CASCADE)
    amount = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)
