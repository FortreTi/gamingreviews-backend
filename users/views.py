from django.shortcuts import render
from rest_framework import serializers, viewsets
from users.models import User
from base.serializers import UserSerializer

# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer




    
