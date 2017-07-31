from django.db import models
from collections import Counter
import numpy
import operator
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
        try:
            return Song.objects.get(title=title)
        except:
            print("Error creating object for this title : ",title)
            return False

class SongManager(models.Manager):

    @staticmethod
    def initDB():
        with open('/Users/max/PycharmProjects/mti830/MuseBox/static/MuseBox/SongDB_FINAL.csv') as f:
            Song.objects.all().delete()
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


    @staticmethod
    def euclideanCalculationOnGender(user_songs,songs_set):
        euclidean_results = []

        # Variable initiation
        for idx in user_songs:
            euclidean_results.append({})

        # Calculation algorithm
        for song in songs_set:
            for idx, user_song in enumerate(user_songs):
                if song != user_song:
                    gender_attributes_song_dataset = numpy.array((song.categoryRock,song.categoryFolkCeltic,song.categoryElectronicTrance,song.categoryMetal,song.categoryPunkGrungeSka,
                                                                  song.categoryPopChart,song.categoryJazzBlues,song.categoryCountry,song.categorySoulReggaeFunk,song.categoryDance))
                    gender_attributes_song_user = numpy.array((user_song.categoryRock,user_song.categoryFolkCeltic,user_song.categoryElectronicTrance,user_song.categoryMetal,
                                                               user_song.categoryPunkGrungeSka,user_song.categoryPopChart,user_song.categoryJazzBlues,user_song.categoryCountry,
                                                               user_song.categorySoulReggaeFunk,user_song.categoryDance))
                    dist = numpy.linalg.norm(gender_attributes_song_dataset - gender_attributes_song_user)
                    euclidean_results[idx][song] = dist

        # Sort each list by distance ( < is the most valuable)
        for idx, my_list in enumerate(euclidean_results):
            euclidean_results[idx] = sorted(my_list.items(), key=operator.itemgetter(1))

        return euclidean_results


    @staticmethod
    def filteringListsByDistance(lists):
        for idx, my_list in enumerate(lists):
            count = 0
            for song, dist in my_list:
                # Take first 50 elements
                if count < 50 and dist != 0:
                    lists[idx] = lists[idx][:50]
                    break
                # Take all 0 distance, in case it is greater of 50
                if count > 50 and dist != 0:
                    lists[idx] = lists[idx][:count]
                    break
                count += 1

    @staticmethod
    def createFinalList(lists):
        result = []

        for my_list in lists:
            temp_list = []
            for song, dist in my_list:
                temp_list.append(song.title + " - " + song.artistName)
            result.append(temp_list[:3])

        return result

    @staticmethod
    def findBestMatch(user_songs):
        songs_set = list(Song.objects.all())

        # Euclidian algo on gender attributes. list for each user song of type dictionary (song:distance), ordered lower to higher.
        temp = SongManager.euclideanCalculationOnGender(user_songs,songs_set)

        # Take 50 first or all with distance 0.00
        SongManager.filteringListsByDistance(temp)


        return SongManager.createFinalList(temp)
