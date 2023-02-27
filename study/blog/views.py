from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework import generics
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from blog.permission import IsAdminOrReadOnly, IsAdminOrOwnerOrReadOnlyForPosts

from blog.models import Post
from serializer import PostSerializer


def index(request):
    if request.user.is_superuser:
        posts = Post.objects.all()
    else:
        posts = Post.objects.filter(published=True)
    return render(request, 'index.html', {"posts": posts})


class PostAPIView(generics.ListCreateAPIView):
    """
    GET, POST
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]


# UpdateAPIView

class PostUpdate(generics.RetrieveUpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    # permission_classes = [IsAuthenticatedOrReadOnly]

class WomenAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAdminOrOwnerOrReadOnlyForPosts,)
