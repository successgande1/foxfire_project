
from django.contrib import admin
from django.urls import path, include

#Import Settings
from django.conf import settings

#Import Static
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pages.urls')),
    path('accounts/', include('accounts.urls')),
    path('listings/', include('listings.urls')),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
