from django.db import models

class Song(models.Model):
    title = models.CharField(max_length=30)
    author = models.CharField(max_length=30)
    album = models.CharField(max_length=30)
    category = models.CharField(max_length=30)

    @classmethod
    def create(cls, title):
        return cls(title=title)


class SongManager(models.Manager):
    @staticmethod
    def findBestMatch(song1,song2,song3):
        #
        # Do something here
        #
        return Song.create("Lose yourself")
