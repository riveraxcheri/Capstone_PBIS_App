
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from .models import ShoppingCart
from .serializers import ShoppingCartSerializer
from products.models import Products
from products.serializers import ProductsSerializer
from django.shortcuts import get_object_or_404


# from django.shortcuts import render, redirect

# Create your views here.
@api_view (['GET'])
@permission_classes ([AllowAny])
def cart_data(request, qr_id):
    request.method == 'GET'
    cart= ShoppingCart.objects.filter(qr_id=qr_id)
    serializer= ShoppingCartSerializer(cart, many=True)
    return Response(serializer.data)

# @api_view (['POST', 'DELETE'])
# @permission_classes([AllowAny])
# def add_to_cart(request, products_id):
#     product = get_object_or_404(Products, products_id=products_id)
#     serializer = ProductsSerializer(product, data=request.data)
#     request.method == 'POST'
#     if serializer.is_valid(raise_exception=True):
#         serializer.save()
#         return Response(cart_data, status=status.HTTP_202_ACCEPTED)
# def remove_from_cart(request, products_id):
#     request.method == 'DELETE'
#     cart = get_object_or_404(ShoppingCart, products_id=products_id)
#     product = get_object_or_404(Products, products_id=products_id)
#     serializer = ShoppingCartSerializer(cart, data=request.data)
#     ShoppingCart.delete(product)
#     return Response(cart_data)
#ATTEMPT
# @api_view (['GET'])
# @permission_classes([AllowAny])
# def get_cart_data(request):
#     cart = ShoppingCart.objects.get(qr_id=request.qr_id)
#     cart_items = CartItem.objects.filter(cart=cart)
#     context = {'cart_items': cart_items}
#     serializer = ShoppingCartSerializer(cart, many=True)
#     return Response(serializer.data, context)

# @api_view (['GET', 'PUT', 'POST', 'DELETE'])
# @permission_classes([AllowAny])
# def add_to_cart(request, product_id):
#     product = Products.objects.get(id=product_id)
#     cart, created = ShoppingCart.objects.get_or_create(qr_id=request.qr_id)
#     cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
#     cart_item.quantity += 1
#     cart_item.save()
#     return redirect('get_cart_data')
# def remove_from_cart(request, product_id):
#     product = Products.objects.get(id=product_id)
#     cart = ShoppingCart.objects.get(qr_id=request.qr_id)
#     cart_item = CartItem.objects.get(cart=cart, product=product)
#     if cart_item.quantity > 1:
#         cart_item.quantity -= 1
#         cart_item.save()
#     else:
#         cart_item.delete()
#     return redirect('get_cart_data')
#create function to calc total cost (product.cost x cart.quantity)