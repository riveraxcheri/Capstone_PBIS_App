from django.db import models
from authentication.models import User
from products.models import Products
# Create your models here.
class ShoppingCart(models.Model):
    qr_id = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    total_cost = models.IntegerField()