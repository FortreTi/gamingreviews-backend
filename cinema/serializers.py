from django.contrib.auth.models import User, Post
from rest_framework import serializers

class User(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['email', 'name', 'password']

class Post(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['name_game', 'date_post', 'review']


