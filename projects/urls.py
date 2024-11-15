from django.urls import path
from . import views

#from .views import project_list, project_detail

urlpatterns = [
    path('', views.project_list, name='project_list'),
    path('project/<int:pk>/', views.project_detail, name='project_detail'),
]
