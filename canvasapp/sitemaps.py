from django.contrib.sitemaps import Sitemap
from .models import Recipe # Example for your Savora project

class RecipeSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8

    def items(self):
        return Recipe.objects.all()

    def lastmod(self, obj):
        return obj.updated_at # Assumes you have a timestamp field