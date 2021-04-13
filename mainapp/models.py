from django.db import models
import datetime
from django.utils import timezone


class User (models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20, default='password')

    def __str__(self):
        return self.username


class Bin (models.Model):
    pass


class PrivateDisc (models.Model):
    userID = models.ForeignKey(User, on_delete=models.CASCADE)
    binID = models.ForeignKey(Bin, on_delete=models.CASCADE)
    discName = models.CharField(max_length=20)

    def __str__(self):
        return self.discName


class Directory (models.Model):
    discID = models.ForeignKey(PrivateDisc, on_delete=models.CASCADE)
    directoryName = models.CharField(max_length=20)

    def __str__(self):
        return self.directoryName


class File (models.Model):
    fileName = models.CharField(max_length=30)
    content = models.FileField(default='No file loaded')
    directoryID = models.ForeignKey(Directory, on_delete=models.CASCADE)
    uploadDate = models.DateTimeField()
    inBin = models.BooleanField(default=False)

    def __str__(self):
        return self.fileName

    def move_to_bin(self):
        self.inBin = True


class PublicLink (models.Model):
    fileID = models.ForeignKey(File, on_delete=models.CASCADE)
    URL = models.URLField(max_length=50)
    generationDate = models.DateTimeField()

    def __str__(self):
        return self.URL

    def isExpired(self):
        return self.generationDate >= timezone.now() - datetime.timedelta(days=7)
