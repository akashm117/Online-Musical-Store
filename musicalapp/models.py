from django.db import models

# Create your models here.
class Instrument(models.Model):
    # id: int
    # name: str
    # image: str
    # price: float
    # desc: str

    name=models.CharField(max_length=100)
    desc=models.TextField()
    price=models.FloatField()
    image=models.ImageField(upload_to='pics')
