from django.urls import path
from .views import TagListCreateAPIView, CategoryListCreateAPIView, root_view

urlpatterns = [
    path('', root_view, name='root'),
    path('api/articles/tags/', TagListCreateAPIView.as_view(), name='tag-list-create'),
    path('api/articles/categories/', CategoryListCreateAPIView.as_view(), name='category-list-create'),
]
