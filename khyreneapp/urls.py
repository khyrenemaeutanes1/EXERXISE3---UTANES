from django.urls import path
from .views import TagListCreateAPIView, root_view

urlpatterns = [
    path('', root_view, name='root'),  # Root URL
    path('api/articles/tags/', TagListCreateAPIView.as_view(), name='tag-list-create'),
]
