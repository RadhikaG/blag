from django.contrib.syndication.views import Feed
from .models import Post

class LatestPosts(Feed):
    title = "blag"
    link = "/feed/"
    description = "Latest Posts on Blag"

    def items(self):
        return Post.objects.published()[:5]
