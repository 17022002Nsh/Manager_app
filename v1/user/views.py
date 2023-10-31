<<<<<<< HEAD
from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import  CreateAPIView

from v1.user.models import User
from v1.user.serializer import CoderCreateSerializer, CoderMessageSerializer, UserRegisterSerializer




# class UserRegisterAPi(ListCreateAPIView):
#     permission_classes = (IsAuthenticated, )
#     queryset = User.objects.all()
#     serializer_class = UserRegisterSerializer









    
    
=======
from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import  CreateAPIView

from v1.user.models import User
from v1.user.serializer import CoderCreateSerializer, CoderMessageSerializer, UserRegisterSerializer




# class UserRegisterAPi(ListCreateAPIView):
#     permission_classes = (IsAuthenticated, )
#     queryset = User.objects.all()
#     serializer_class = UserRegisterSerializer









    
    
>>>>>>> d51e158 (..)
