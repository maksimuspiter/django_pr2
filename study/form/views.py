from django.http import HttpResponseRedirect
from django.shortcuts import render, HttpResponse, redirect
from form.models import Post, Tag, Portfolio
from .forms import CreateTagForm, CreatePostForm, CreateCategoryForm


def index(request):
    # return HttpResponse(f'Hello world')
    return render(request, 'form/index2.html')


def show_posts(request):
    post = [str(post) + ' ' for post in Post.objects.all()]
    return HttpResponse(post)


def show_tags(request):
    tags = [str(tag) + ' ' for tag in Tag.objects.all()]
    return HttpResponse(tags)


def create_tag(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = CreateTagForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            title = form.cleaned_data['title']
            Tag.objects.create(title=title)
            return redirect('get-all-tags')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = CreateTagForm()

    return render(request, 'form/name.html', {'form': form})





def create_post(request):
    if request.method == 'POST':
        form = CreatePostForm(request.POST)

        if form.is_valid():
            title = form.cleaned_data['title']
            text = form.cleaned_data['text']
            # author = Portfolio.objects.get(author=request.user)
            category = form.cleaned_data['category']
            tags = form.cleaned_data['tags']
            # print(request.user)

            Post.objects.create(title=title)
            return redirect('get-all-posts')

    else:
        data = {'user_id': request.user.id}
        form = CreatePostForm(user=request.user)

    return render(request, 'form/name.html', {'form': form})
