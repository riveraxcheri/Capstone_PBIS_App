from django.db import models
from authentication.models import User
from products.models import Products
# Create your models here.
class ShoppingCart(models.Model):
    qr_id = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ForeignKey(Products, on_delete=models.CASCADE)
    total_cost = models.IntegerField(default=0)

# class CartItem(models.Model):
#     cart = models.ForeignKey(ShoppingCart, on_delete=models.CASCADE)
#     product = models.ForeignKey(Products, on_delete=models.CASCADE)
#     quantity = models.IntegerField(default=1)