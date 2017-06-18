from django.db import models
import csv

class Song(models.Model):
    title = models.CharField(max_length=100)
    album = models.CharField(max_length=100)
    artistLocation = models.CharField(max_length=100, null=True)
    artistName = models.CharField(max_length=100, null=True)
    duration = models.DecimalField(max_digits=20,decimal_places=3, null=True)
    popularity = models.CharField(max_length=100, null=True)
    year = models.IntegerField(null=True)
    artistFamiliarity = models.DecimalField(max_digits=20,decimal_places=1, null=True)
    artistPopularity = models.DecimalField(max_digits=20,decimal_places=1, null=True)
    gender1 = models.CharField(max_length=100, null=True)
    gender2 = models.CharField(max_length=100, null=True)
    gender3 = models.CharField(max_length=100, null=True)
    gender4 = models.CharField(max_length=100, null=True)

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

    @staticmethod
    def initDB():
        with open('/Users/maximelafond/PycharmProjects/mti830/MuseBox/static/MuseBox/SongDB.csv') as f:
            reader = csv.reader(f)
            i = 0
            for row in reader:
                if i != 0:
                    _, created = Song.objects.get_or_create(
                        title=row[3],
                        album=row[6],
                        artistLocation=row[8],
                        artistName=row[12],
                        duration=row[14],
                        popularity=row[17],
                        year=row[21],
                        artistFamiliarity=row[22],
                        artistPopularity=row[23],
                        gender1=row[24],
                        gender2=row[25],
                        gender3=row[26],
                        gender4=row[27],
                    )
                    # creates a tuple of the new object or
                    # current object and a boolean of if it was created
                i = i + 1
