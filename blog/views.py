from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post
# Create your views here.


class PostListView(ListView):
    template_name = "post_list.html"
    model = Post


class BlogDetailView(DetailView):
    template_name = "detail.html"
    model = Post


class MessageDetailView(DetailView):
    template_name = "detail.html"
    model = Post
