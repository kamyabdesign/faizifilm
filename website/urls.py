from django.contrib import admin, sitemaps
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from blog.sitemaps import Postsitemap
sitemaps = {
    "post": Postsitemap
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('film.urls')),
    path('blog/', include('blog.urls')),
    path('work/', include('work.urls')),
    path('tamas/', include('tamas.urls')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps})
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
