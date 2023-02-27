from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from blog.models import Post

# class BookReaderSerializer(ModelSerializer):
#     class Meta:
#         model = User
#         fields = ('first_name', 'last_name')

class PostSerializer(ModelSerializer):

    author = serializers.HiddenField(default=serializers.CurrentUserDefault())


    class Meta:
        model = Post
        fields = '__all__'

