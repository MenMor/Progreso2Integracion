from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    stock = models.IntegerField()

class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    customer_name = models.CharField(max_length=255)
    customer_email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)
