from django.urls import path, include, re_path
from form import views

app_name = 'form'

urlpatterns = [
    path('', views.index, name='index'),
    path('posts/', views.show_posts, name='get-all-posts'),
    path('tags/', views.show_tags, name='get-all-tags'),
    path('categories/', views.show_category, name='get-all-categories'),
    path('portfolios/', views.show_portfolio, name='get-all-portfolios'),


    path('tags/create/', views.create_tag, name='create-tag'),
    path('posts/create/', views.create_post, name='create-post'),
    path('categories/create/', views.CreateCategoryFactory.as_view(), name='create-category'),
    path('portfolios/create/', views.create_portfolios, name='create-portfolios'),

]
