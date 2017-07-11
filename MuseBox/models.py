from django.db import models
import csv
import os

class Song(models.Model):
    title = models.CharField(max_length=100,null=True)
    album = models.CharField(max_length=100,null=True)
    artistLocation = models.CharField(max_length=100, null=True)
    artistName = models.CharField(max_length=100,null=True)
    duration = models.DecimalField(max_digits=20,decimal_places=3, null=True)
    keySignature = models.DecimalField(max_digits=20,decimal_places=3, null=True)
    popularity = models.DecimalField(max_digits=20,decimal_places=7,null=True)
    timeSignature = models.DecimalField(max_digits=20,decimal_places=3, null=True)
    year = models.IntegerField(null=True)
    artistFamiliarity = models.DecimalField(max_digits=20,decimal_places=7,null=True)
    artistPopularity = models.DecimalField(max_digits=20,decimal_places=7,null=True)
    oneStarArtistPopularity = models.IntegerField(null=True)
    twoStarArtistPopularity = models.IntegerField(null=True)
    threeStarArtistPopularity = models.IntegerField(null=True)
    fourStarArtistPopularity = models.IntegerField(null=True)
    fiveStarArtistPopularity = models.IntegerField(null=True)
    categoryRapHipHopRnb = models.IntegerField(null=True)
    categoryRock = models.IntegerField(null=True)
    categoryFolkCeltic = models.IntegerField(null=True)
    categoryElectronicTrance = models.IntegerField(null=True)
    categoryMetal = models.IntegerField(null=True)
    categoryPunkGrungeSka = models.IntegerField(null=True)
    categoryPopChart = models.IntegerField(null=True)
    categoryJazzBlues = models.IntegerField(null=True)
    categoryCountry = models.IntegerField(null=True)
    categorySoulReggaeFunk = models.IntegerField(null=True)
    categoryDance = models.IntegerField(null=True)


class SongManager(models.Manager):

    @staticmethod
    def findBestMatch(song1,song2,song3):
        # first, find these 3 songs in the DB
        userSongs = SongManager.retrieveSongsDB([song1,song2,song3])
        #
        # DATA Mining here
        #

    @staticmethod
    def retrieveSongsDB(userSongsTitle):
        result = []
        for value in userSongsTitle:
            song = list(Song.objects.filter(title__icontains=value))
            result.append(song[0])
        return result

    @staticmethod
    def initDB():
        dir = os.path.dirname(__file__)
        filePath = os.path.join(dir, 'static','MuseBox','SongDB_FINAL.csv')
        with open(filePath) as f:
            reader = csv.reader(f)
            next(reader)
            for row in reader:
                _, created = Song.objects.get_or_create(
                    title=row[1],
                    album=row[2],
                    artistLocation=row[3],
                    artistName=row[4],
                    duration=row[5],
                    keySignature=row[6],
                    popularity=row[7],
                    timeSignature=row[9],
                    year=row[10],
                    artistFamiliarity=row[11],
                    artistPopularity=row[12],
                    oneStarArtistPopularity=row[13],
                    twoStarArtistPopularity=row[14],
                    threeStarArtistPopularity=row[15],
                    fourStarArtistPopularity=row[16],
                    fiveStarArtistPopularity=row[17],
                    categoryRapHipHopRnb=row[18],
                    categoryRock=row[19],
                    categoryFolkCeltic=row[20],
                    categoryElectronicTrance=row[21],
                    categoryMetal=row[22],
                    categoryPunkGrungeSka=row[23],
                    categoryPopChart=row[24],
                    categoryJazzBlues=row[25],
                    categoryCountry=row[26],
                    categorySoulReggaeFunk=row[27],
                    categoryDance=row[28],
                    )
                    # creates a tuple of the new object or
                    # current object and a boolean of if it was created
