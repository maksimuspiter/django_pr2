from django.urls import path, include
from blog import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'tag', views.TagViewSet, basename="tag")
router.register(r'post', views.PostViewSet, basename="post")

urlpatterns = [
    path('', include(router.urls)),

]
