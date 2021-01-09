from django.db import models


# Create your models here.
class Restaurant(models.Model):
    name = models.CharField(max_length=64)
    address = models.CharField(max_length=128)

    def __str__(self):
        return self.name

class Customer(models.Model):
    user_name = models.CharField(max_length=64)
    user_address = models.CharField(max_length=128)

    def __str__(self):
        return self.user_name

class OrderList(models.Model):
    item_name = models.CharField(max_length=64)
    price = models.IntegerField()
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    def __str__(self):
        return self.item_name

class OrderedItems(models.Model):
    customer_name = models.ForeignKey(Customer, on_delete=models.CASCADE)
    ordered_item = models.ForeignKey(OrderList, on_delete=models.CASCADE)
