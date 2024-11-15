from django.contrib import admin
from django.urls import path, include
from . import views

from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('contact/', include('contact.urls')),  # Contacts app
    # Future apps can be added here (e.g., 'projects/')
]
