from django.test import SimpleTestCase
from django.urls import resolve, reverse
from mainapp.views import *


class TestUrls(SimpleTestCase):

    def test_home_url_is_resolved(self):
        url = reverse('home')
        self.assertEquals(resolve(url).func, IndexView)

    def test_bin_url_is_resolved(self):
        url = reverse('bin')
        self.assertEquals(resolve(url).func, binPage)

    def test_favourite_url_is_resolved(self):
        url = reverse('favourite')
        self.assertEquals(resolve(url).func, favouritePage)

    def test_register_url_is_resolved(self):
        url = reverse('register')
        self.assertEquals(resolve(url).func, register)

    def test_login_url_is_resolved(self):
        url = reverse('login')
        self.assertEquals(resolve(url).func, loginPage)

    def test_upload_url_is_resolved(self):
        url = reverse('upload_file', args=[1])
        self.assertEquals(resolve(url).func, upload_file)

    def test_drive_url_is_resolved(self):
        url = reverse('drive')
        self.assertEquals(resolve(url).func, drivePage)

    def test_logout_url_is_resolved(self):
        url = reverse('logout')
        self.assertEquals(resolve(url).func, logoutUser)

    def test_create_directory_url_is_resolved(self):
        url = reverse('create_directory')
        self.assertEquals(resolve(url).func, create_directory)

    def test_rename_directory_url_is_resolved(self):
        url = reverse('rename_directory')
        self.assertEquals(resolve(url).func, rename_directory)

    def test_rename_directory_function_url_is_resolved(self):
        url = reverse('rename_directory_function', args=[1])
        self.assertEquals(resolve(url).func, rename_directory_function)

    def test_delete_directory_url_is_resolved(self):
        url = reverse('delete_directory')
        self.assertEquals(resolve(url).func, delete_directory)

    def test_delete_directory_function_url_is_resolved(self):
        url = reverse('delete_directory_function', args=[1])
        self.assertEquals(resolve(url).func, delete_directory_function)

    def test_rename_file_is_resolved(self):
        url = reverse('rename_file', args=[1])
        self.assertEquals(resolve(url).func, rename_file)

    def test_rename_file_function_url_is_resolved(self):
        url = reverse('rename_file_function', args=[1, 2])
        self.assertEquals(resolve(url).func, rename_file_function)

    def test_delete_file_url_is_resolved(self):
        url = reverse('delete_file', args=[1])
        self.assertEquals(resolve(url).func, delete_file)

    def test_delete_file_function_url_is_resolved(self):
        url = reverse('delete_file_function', args=[1, 2])
        self.assertEquals(resolve(url).func, delete_file_function)

    def test_make_favourite_url_is_resolved(self):
        url = reverse('make_favourite', args=[1])
        self.assertEquals(resolve(url).func, make_favourite)

    def test_make_favourite_function_url_is_resolved(self):
        url = reverse('make_favourite_function', args=[1, 2])
        self.assertEquals(resolve(url).func, make_favourite_function)

    def test_move_to_bin_url_is_resolved(self):
        url = reverse('move_to_bin', args=[1])
        self.assertEquals(resolve(url).func, move_to_bin)

    def test_move_to_bin_function_url_is_resolved(self):
        url = reverse('move_to_bin_function', args=[1, 2])
        self.assertEquals(resolve(url).func, move_to_bin_function)

    def test_restore_file_url_is_resolved(self):
        url = reverse('restore_file')
        self.assertEquals(resolve(url).func, restore_file)

    def test_restore_file_function_url_is_resolved(self):
        url = reverse('restore_file_function', args=[1])
        self.assertEquals(resolve(url).func, restore_file_function)

    def test_unmake_favourite_url_is_resolved(self):
        url = reverse('unmake_favourite')
        self.assertEquals(resolve(url).func, unmake_favourite)

    def test_unmake_favourite_function_url_is_resolved(self):
        url = reverse('unmake_favourite_function', args=[1])
        self.assertEquals(resolve(url).func, unmake_favourite_function)

    def test_cut_url_is_resolved(self):
        url = reverse('cut', args=[1])
        self.assertEquals(resolve(url).func, cut)

    def test_cut_function_url_is_resolved(self):
        url = reverse('cut_function', args=[1, 2])
        self.assertEquals(resolve(url).func, cut_function)

    def test_copy_url_is_resolved(self):
        url = reverse('copy', args=[1])
        self.assertEquals(resolve(url).func, copy)

    def test_copy_function_url_is_resolved(self):
        url = reverse('copy_function', args=[1, 2])
        self.assertEquals(resolve(url).func, copy_function)

    def test_paste_url_is_resolved(self):
        url = reverse('paste_function', args=[1])
        self.assertEquals(resolve(url).func, paste_function)

    def test_download_url_is_resolved(self):
        url = reverse('download', args=[1])
        self.assertEquals(resolve(url).func, download)

    def test_download_function_url_is_resolved(self):
        url = reverse('download_function', args=[1, 2])
        self.assertEquals(resolve(url).func, download_function)

    def test_share_function_url_is_resolved(self):
        url = reverse('share_function', args=[1])
        self.assertEquals(resolve(url).func, share_function)

    def test_share_favourite_url_is_resolved(self):
        url = reverse('share_favourite_function')
        self.assertEquals(resolve(url).func, share_favourite_function)

    def test_share_url_is_resolved(self):
        url = reverse('share', args=[1])
        self.assertEquals(resolve(url).func, share)

    def test_download_favourite_url_is_resolved(self):
        url = reverse('download_function', args=[1, 2])
        self.assertEquals(resolve(url).func, download_function)

    def test_download_favourite_function_url_is_resolved(self):
        url = reverse('download_favourite_function', args=[1])
        self.assertEquals(resolve(url).func, download_favourite_function)

    def test_inDirectory_url_is_resolved(self):
        url = reverse('inDirectory', args=[1])
        self.assertEquals(resolve(url).func.view_class, InDirectoryView)
