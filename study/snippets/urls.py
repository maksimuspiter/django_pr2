from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views

urlpatterns = [
    path('snippets/', views.SnippetList.as_view()),
    path('snippets/<int:pk>/', views.SnippetDetail.as_view()),
]
urlpatterns = format_suffix_patterns(urlpatterns)
"""
add suffix
http://127.0.0.1:8000/snippets.json  # JSON suffix
http://127.0.0.1:8000/snippets.api   # Browsable API suffix
"""