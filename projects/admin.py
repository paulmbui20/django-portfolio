from django.contrib import admin
from .models import Project, ProjectImage, Category

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'status', 'date', 'category']
    list_filter = ['status', 'category']

@admin.register(ProjectImage)
class ProjectImageAdmin(admin.ModelAdmin):
    list_display = ['id', 'image']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
