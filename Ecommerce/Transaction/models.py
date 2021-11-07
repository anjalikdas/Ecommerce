from django.db import models
from Order import models as Omodel
from Seller import models as Smodel
from Buyer import models as Bmodel


# Create your models here.


class Payment(models.Model):
    customer = models.ForeignKey(Bmodel.customer, on_delete=models.CASCADE)
    order_id
    amount = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10)

class sucessfull_Trasaction:
    customer
    order_id
    seller
    payement_id

class unsucessfull_Transaction:


