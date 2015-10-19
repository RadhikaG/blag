from django.contrib import admin
from django_markdown.admin import MarkdownModelAdmin
from django_markdown.widgets import AdminMarkdownWidget
from django.db.models import TextField

from .models import Category, Post, Comment
# Register your models here.

class PostAdmin(MarkdownModelAdmin):
    list_display = ('title', 'created_on')
    prepopulated_fields = {'slug': ('title',)}
    formfield_overrides = {TextField: {'widget': AdminMarkdownWidget}}

admin.site.register(Category)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
