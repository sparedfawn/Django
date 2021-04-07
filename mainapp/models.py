from django.db import models
import datetime
from django.utils import timezone


class User(models.Model):
    username = models.CharField(max_length=20)

    def __str__(self):
        return self.username


# stworzone pliki domyslnie trafiaja do kosza o id 1, ktory nie jest koszem a trzyma tam pliki,
# ktore po usunieciu trafiaja do przypisanego konkretnemu kontu koszowi
class Bin(models.Model):
    pass


class PrivateDisc(models.Model):
    userID = models.ForeignKey(User, on_delete=models.CASCADE)
    binID = models.ForeignKey(Bin, on_delete=models.CASCADE)
    discName = models.CharField(max_length=20)

    def __str__(self):
        return self.discName


class Directory(models.Model):
    discID = models.ForeignKey(PrivateDisc, on_delete=models.CASCADE)
    directoryName = models.CharField(max_length=20)

    # previouslyWorkingDirectory = models.Model

    def __str__(self):
        return self.directoryName


class File(models.Model):
    binID = models.ForeignKey(Bin, on_delete=models.CASCADE)
    directoryID = models.ForeignKey(Directory, on_delete=models.CASCADE)
    fileName = models.CharField(max_length=30)
    uploadDate = models.DateTimeField()
    content = models.FileField()

    def __str__(self):
        return self.fileName

    def create(self):
        self.binID = 1

    def move_to_bin(self):
        self.binID = self.directoryID.discID.binID


class PublicLink(models.Model):
    fileID = models.ForeignKey(File, on_delete=models.CASCADE)
    URL = models.URLField(max_length=50)
    generationDate = models.DateTimeField()

    def __str__(self):
        return self.URL

    def isExpired(self):
        return self.generationDate >= timezone.now() + datetime.timedelta(days=7)
