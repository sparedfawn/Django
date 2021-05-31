from django.test import TestCase
from mainapp.models import *
from django.contrib.auth.models import User
from django.utils import timezone


class TestModels(TestCase):

    def setUp(self):
        self.directory1 = Directory.objects.create(
            user=User.objects.create(),
            directoryName='test_name',
        )

        self.file1 = File.objects.create(
            fileName='test_file',
            extension='pdf',
            directory=self.directory1,
            uploadDate=timezone.now(),
        )

        self.publicLink1 = PublicLink.objects.create(
            file=self.file1,
            URL='123451',
        )

    def test_directory_str(self):
        self.assertEquals(self.directory1.__str__(), self.directory1.directoryName)

    def test_file_str(self):
        name = '{}.{}'.format(self.file1.fileName, self.file1.extension)
        self.assertEquals(self.file1.__str__(), name)

    def test_public_link_str(self):
        self.assertEquals(self.publicLink1.__str__(), self.publicLink1.URL)

    def test_public_link_isExpired(self):
        self.assertTrue(self.publicLink1.isExpired())
