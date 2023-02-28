from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views

from snippets.views import SnippetViewSet, UserViewSet, api_root
from rest_framework import renderers
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'snippets', views.SnippetViewSet, basename="snippet")
router.register(r'users', views.UserViewSet, basename="user")

urlpatterns = [
    path('', include(router.urls)),
]
