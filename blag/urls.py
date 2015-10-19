from django.conf.urls import patterns, url
from . import views, feed

urlpatterns = patterns(
        '',
        url(r'^feed/$', feed.LatestPosts(), name="feed"),
        url(r'^$', views.BlogIndex.as_view(), name="index"),
        url(r'^/post/(?P<slug>\S+)$', views.BlogDetail.as_view(), name="post_detail"),
)
