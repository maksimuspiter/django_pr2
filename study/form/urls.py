from django.urls import path, include, re_path
from form import views

app_name = 'form'

urlpatterns = [
    path('', views.index, name='index'),
    path('posts/', views.show_posts, name='get-all-posts'),
    path('posts/less/', views.show_posts_less_qwery, name='get-all-posts_l'),

    path('tags/', views.show_tags, name='get-all-tags'),
    path('categories/', views.show_category, name='get-all-categories'),
    path('portfolios/', views.show_portfolio, name='get-all-portfolios'),


    path('tags/create/', views.create_tag, name='create-tag'),
    path('posts/create/', views.create_post, name='create-post'),
    path('categories/create/', views.CreateCategoryFactory.as_view(), name='create-category'),
    path('portfolios/create/', views.create_portfolios, name='create-portfolios'),
    path('portfolios/create2/', views.create_portfolios2, name='create-portfolios2'),

    path('posts/search/', views.search, name='search-posts'),

    # path('categories/add3/', views.CategoryFormSet, name='create-categories-3')

]
