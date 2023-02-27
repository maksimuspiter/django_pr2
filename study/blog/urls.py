from django.urls import path
from blog.views import hello_world

urlpatterns = [
    path('', hello_world),


]
