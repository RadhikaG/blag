from django.db import models
from django.core.urlresolvers import reverse
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, db_index=True)

    def __unicode__(self):
        return '%s' % self.title

    # def get_absolute_url(self):
        # return reverse("category_index", kwargs={"slug": self.slug})
    
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

# This custom QuerySet subclasses the regular QuerySet to provide
# an extra method called published()
class PostQuerySet(models.QuerySet):
    def published(self):
        return self.filter(published=True)


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

    def save(self):
        self.body_html = markdown2.markdown(self.body, extras=['fenced-code-blocks'])
        super(Post, self).save()

    def __unicode__(self):
        return '%s' % self.title
   
    def get_absolute_url(self):
        return reverse("view_post", kwargs={"slug": self.slug})
    # This returns a URL calculated from the urls.py file, using
    # the unique slug.
    # Example:
    # Response from __unicode__: My first post
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

    def __unicode__(self):
        return '%s' % self.text

    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = "Comments"
        ordering = ["-created_on"]

