from django.db import models

# Create your models hitertools import


class Youtube(models.Model):
    title = models.CharField(max_length=255)
    video_id = models.CharField(max_length=20)
    url = models.URLField()