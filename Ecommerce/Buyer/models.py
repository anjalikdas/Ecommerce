from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=35)
    last_name = models.CharField(max_length=35)
    address = models.JSONField()
    email = models.EmailField()
    ph_no = models.CharField(max_length=10)


