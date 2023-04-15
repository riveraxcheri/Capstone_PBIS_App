
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from .models import ShoppingCart
from .serializers import ShoppingCartSerializer

# Create your views here.
@api_view (['GET'])
@permission_classes([AllowAny])
def get_cart_data(request):
    cart = ShoppingCart.objects.all()
    serializer = ShoppingCartSerializer(cart, many=True)
    return Response(serializer.data)