from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from blog.models import Post, Tag


# class BookReaderSerializer(ModelSerializer):
#     class Meta:
#         model = User
#         fields = ('first_name', 'last_name')
class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = 'title',

class PostSerializer(ModelSerializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())
    # tag_list = TagSerializer(many=True, read_only=True)
    tags = TagSerializer(many=True, read_only=True)



    class Meta:
        model = Post
        fields = ('title', 'text', 'created_date', 'published', 'author', 'tags')

