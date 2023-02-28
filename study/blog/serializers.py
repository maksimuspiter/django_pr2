from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from blog.models import Post, Tag


class TagSerializer(serializers.ModelSerializer):
    # posts = serializers.PrimaryKeyRelatedField(many=True, queryset=Post.objects.all())

    class Meta:
        model = Tag
        fields = ('title',)


class PostSerializer(ModelSerializer):
    # author = serializers.HiddenField(default=serializers.CurrentUserDefault())
    # author = serializers.ReadOnlyField(source='author.username')
    # tags_name = TagSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ('id', 'title', 'text', 'created_date', 'published', 'author')
