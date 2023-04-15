from rest_framework import serializers
from .models import ShoppingCart

class ShoppingCartSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShoppingCart
        fields = ['id', 'quantity', 'total_cost', 'qr_id_id', 'products_id']
        depth = 1