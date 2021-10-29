from django.urls import path

from blog.views import BlogDeleteView


from .views import (
    PostListView,
    BlogDetailView,
    MessageDetailView,
    BlogCreateView,
    BlogUpdateView,
    BlogDeleteView
)

urlpatterns = [
    path('', PostListView.as_view(), name='home'),
    path('message/<int:pk>/', BlogDetailView.as_view(), name='message'),
    path('messagedetail/<int:pk>/',
         MessageDetailView.as_view(), name='post_detail'),
    path('post/new/', BlogCreateView.as_view(), name='post_new'),
    path('post/<int:pk>/edit/', BlogUpdateView.as_view(), name='post_edit'),
    path('post/<int:pk>/delete/', BlogDeleteView.as_view(), name="post_delete"),

]
