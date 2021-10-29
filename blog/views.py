from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import (
    CreateView,
    UpdateView,
    DeleteView
)
from django.urls import reverse_lazy
from .models import Post


class PostListView(ListView):
    template_name = "post_list.html"
    model = Post


class BlogDetailView(DetailView):
    template_name = "detail.html"
    model = Post


class MessageDetailView(DetailView):
    template_name = "detail.html"
    model = Post


class BlogCreateView(CreateView):
    model = Post
    template_name = "post_new.html"
    fields = ["title", "body", "author"]


class BlogUpdateView(UpdateView):
    model = Post
    template_name = "post_edit.html"
    fields = ["title", "body"]


class BlogDeleteView(DeleteView):
    model = Post
    template_name = "post_delete.html"
    success_url = reverse_lazy("home")
