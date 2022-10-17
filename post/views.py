from django.shortcuts import render
from rest_framework import serializers, viewsets
from post.models import Post
from base.serializers import PostSerializer

# Create your views here.

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer