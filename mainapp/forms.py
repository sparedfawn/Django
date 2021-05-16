from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from . import models


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'u-border-3 u-border-no-left u-border-no-right '
                                                        'u-border-no-top u-border-white u-input u-input-rectangle',
                                               'placeholder': 'Username'}),
            'email': forms.EmailInput(attrs={'class': 'u-border-3 u-border-no-left u-border-no-right '
                                                      'u-border-no-top u-border-white u-input u-input-rectangle',
                                             'placeholder': 'E-mail'}),
        }

    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(
            attrs={
                'class': 'u-border-3 u-border-no-left u-border-no-right '
                         'u-border-no-top u-border-white u-input u-input-rectangle',
                'type': 'password', 'placeholder': 'Password'}),
    )

    password2 = forms.CharField(
        label="Confirm password",
        widget=forms.PasswordInput(
            attrs={
                'class': 'u-border-3 u-border-no-left u-border-no-right '
                         'u-border-no-top u-border-white u-input u-input-rectangle',
                'type': 'password', 'placeholder': 'Repeated password'}),
    )


class CreateDirectoryForm(forms.ModelForm):
    class Meta:
        model = models.Directory
        fields = ['directoryName']
        widgets = {
            'directoryName': forms.TextInput(attrs={
                'placeholder': 'new directory',
            })
        }


class UploadFileForm(forms.ModelForm):
    class Meta:
        model = models.File
        fields = ['content']

