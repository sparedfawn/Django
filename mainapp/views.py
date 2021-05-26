from .models import *
from django.shortcuts import render, redirect
from django.views import generic
from django.contrib.auth import authenticate, login, logout
from .forms import CreateUserForm, CreateDirectoryForm, UploadFileForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.utils import timezone

from .decorators import check_recaptcha


class IndexView(generic.ListView):
    template_name = 'mainapp/index.html'
    context_object_name = 'homeIndex'

    def get_queryset(self):
        return User.objects.order_by('-username')


@check_recaptcha
def register(request):
    if request.user.is_authenticated:
        return redirect('drive')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                if request.recaptcha_is_valid:
                    form.save()
                    messages.success(request, 'Account was created successfully')
                    return redirect('login')
                else:
                    return redirect('register')

        context = {'form': form}
        return render(request, 'mainapp/sign-up.html', context)


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('drive')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                if username == 'admin':
                    return redirect('../admin')
                else:
                    return redirect('drive')
            else:
                messages.info(request, 'Username or password is incorrect')

        context = {}
        return render(request, 'mainapp/sign-in.html', context)


@login_required(login_url='login')
def drivePage(request):
    if request.user.username == 'admin':
        return redirect('../admin')
    else:
        return render(request, 'mainapp/drive.html')


def logoutUser(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def binPage(request):
    return render(request, 'mainapp/bin.html')


@login_required(login_url='login')
def favouritePage(request):
    return render(request, 'mainapp/favourites.html')


class InDirectoryView(generic.DetailView):
    model = Directory
    template_name = 'mainapp/directory.html'


@login_required(login_url='login')
def create_directory(request):
    form = CreateDirectoryForm(request.POST or None)
    if form.is_valid():
        stock = form.save(commit=False)
        stock.user = request.user
        stock.save()
        return redirect('drive')

    context = {
        'form': form
    }
    return render(request, 'mainapp/create_directory.html', context)


@login_required(login_url='login')
def rename_directory(request):
    return render(request, 'mainapp/rename_directory.html')


@login_required(login_url='login')
def rename_directory_function(request, pk):
    if request.method == 'POST':
        name = request.POST.get('input_name')
        directory = Directory.objects.get(pk=pk)
        directory.directoryName = name
        directory.save()
        return redirect('../../drive')

    context = {
        'key': pk
    }
    return render(request, 'mainapp/rename_directory_function.html', context)


@login_required(login_url='login')
def delete_directory(request):
    return render(request, 'mainapp/delete_directory.html')


@login_required(login_url='login')
def rename_file(request, directory_key):
    context = {
        'directory_key': directory_key
    }
    return render(request, 'mainapp/rename_file.html', context)


@login_required(login_url='login')
def rename_file_function(request, directory_key, file_key):
    if request.method == 'POST':
        name = request.POST.get('input_name')
        file = File.objects.get(pk=file_key)
        file.fileName = name
        file.save()
        return redirect('../../{}'.format(directory_key))

    context = {
        'directory_key': directory_key,
        'file_key': file_key,
    }
    return render(request, 'mainapp/rename_file_function.html', context)


@login_required(login_url='login')
def delete_directory_function(request, pk):
    Directory.objects.get(pk=pk).delete()
    return redirect('drive')


@login_required(login_url='login')
def delete_file(request, directory_key):
    context = {
        'directory_key': directory_key
    }
    return render(request, 'mainapp/delete_file.html', context)


@login_required(login_url='login')
def delete_file_function(request, directory_key, file_key):
    File.objects.get(pk=file_key).delete()
    return redirect('../../../drive/{}'.format(directory_key))


@login_required(login_url='login')
def make_favourite(request, directory_key):
    context = {
        'directory_key': directory_key
    }
    return render(request, 'mainapp/make_favourite.html', context)


@login_required(login_url='login')
def make_favourite_function(request, directory_key, file_key):
    file = File.objects.get(pk=file_key)
    file.make_favourite()
    file.save()
    return redirect('../../../drive/{}'.format(directory_key))


@login_required(login_url='login')
def move_to_bin(request, directory_key):
    context = {
        'directory_key': directory_key
    }
    return render(request, 'mainapp/move_to_bin.html', context)


@login_required(login_url='login')
def move_to_bin_function(request, directory_key, file_key):
    file = File.objects.get(pk=file_key)
    file.move_to_bin()
    file.save()
    return redirect('../../../drive/{}'.format(directory_key))


@login_required(login_url='login')
def restore_file(request):
    return render(request, 'mainapp/restore_file.html')


@login_required(login_url='login')
def restore_file_function(request, file_key):
    file = File.objects.get(pk=file_key)
    file.return_from_bin()
    file.save()
    return redirect('../../bin')


@login_required(login_url='login')
def unmake_favourite(request):
    return render(request, 'mainapp/unmake_favourite.html')


@login_required(login_url='login')
def unmake_favourite_function(request, file_key):
    file = File.objects.get(pk=file_key)
    file.unmake_favourite()
    file.save()
    return redirect('../../favourites')


@login_required(login_url='login')
def upload_file(request, pk):
    form = UploadFileForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        stock = form.save(commit=False)
        stock.directory = Directory(pk)
        stock.uploadDate = timezone.now()
        name = stock.content.name
        index = name.find('.')
        stock.fileName = name[:index]
        stock.extension = name[index+1:]
        stock.save()
        return redirect('../{}'.format(pk))

    context = {
        'form': form,
        'directory_key': pk,
    }
    return render(request, 'mainapp/upload_file.html', context)


@login_required(login_url='login')
def rename_favourite(request):
    return render(request, 'mainapp/rename_favourite.html')


@login_required(login_url='login')
def rename_favourite_function(request, file_key):
    if request.method == 'POST':
        name = request.POST.get('input_name')
        file = File.objects.get(pk=file_key)
        file.fileName = name
        file.save()
        return redirect('../../favourites')

    context = {
        'file_key': file_key,
    }
    return render(request, 'mainapp/rename_favourite_function.html', context)
