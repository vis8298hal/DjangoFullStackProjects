from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Item(models.Model):

    def __str__(self):
        return self.Item_name
    User_name = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    Item_name = models.CharField(max_length=200)
    Item_descr = models.CharField(max_length=200)
    unit_price = models.IntegerField()
    Item_image = models.CharField(max_length=500, default="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSq9LhDfNFGvhQm1vx6I3gkDNi5M5r9tRSKqtr8qATPESYBsSIJNjdzr1iwqINoN_XcJ9U&usqp=CAU")

    def get_absolute_url(self):
        return reverse("food:detail", kwargs={"pk": self.pk})
    
