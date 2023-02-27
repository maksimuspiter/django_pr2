from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from blog.models import Post, Portfolio

# class BookReaderSerializer(ModelSerializer):
#     class Meta:
#         model = User
#         fields = ('first_name', 'last_name')

class PostSerializer(ModelSerializer):
    # likes_count = serializers.SerializerMethodField()
    # annotated_likes = serializers.IntegerField(read_only=True)
    # rating = serializers.DecimalField(max_digits=3, decimal_places=2, read_only=True)
    # owner_name = serializers.CharField(source='owner.username', default='', read_only=True)


    class Meta:
        model = Post
        fields = '__all__'

