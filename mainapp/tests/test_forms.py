from django.test import TestCase
from mainapp.forms import *


class TestForms(TestCase):

    def test_CreateUserForm_valid_data(self):
        form = CreateUserForm(data={
            'username': 'test_user',
            'email': 'test@gmail.com',
            'password1': 'haslo123',
            'password2': 'haslo123',
        })

        self.assertTrue(form.is_valid())

    def test_CreateUserForm_no_data(self):
        form = CreateUserForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 3)

    def test_CreateUserForm_invalid_data(self):
        form = CreateUserForm(data={
            'username': 'test_user',
            'email': 'test@gmail.com',
            'password1': 'notsamepassword123',
            'password2': 'badpassword321',
        })

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 1)

    def test_CreateDirectoryForm_valid_data(self):
        form = CreateDirectoryForm(data={
            'directoryName': 'test_name',
        })

        self.assertTrue(form.is_valid())

    def test_CreateDirectoryForm_no_data(self):
        form = CreateDirectoryForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 1)

    def test_CreateDirectoryForm_invalid_data(self):
        form = CreateDirectoryForm(data={
            'username': 'veryveryverylongnamethatwillexceedthemodelassumption'
        })

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 1)

    def test_UploadFileForm_valid_data(self):
        form = UploadFileForm(data={
            'content': 'valid_content.pdf',
        })

        self.assertTrue(form.is_valid())
