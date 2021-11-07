from django.db import models
from Product import models as Pmodel
from Buyer import models as Bmodel
from Transaction import models as Tmodel


# Create your models here.
class OrderProduct(models.Model):
    customer = models.ForeignKey(Bmodel.customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Pmodel.Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    ordered = models.BooleanField(default=False)

    def get_total_product_price(self):
        return self.quantity * self.product.price


class Order(models.Model):
    customer = models.ForeignKey(Bmodel.customer, on_delete=models.CASCADE)
    product = models.ManyToManyField(OrderProduct)
    address = models.CharField(max_length=250)
    address_second = models.CharField(max_length=250, null=True, blank=True)
    postal_code = models.CharField(max_length=20)
    country = models.CharField(max_length=100, null=True, blank=True)
    state = models.CharField(max_length=100)
    o_date = models.DateField(auto_now=True)
    status = models.CharField(max_length=10)
    payment = models.ForeignKey(Tmodel.Payment, on_delete=models.SET_NULL, blank=True, null=True)

    @property
    def get_total_price(self):
        total = 0
        for product in self.product.all():
            total = total + product.get_total_product_price()
        return total
