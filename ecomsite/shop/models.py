from django.db import models
from datetime import datetime, timedelta

# Create your models here.
def get_future_datetime():
    return datetime.now() + timedelta(days=30)

class Product(models.Model):
    title = models.CharField(max_length=200)
    price = models.FloatField()
    category = models.CharField(max_length=200)
    discount_price = models.FloatField()
    image = models.CharField(max_length=300)
    description = models.TextField()
    MFG_DT = models.DateField(default=datetime.now())
    EXP_DT = models.DateField(default=get_future_datetime)

    def __str__(self):
        return self.title