from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Project(models.Model):
    STATUS_CHOICES = [
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    featured_image = models.ImageField(upload_to='projects/featured/')
    images_gallery = models.ManyToManyField('ProjectImage', blank=True)
    project_link = models.URLField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    date = models.DateField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.title


class ProjectImage(models.Model):
    image = models.ImageField(upload_to='projects/gallery/')

    def __str__(self):
        return f"Image {self.image}"
