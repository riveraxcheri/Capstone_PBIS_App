from django.urls import path, include
from shopping_cart import views

urlpatterns = [
    path('', views.get_cart_data)
]