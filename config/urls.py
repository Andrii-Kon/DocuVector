# config/urls.py

from django.contrib import admin
from django.urls import path, include  # Add include
from django.conf import settings  # Import settings
from django.conf.urls.static import static  # Import static

urlpatterns = [
    path('admin/', admin.site.urls),
    # We will point the root URL to our converter app's URLs.
    path('', include('converter.urls')),
]

# This is a standard pattern to serve media files during development.
# It should NOT be used in a production environment.
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)