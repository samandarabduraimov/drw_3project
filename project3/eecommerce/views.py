from django.shortcuts import render
from .models import User,Categories,Product
from .serializers import UserSerializer,OrderSerializer,CategoriesSerializer,ProductSerializer
from rest_framework.response import Response
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView,ListAPIView
# Create your views here.

class UserApiView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class CategoriesApiView(ListAPIView):
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer

class ProductApiView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class CreateListUserView(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class CreateListCategoryView(ListCreateAPIView):
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer

class CreateListProductView(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class UpdateListSignsView(RetrieveUpdateDestroyAPIView):
    queryset = User
    serializer_class = UserSerializer


class UpdateListCategoryView(RetrieveUpdateDestroyAPIView):
    queryset = Categories
    serializer_class = CategoriesSerializer


class UpdateListProductView(RetrieveUpdateDestroyAPIView):
    queryset = Product
    serializer_class = ProductSerializer