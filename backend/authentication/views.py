from django.contrib.auth import get_user_model
from .serializers import MyTokenObtainPairSerializer, RegistrationSerializer
from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView
User = get_user_model()


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegistrationSerializer

#////////////// Teacher User CRUD for Students /////////////
# from django.shortcuts import render
# from rest_framework import status
# from rest_framework.response import Response
# from rest_framework.permissions import IsAuthenticated, AllowAny
# from rest_framework.decorators import api_view, permission_classes
# from .models import User
# from .serializers import RegistrationSerializer
# from django.shortcuts import get_object_or_404

# # Create your views here.
# @api_view (['GET'])
# @permission_classes([AllowAny])
# def get_all_students(request, is_student):
#     students = User.objects.filter(is_student=True)
#     serializer = User(students, many=True)
#     return Response(serializer.data)

# @api_view(['POST'])
# @permission_classes([IsAuthenticated])
# def add_products(request):
#     serializer = ProductsSerializer(data=request.data)
#     if serializer.is_valid(raise_exception=True):
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)

# @api_view (['PUT', 'DELETE'])
# @permission_classes([IsAuthenticated])
# def update_products(request, pk):
#     products = get_object_or_404(Products, pk=pk)
#     serializer = ProductsSerializer(products, data=request.data)
#     if request.method == 'PUT':
#         if serializer.is_valid(raise_exception=True):
#             serializer.save(data=request.data)
#             return Response(serializer.data)
#     elif request.method == 'DELETE':
#         Products.delete()
#         return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)