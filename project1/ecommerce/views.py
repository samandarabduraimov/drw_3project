from django.shortcuts import render
from rest_framework.views import APIView
from .models import User,Categories,Product
from .serializers import UserSerializer,CategoriesSerializer,ProductSerializer
from rest_framework.response import Response
# Create your views here.

class UserView(APIView):
    def get(self,request):
        users = User.objects.all()
        serializer = UserSerializer(users,many=True)
        return Response(serializer.data)
    
class ProductView(APIView):
    def get(self,request):
        products = Product.objects.all()
        serializer = ProductSerializer(products,many=True)
        return Response(serializer.data)
    

class CategoriesView(APIView):
    def get(self,request):
        categories = Categories.objects.all()
        serializer = CategoriesSerializer(categories,many=True)
        return Response(serializer.data)
    
class DeleteUserView(APIView):
    def delete(self,request,pk):
        user = User.objects.get(pk=pk)
        user.delete()
        return Response("User Deleted")

class UpdateUserView(APIView):
    def put(self,request,pk):
        user = User.objects.get(pk=pk)
        serializer = UserSerializer(instance=user,data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

class CreateUserView(APIView):
    def post(self,request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)