from django.db import models
from django.core.validators import ValidationError

class Contact(models.Model):
    name = models.CharField(max_length=64)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    message = models.TextField()

    def clean(self):
        if len(self.message) < 100:
            raise ValidationError("The message must be at least 10 characters long.")

    def __str__(self):
        return self.name
