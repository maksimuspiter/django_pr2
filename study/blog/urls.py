from django.urls import path, include
from blog.views import index, PostAPIView, PostCreate, PostUpdate
from rest_framework.routers import SimpleRouter

router = SimpleRouter()


urlpatterns = [
    path('', index),
    # path('api/v1/drf-auth/', include('rest_framework.urls')),
    path('api/v1/postlist/', PostAPIView.as_view()),
    path('api/v1/postcreate/', PostCreate.as_view()),
    path('api/v1/postupdate/<int:pk>', PostUpdate.as_view()),

]
# urlpatterns += router.urls