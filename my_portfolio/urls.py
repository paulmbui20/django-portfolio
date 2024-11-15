from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

from . import views

from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('contact/', include('contact.urls')),  # Contacts app
    path('projects/', include('projects.urls')), #projects app
    # Future apps can be added here (e.g., 'Blog')
]
if settings.DEBUG:  # Serve media files only in development
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
