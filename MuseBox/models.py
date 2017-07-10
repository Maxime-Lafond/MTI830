from django.db import models
import csv

class Song(models.Model):
    title = models.CharField(max_length=100,null=True)
    album = models.CharField(max_length=100,null=True)
    artistLocation = models.CharField(max_length=100, null=True)
    artistName = models.CharField(max_length=100,null=True)
    duration = models.DecimalField(max_digits=20,decimal_places=3, null=True)
    keySignature = models.DecimalField(max_digits=20,decimal_places=3, null=True)
    popularity = models.DecimalField(max_digits=20,decimal_places=7,null=True)
    timeSignature = models.DecimalField(max_digits=20,decimal_places=3, null=True)
    year = models.DecimalField(max_digits=20,decimal_places=3, null=True)
    artistFamiliarity = models.DecimalField(max_digits=20,decimal_places=7,null=True)
    artistPopularity = models.DecimalField(max_digits=20,decimal_places=7,null=True)
    oneStarArtistPopularity = models.DecimalField(max_digits=20,decimal_places=3, null=True)
    twoStarArtistPopularity = models.DecimalField(max_digits=20,decimal_places=3, null=True)
    threeStarArtistPopularity = models.DecimalField(max_digits=20,decimal_places=3, null=True)
    fourStarArtistPopularity = models.DecimalField(max_digits=20,decimal_places=3, null=True)
    fiveStarArtistPopularity = models.DecimalField(max_digits=20,decimal_places=3, null=True)
    categoryRapHipHopRnb = models.DecimalField(max_digits=20,decimal_places=3, null=True)
    categoryRock = models.DecimalField(max_digits=20,decimal_places=3, null=True)
    categoryFolkCeltic = models.DecimalField(max_digits=20,decimal_places=3, null=True)
    categoryElectronicTrance = models.DecimalField(max_digits=20,decimal_places=3, null=True)
    categoryMetal = models.DecimalField(max_digits=20,decimal_places=3, null=True)
    categoryPunkGrungeSka = models.DecimalField(max_digits=20,decimal_places=3, null=True)
    categoryPopChart = models.DecimalField(max_digits=20,decimal_places=3, null=True)
    categoryJazzBlues = models.DecimalField(max_digits=20,decimal_places=3, null=True)
    categoryCountry = models.DecimalField(max_digits=20,decimal_places=3, null=True)
    categorySoulReggaeFunk = models.DecimalField(max_digits=20,decimal_places=3, null=True)
    categoryDance = models.DecimalField(max_digits=20,decimal_places=3, null=True)

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
        with open('/Users/max/PycharmProjects/mti830/MuseBox/static/MuseBox/SongDB_FINAL.csv') as f:
            reader = csv.reader(f)
            i = 0
            for row in reader:
                if i != 0:
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
                i = i + 1
