from cinema.models import User, Post
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['email', 'name', 'password']

class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ['name_game', 'date_post', 'review']


