from django.db import models
from django.core.urlresolvers import reverse
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.forms import ModelForm

import markdown
# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, db_index=True)

    def __str__(self):
        return '%s' % self.title

    def get_absolute_url(self):
        return reverse("category_index", kwargs={"slug": self.slug})
    
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"


class PostQuerySet(models.QuerySet):
    def published(self):
        return self.filter(published=True)
# This custom QuerySet subclasses the regular QuerySet to provide
# an extra method called published()


class Post(models.Model):
    author = models.ForeignKey(User)
    title = models.CharField(max_length=100, unique=True)

    text = models.TextField()
    # A 'slug' is a short label used as a unique identifier in urls.

    text_html = models.TextField(editable=False, blank=True, null=True)
    # This is set as non-editable so that markdown can set the HTML
    # for the post.

    created_on = models.DateTimeField(db_index=True, auto_now_add=True)
    slug = models.SlugField(max_length=100, unique=True)
    categories = models.ManyToManyField(Category)

    published = models.BooleanField(default=True)
    objects = PostQuerySet.as_manager()
    # We set PostQuerySet as the default QuerySet manager for the Post model.
    # We set it as objects, because we always tend to call Post.objects.whatever(some params)
    # to create a QuerySet.

    def save(self):
        # self.text_html = markdown2.markdown(self.text, extras=['fenced-code-blocks'])
        self.text_html = markdown.markdown(self.text, extensions=['markdown.extensions.extra', 'magic'])
        super(Post, self).save()

    def __str__(self):
        return '%s' % self.title
   
    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"slug": self.slug})
    # This returns a URL calculated from the urls.py file, using
    # the unique slug.
    # Example:
    # Response from __str__: My first post
    # Response from get_absolute_url: /blag/view/my-first-post.html

    class Meta:
        verbose_name = "Blog Post"
        verbose_name_plural = "Blog Posts"
        ordering = ["-created_on"]


class Comment(models.Model):
    name = models.CharField(max_length=42)
    email = models.EmailField(max_length=75)
    website = models.URLField(max_length=200, null=True, blank=True)
    text = models.CharField(max_length=100)
    post = models.ForeignKey(Post)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s' % self.text

    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = "Comments"
        ordering = ["-created_on"]


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['name','email','website','text']
