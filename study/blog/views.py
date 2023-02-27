from django.shortcuts import render, HttpResponse

from blog.models import Post


def index(request):
    if request.user.is_superuser:
        posts = Post.objects.all()
    else:
        posts = Post.objects.filter(published=True)
    return render(request, 'index.html', {"posts": posts})
