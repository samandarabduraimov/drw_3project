from django.shortcuts import render
from .models import User
from rest_framework.response import Response
from .serializers import UserSerializer
from rest_framework.decorators import api_view
from rest_framework import status,viewsets
# Create your views here.

@api_view(['POST'])
def create_user(request):
    serializer=UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=status.HTTP_200_OK)
    
@api_view(['GET'])
def get_user(request):
    users=User.objects.all()
    serializer=UserSerializer(users,many=True)
    return Response(serializer.data,status=status.HTTP_200_OK)

@api_view(['GET'])
def get_user_id(request,pk):
    user=User.objects.get(pk=pk)
    serializer=UserSerializer(user)
    return Response(serializer.data,status=status.HTTP_200_OK)

@api_view(['DELETE'])
def delete_user(request,pk):
    user=User.objects.get(pk=pk)
    user.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['PUT'])
def update_user(request,pk):
    user=User.objects.get(pk=pk)
    serializer=UserSerializer(instance=user,data=request.data,partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=status.HTTP_200_OK)
    
@api_view(['PATCH'])
def partial_update_user(request,pk):
    user=User.objects.get(pk=pk)
    serializer=UserSerializer(instance=user,data=request.data,partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=status.HTTP_200_OK)



class UsersView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer