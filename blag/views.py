from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.views.generic import ListView, DetailView, CreateView, FormView
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import ModelFormMixin
from django.views.generic.detail import SingleObjectMixin
from django.views.generic import View

from .models import Category, Post, Comment
from .models import CommentForm
# Create your views here.


class BlogIndex(ListView):
    queryset = Post.objects.published()
    template_name = "home.html"
    paginate_by = 5


class PostDisplay(DetailView):
    model = Post
    template_name = "post.html"

    def get_context_data(self, **kwargs):
        """
        Insert into the context dict.
        """
        context = super(PostDisplay, self).get_context_data(**kwargs)
        post = self.object
        context['comment_list'] = Comment.objects.filter(post=post)
        context['form'] = CommentForm()
        return context


class PostComment(SingleObjectMixin, FormView):
    model = Post
    template_name = "post.html"
    form_class = CommentForm

    def form_valid(self, form):
        self.object = form.save(commit=False)
        slug = self.kwargs['slug']
        self.object.post = Post.objects.get(slug=slug)
        self.object.save()
        return super(PostComment, self).form_valid(form)

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super(PostComment, self).post(request, *args, **kwargs)

    def get_success_url(self):
        slug = self.kwargs['slug']
        return reverse('post_detail', kwargs={'slug': slug})


class PostDetail(View):

    def get(self, request, *args, **kwargs):
        view = PostDisplay.as_view()
        return view(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        view = PostComment.as_view()
        return view(request, *args, **kwargs)


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
