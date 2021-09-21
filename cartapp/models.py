from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from musicalapp.models import Instrument


class Cart(models.Model):
    instrument = models.ForeignKey(Instrument, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Order(models.Model):
    totalBill = models.IntegerField()
    status = models.CharField(max_length=30, default="processing")
    order_date = models.DateTimeField(auto_now=True)
    user=models.ForeignKey(User, on_delete=models.CASCADE)
