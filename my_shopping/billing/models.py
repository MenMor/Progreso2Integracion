from django.db import models
from orders.models import Order

class Invoice(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
