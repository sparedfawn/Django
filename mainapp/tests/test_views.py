from django.test import TestCase, Client
from django.urls import reverse


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()

    def test_IndexView_GET(self):
        response = self.client.get(reverse('home'))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'mainapp/index.html')

    def test_register_GET(self):
        response = self.client.get(reverse('register'))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'mainapp/sign-up.html')

    def test_login_GET(self):
        response = self.client.get(reverse('login'))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'mainapp/sign-in.html')

    def test_drivePage_GET(self):
        response = self.client.get(reverse('drive'))

        self.assertEquals(response.status_code, 302)

    def test_logoutUser_GET(self):
        response = self.client.get(reverse('logout'))

        self.assertEquals(response.status_code, 302)

    def test_binPage_GET(self):
        response = self.client.get(reverse('bin'))

        self.assertEquals(response.status_code, 302)

    def test_favouritePage_GET(self):
        response = self.client.get(reverse('favourite'))

        self.assertEquals(response.status_code, 302)

    def test_register_POST(self):
        response = self.client.post(reverse('register'), {
            'username': 'test_user',
            'email': 'test@gmail.com',
            'password1': 'haslo123',
            'password2': 'haslo123'
        })

        self.assertEquals(response.status_code, 302)

    def test_login_POST(self):
        response = self.client.post(reverse('login'), {
            'username': 'admin',
            'password': 'admin',
        })

        self.assertEquals(response.status_code, 200)

    def test_register_POST_no_data(self):
        response = self.client.post(reverse('register'))

        self.assertEquals(response.status_code, 200)

    def test_login_POST_no_data(self):
        response = self.client.post(reverse('login'))

        self.assertEquals(response.status_code, 200)

    def test_inDirectory_GET(self):
        response = self.client.get(reverse('inDirectory', args=[1]))

        self.assertEquals(response.status_code, 302)

    def test_create_directory_POST(self):
        response = self.client.post(reverse('create_directory'), {
            'directoryName': 'test_name'
        })

        self.assertEquals(response.status_code, 302)

    def test_create_directory_POST_no_data(self):
        response = self.client.post(reverse('create_directory'))

        self.assertEquals(response.status_code, 302)

    def test_create_directory_GET(self):
        response = self.client.get(reverse('create_directory'))

        self.assertEquals(response.status_code, 302)

    def test_rename_directory_GET(self):
        response = self.client.get(reverse('rename_directory'))

        self.assertEquals(response.status_code, 302)

    def test_rename_directory_function_GET(self):
        response = self.client.get(reverse('rename_directory_function', args=[1]))

        self.assertEquals(response.status_code, 302)

    def test_rename_directory_function_POST(self):
        response = self.client.post(reverse('rename_directory_function', args=[1]), {
            'directoryName': 'test_name'
        })

        self.assertEquals(response.status_code, 302)

    def test_rename_directory_function_POST_no_data(self):
        response = self.client.post(reverse('rename_directory_function', args=[1]))

        self.assertEquals(response.status_code, 302)

    def test_delete_directory_GET(self):
        response = self.client.get(reverse('delete_directory'))

        self.assertEquals(response.status_code, 302)

    def test_rename_file_GET(self):
        response = self.client.get(reverse('rename_file', args=[1]))

        self.assertEquals(response.status_code, 302)

    def test_rename_file_function_GET(self):
        response = self.client.get(reverse('rename_file_function', args=[1, 2]))

        self.assertEquals(response.status_code, 302)

    def test_rename_file_function_POST(self):
        response = self.client.post(reverse('rename_file_function', args=[1, 2]), {
            'fileName': 'test_name'
        })

        self.assertEquals(response.status_code, 302)

    def test_rename_file_function_POST_no_data(self):
        response = self.client.post(reverse('rename_file_function', args=[1, 2]))

        self.assertEquals(response.status_code, 302)

    def test_delete_directory_function_GET(self):
        response = self.client.get(reverse('delete_directory_function', args=[1]))

        self.assertEquals(response.status_code, 302)

    def test_delete_file_GET(self):
        response = self.client.get(reverse('delete_file', args=[1]))

        self.assertEquals(response.status_code, 302)

    def test_delete_file_function_GET(self):
        response = self.client.get(reverse('delete_file_function', args=[1, 2]))

        self.assertEquals(response.status_code, 302)

    def test_make_favourite_GET(self):
        response = self.client.get(reverse('make_favourite', args=[1]))

        self.assertEquals(response.status_code, 302)

    def test_make_favourite_function_GET(self):
        response = self.client.get(reverse('make_favourite_function', args=[1, 2]))

        self.assertEquals(response.status_code, 302)

    def test_move_to_bin_GET(self):
        response = self.client.get(reverse('move_to_bin', args=[1]))

        self.assertEquals(response.status_code, 302)

    def test_move_to_bin_function(self):
        response = self.client.get(reverse('move_to_bin_function', args=[1, 2]))

        self.assertEquals(response.status_code, 302)

    def test_restore_file_GET(self):
        response = self.client.get(reverse('restore_file'))

        self.assertEquals(response.status_code, 302)

    def test_restore_file_function_GET(self):
        response = self.client.get(reverse('restore_file_function', args=[1]))

        self.assertEquals(response.status_code, 302)

    def test_unmake_favourite_GET(self):
        response = self.client.get(reverse('unmake_favourite'))

        self.assertEquals(response.status_code, 302)

    def test_unmake_favourite_function_GET(self):
        response = self.client.get(reverse('unmake_favourite_function', args=[1]))

        self.assertEquals(response.status_code, 302)

    def test_upload_file_GET(self):
        response = self.client.get(reverse('upload_file', args=[1]))

        self.assertEquals(response.status_code, 302)

    def test_upload_file_POST(self):
        response = self.client.post(reverse('upload_file', args=[1]), {
            'content': 'test_name.pdf'
        })

        self.assertEquals(response.status_code, 302)

    def test_upload_file_POST_no_data(self):
        response = self.client.post(reverse('rename_file_function', args=[1, 2]))

        self.assertEquals(response.status_code, 302)

    def test_rename_favourite_GET(self):
        response = self.client.get(reverse('rename_favourite'))

        self.assertEquals(response.status_code, 302)

    def test_rename_favourite_function_GET(self):
        response = self.client.get(reverse('rename_favourite_function', args=[1]))

        self.assertEquals(response.status_code, 302)

    def test_rename_favourite_function_POST(self):
        response = self.client.post(reverse('rename_favourite_function', args=[1]), {
            'name': 'test_name'
        })

        self.assertEquals(response.status_code, 302)

    def test_rename_favourite_function_POST_no_data(self):
        response = self.client.post(reverse('upload_file', args=[1]))

        self.assertEquals(response.status_code, 302)

    def test_cut_GET(self):
        response = self.client.get(reverse('cut', args=[1]))

        self.assertEquals(response.status_code, 302)

    def test_cut_function_GET(self):
        response = self.client.get(reverse('cut_function', args=[1, 2]))

        self.assertEquals(response.status_code, 302)

    def test_paste_function_GET(self):
        response = self.client.get(reverse('paste_function', args=[1]))

        self.assertEquals(response.status_code, 302)

    def test_copy_GET(self):
        response = self.client.get(reverse('copy', args=[1]))

        self.assertEquals(response.status_code, 302)

    def test_copy_function_GET(self):
        response = self.client.get(reverse('copy_function', args=[1, 2]))

        self.assertEquals(response.status_code, 302)

    def test_download_GET(self):
        response = self.client.get(reverse('download', args=[1]))

        self.assertEquals(response.status_code, 302)

    def test_download_function_GET(self):
        response = self.client.get(reverse('download_function', args=[1, 2]))

        self.assertEquals(response.status_code, 302)

    def test_share_function_GET(self):
        response = self.client.get(reverse('share_function', args=[1]))

        self.assertEquals(response.status_code, 302)

    def test_share_function_POST(self):
        response = self.client.post(reverse('rename_favourite_function', args=[1]), {
            'file': 2
        })

        self.assertEquals(response.status_code, 302)

    def test_share_function_POST_no_data(self):
        response = self.client.post(reverse('rename_favourite_function', args=[1]))

        self.assertEquals(response.status_code, 302)

    def test_share_GET(self):
        response = self.client.get(reverse('share', args=['123912838']))

        self.assertEquals(response.status_code, 404)

    def test_share_favourite_function_GET(self):
        response = self.client.get(reverse('share_favourite_function'))

        self.assertEquals(response.status_code, 302)

    def test_share_function_POST(self):
        response = self.client.post(reverse('share_favourite_function'), {
            'file': 2
        })

        self.assertEquals(response.status_code, 302)

    def test_share_function_POST_no_data(self):
        response = self.client.post(reverse('share_favourite_function'))

        self.assertEquals(response.status_code, 302)

    def test_download_favourite_GET(self):
        response = self.client.get(reverse('download_favourite'))

        self.assertEquals(response.status_code, 302)

    def test_download_favourite_function_GET(self):
        response = self.client.get(reverse('download_favourite_function', args=[1]))

        self.assertEquals(response.status_code, 302)
