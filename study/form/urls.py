from django.urls import path, include, re_path
from form import views

urlpatterns = [
    path('', views.index, name='index'),
    path('posts/', views.show_posts, name='get-all-posts'),
    path('tags/', views.show_tags, name='get-all-tags'),
    path('tags/create/', views.create_tag, name='create-tag'),
    path('posts/create/', views.create_post, name='create-post'),


]
