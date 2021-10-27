from django.urls import path


from .views import PostListView, BlogDetailView, MessageDetailView

urlpatterns = [
    path('', PostListView.as_view(), name='home'),
    path('message/<int:pk>/', BlogDetailView.as_view(), name='message'),
    path('messagedetail/<int:pk>/', MessageDetailView.as_view(), name='post_detail')

]
