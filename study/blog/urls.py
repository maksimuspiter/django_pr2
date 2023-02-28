from django.urls import path, include, re_path
from blog.views import index, PostAPIView, PostUpdate
from rest_framework.routers import SimpleRouter

router = SimpleRouter()


urlpatterns = [
    path('', index),
    path('api/v1/post/', PostAPIView.as_view()),
    path('api/v1/post/<int:pk>', PostUpdate.as_view()),

    # path('api/v1/auth/', include('djoser.urls')),  # djoser authentication
    # re_path(r'^auth/', include('djoser.urls.authtoken')),  #  djoser authentication

]
# urlpatterns += router.urls