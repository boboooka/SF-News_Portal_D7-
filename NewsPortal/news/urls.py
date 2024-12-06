from django.urls import path
from .views import post, posts, news_search, post_create, post_edit, post_delete

urlpatterns = [
    path('news/', posts, name='news'),
    path('news/<int:pk>/', post, name='post'),
    path('news/search/', news_search, name='news_search'),
    path('news/create/', post_create, name='post_create'),
    path('news/<int:pk>/edit/', post_edit, name='post_edit'),
    path('news/<int:pk>/delete/', post_delete, name='post_delete'),
]