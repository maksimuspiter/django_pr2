from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticated
from blog.permission import IsAdminOrOwnerOrReadOnlyForPosts

from blog.models import Post, Tag
from blog.serializers import PostSerializer, TagSerializer


def index(request):
    if request.user.is_superuser:
        posts = Post.objects.all()
    else:
        posts = Post.objects.filter(published=True)
    return render(request, 'index.html', {"posts": posts})





class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
