from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import ModelFormMixin
from django.views.generic.detail import SingleObjectMixin

from .models import Category, Post, Comment
# Create your views here.


class BlogIndex(ListView):
    queryset = Post.objects.published()
    template_name = "home.html"
    paginate_by = 5


class BlogDetail(DetailView):
    model = Post
    template_name = "post.html"

    def get_context_data(self, **kwargs):
        """
        Insert into the context dict.
        """
        context = super(BlogDetail, self).get_context_data(**kwargs)
        post = self.object
        context['comment_list'] = Comment.objects.filter(post=post)
        return context

class CategoryIndex(ListView):
    template_name = "home.html"
    paginate_by = 5

    def get_queryset(self):
        slug = self.kwargs['slug']
        category = Category.objects.get(slug=slug)
        results = Post.objects.filter(categories=category)
        return results

class Registration(CreateView):
    template_name = "register.html"
    form_class = UserCreationForm
    success_url = '/admin/'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.is_staff = True
        self.object.save()
        return super(ModelFormMixin, self).form_valid(form)
