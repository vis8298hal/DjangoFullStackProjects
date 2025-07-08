from django.db import models

# Create your models here.
class Item(models.Model):

    def __str__(self):
        return self.Item_name
    
    Item_name = models.CharField(max_length=200)
    Item_descr = models.CharField(max_length=200)
    unit_price = models.IntegerField()
    Item_image = models.CharField(max_length=500, default="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSq9LhDfNFGvhQm1vx6I3gkDNi5M5r9tRSKqtr8qATPESYBsSIJNjdzr1iwqINoN_XcJ9U&usqp=CAU")
