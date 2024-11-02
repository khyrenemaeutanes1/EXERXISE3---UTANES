from django.urls import path
from .views import UserRegistrationView, UserLoginView, TagListCreateAPIView, CategoryListCreateAPIView, root_view

urlpatterns = [
    path('', root_view, name='root'),
    path('tags/', TagListCreateAPIView.as_view(), name='tag-list-create'),
    path('tags/<int:id>/', TagListCreateAPIView.as_view(), name='tag-detail'),
    path('categories/', CategoryListCreateAPIView.as_view(), name='category-list-create'),
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
]
