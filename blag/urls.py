from django.conf.urls import patterns, url
from . import views, feed

urlpatterns = patterns(
        '',
        url(r'^feed/$', feed.LatestPosts(), name="feed"),
        url(r'^$', views.BlogIndex.as_view(), name="index"),
        url(r'^register/$', views.Registration.as_view(), name="registration"),
        url(r'^post/(?P<slug>\S+)$', views.PostDetail.as_view(), name="post_detail"),
        url(r'^category/(?P<slug>\S+)$', views.CategoryIndex.as_view(), name="category_index"),
        # We pass <slug> as a kwarg (keyword argument) into the given views
        url(r'^colophon/$', views.colophon, name="colophon"),
)
