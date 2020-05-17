from django.db import models
from django.utils import timezone

class Jasoseol(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title