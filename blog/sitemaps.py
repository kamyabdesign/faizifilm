from django.contrib.sitemaps import Sitemap
from .models import Article


class Postsitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.8

    def items(self):
        return Article.objects.filter(status="p")

    def lastmod(self, obj):
        return obj.updated
