from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Category, Post, Comment

# Create your views here.
class BlogIndex(ListView):
    queryset = Post.objects.published()
    template_name = "home.html"
    paginate_by = 2


class BlogDetail(DetailView):
    model = Post
    template_name = "post.html"
