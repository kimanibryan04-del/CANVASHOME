from django.contrib import admin
from django.urls import path, include
from django.contrib.sitemaps.views import sitemap  # Ensure this is imported
from canvasapp.sitemaps import YourSitemapClass  # Replace with your actual class name

sitemaps = {
    'static': YourSitemapClass,
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('canvasapp.urls')),

    # Add the sitemap line here, inside the same list
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
]