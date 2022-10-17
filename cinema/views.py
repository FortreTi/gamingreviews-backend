from django.shortcuts import render
from rest_framework import serializers, viewsets
from cinema.models import User, Post
from cinema.serializers import PostSerializer, UserSerializer

# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


    
