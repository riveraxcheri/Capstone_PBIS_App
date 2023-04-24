from django.urls import path, include
from shopping_cart import views

urlpatterns = [
    path('<int:qr_id>/', views.cart_data),
    # path('<int:qr_id>/add/<int:products_id>/', views.add_to_cart),
    # path('<int:qr_id>/remove/<int:products_id>/', views.remove_from_cart)
]

    # path('add/<int:product_id>/', views.add_to_cart),
    # path('remove/<int:product_id>/', views.remove_from_cart)