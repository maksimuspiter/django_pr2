from django.forms import formset_factory
from django.http import HttpResponseRedirect
from django.shortcuts import render, HttpResponse, redirect
from django.views.generic import CreateView

from form.models import Post, Tag, Portfolio, Category
from django import forms
from .forms import CreateTagForm, CreatePostForm, CreateCategoryFormFactory, CreatePortfolioForm, CreateCategoryForm, \
    SearchForm
from django.contrib.auth.decorators import login_required
from django.db.transaction import atomic

CreateCategoryForm


def index(request):
    if request.user.is_authenticated:
        return HttpResponse(f'Hello: {request.user}')
    return redirect('registration:login')


@login_required(login_url='registration:login')
def show_posts(request):
    posts = Post.objects.all()
    data = {'title': 'all_posts', 'posts': posts}
    return render(request, 'form/posts.html', data)


@login_required(login_url='registration:login')
def show_posts_less_qwery(request):
    posts = Post.objects.select_related('category'). \
        prefetch_related('tags').only(
        'title', 'text', 'created_date', 'category', 'tags').all()
    data = {'title': 'all_posts', 'posts': posts}
    return render(request, 'form/posts.html', data)


def show_tags(request):
    tags = [str(tag) + ' ' for tag in Tag.objects.all()]
    return HttpResponse(tags)


def show_portfolio(request):
    ports = [str(port) + ' ' for port in Portfolio.objects.filter(author=request.user)]
    return HttpResponse(ports)


def show_category(request):
    cats = [str(cat) + ' ' for cat in Category.objects.all()]
    return HttpResponse(cats)


def create_tag(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = CreateTagForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            title = form.cleaned_data['title']
            Tag.objects.create(title=title)
            return redirect('form:get-all-tags')

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
            return redirect('form:get-all-posts')

    else:
        if request.user.is_authenticated:
            data = {'user_id': request.user.id}
            form = CreatePostForm(user=request.user)
            return render(request, 'form/name.html', {'form': form})

    return redirect('registration:login')


class CreateCategoryFactory(CreateView):
    form_class = CreateCategoryFormFactory
    template_name = 'form/name.html'
    success_url = '/form/'


def create_portfolios(request):
    if request.method == 'POST':
        form = CreatePortfolioForm(request.POST)

        if form.is_valid():
            nickname = form.cleaned_data['nickname']
            author = request.user

            Portfolio.objects.create(nickname=nickname, author=author, )
            return redirect('form:get-all-portfolios')

    else:
        form = CreatePortfolioForm()

    return render(request, 'form/name.html', {'form': form})


def create_portfolios2(request):
    if request.method == 'POST':
        user = request.user
        form = CreatePortfolioForm(request.POST, initial={"author": user})

        if form.is_valid():
            nickname = form.cleaned_data['nickname']
            author = request.user

            Portfolio.objects.create(nickname=nickname, author=author, )
            return redirect('form:get-all-portfolios')

    else:
        form = CreatePortfolioForm()

    return render(request, 'form/name.html', {'form': form})


CategoryFormSet = forms.modelform_factory(Category, CreateCategoryForm, fields=('title',))


def search(request):
    if request.method == 'POST':
        sf = SearchForm(request.POST)
        if sf.is_valid():
            keyword = sf.cleaned_data['keyword']
            category = sf.cleaned_data['category']
            category_id = category.pk
            posts = Post.objects.filter(title__icontains=keyword,
                                        category=category_id)
            context = {'posts': posts, 'category': category}
            print(category, keyword)
            return render(request, 'form/search_results.html', context)
    else:
        sf = SearchForm()
    context = {'form': sf}
    return render(request, 'form/search.html', context)

# def formset_processing(request):
#     FS = formset_factory(SearchForm, extra=3, can_order=True, can_delete=True)
#
#     if request.method == 'POST':
#         formset = FS(request.POST)
#         if formset.is_valid():
#             for form in formset:
#                 if form.cleaned_data and not form.cleaned_data['DELETE']:
#                     keyword = form.cleaned_data['keyword']
#                     keyword = form.cleaned_data['keyword']
#                     category = form.cleaned_data['category']
#                     category_id = category.pk
#                     order = form.cleaned_data['ORDER']
#
