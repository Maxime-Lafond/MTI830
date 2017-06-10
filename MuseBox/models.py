from django.db import models

class Chanson(models.Model):
    title = models.CharField(max_length=30)
    author = models.CharField(max_length=30)
    album = models.CharField(max_length=30)
    category = models.CharField(max_length=30)
