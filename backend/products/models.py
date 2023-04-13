from django.db import models

# Create your models here.
class Products(models.Model):
    name = models.CharField(max_length=100)
    cost = models.IntegerField()
    category = models.CharField(max_length=100)
    is_available = models.BooleanField(default=True)