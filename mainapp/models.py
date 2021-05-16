from django.db import models
import datetime
from django.utils import timezone
from django.contrib.auth.models import User


# class PrivateDisc (models.Model):
#     discName = models.CharField(max_length=20)
#
#     def __str__(self):
#         return self.discName

#
# class User (models.Model):
#     privateDisc = models.ForeignKey(PrivateDisc, on_delete=models.CASCADE)
#     username = models.CharField(max_length=20)
#     password = models.CharField(max_length=20, default='password')
#
#     def __str__(self):
#         return self.username


class Directory (models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    directoryName = models.CharField(max_length=20)

    def __str__(self):
        return self.directoryName


class File (models.Model):
    fileName = models.CharField(max_length=30)
    extension = models.CharField(max_length=4, default='none')
    content = models.FileField(default='No file loaded')
    directory = models.ForeignKey(Directory, on_delete=models.CASCADE)
    uploadDate = models.DateTimeField()
    inBin = models.BooleanField(default=False)
    isFavourite = models.BooleanField(default=False)

    def __str__(self):
        return self.fileName + "." + self.extension

    def move_to_bin(self):
        self.inBin = True

    def make_favourite(self):
        self.isFavourite = True

    def return_from_bin(self):
        self.inBin = False

    def unmake_favourite(self):
        self.isFavourite = False


class PublicLink (models.Model):
    file = models.ForeignKey(File, on_delete=models.CASCADE)
    URL = models.URLField(max_length=50)
    generationDate = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.URL

    def isExpired(self):
        return self.generationDate >= timezone.now() - datetime.timedelta(days=7)
