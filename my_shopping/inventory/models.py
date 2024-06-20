from django.db import models
from orders.models import Product

class Inventory(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    stock = models.IntegerField()
