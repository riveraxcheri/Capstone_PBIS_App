from rest_framework import serializers
from .models import ShoppingCart
# from .models import CartItem

class ShoppingCartSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShoppingCart
        fields = ['id', 'qr_id', 'products', 'total_cost']
        depth = 1

    # class Meta:
    #     model = CartItem
    #     fields = ['id','cart_id', 'product_id', 'quantity']
    #     depth = 1