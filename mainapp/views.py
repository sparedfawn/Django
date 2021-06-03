from .models import *
from django.shortcuts import render, redirect
from django.views import generic
from django.contrib.auth import authenticate, login, logout
from .forms import CreateUserForm, CreateDirectoryForm, UploadFileForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.utils import timezone
from django.http import FileResponse, HttpResponseNotFound

from .decorators import check_recaptcha


max_disc_space = 1000000000


def IndexView(request):
    return render(request, 'mainapp/index.html')


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
        overall = 0
        for directory in request.user.directory_set.all():
            for file in directory.file_set.all():
                overall += file.content.size

        stock = form.save(commit=False)
        if overall + stock.content.size < max_disc_space:
            stock.directory = Directory(pk)
            stock.uploadDate = timezone.now()
            name = stock.content.name
            index = name.find('.')
            stock.fileName = name[:index]
            stock.extension = name[index+1:]
            stock.save()
            return redirect('../{}'.format(pk))
        else:
            messages.info('You ran out of space in your cloud.')
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


@login_required(login_url='login')
def cut(request, directory_key):
    context = {
        'directory_key': directory_key
    }
    return render(request, 'mainapp/cut.html', context)


@login_required(login_url='login')
def cut_function(request, directory_key, file_key):
    request.session['operation_type'] = 'cut'
    request.session['operation_object'] = file_key
    return redirect('../../{}'.format(directory_key))


@login_required(login_url='login')
def paste_function(request, directory_key):
    object_key = request.session.get('operation_object')
    operation_type = request.session.get('operation_type')
    if operation_type == 'cut':
        file = File.objects.get(pk=int(object_key))
        file.directory_id = directory_key
        file.save()
        request.session['operation_type'] = 'none'
        request.session['operation_object'] = 0
        return redirect('../{}'.format(directory_key))
    elif operation_type == 'copy':
        file = File()
        copied_file = File.objects.get(pk=int(object_key))
        file.fileName = copied_file.fileName
        file.extension = copied_file.extension
        file.content = copied_file.content
        file.directory_id = directory_key
        file.uploadDate = copied_file.uploadDate
        file.save()
        return redirect('../{}'.format(directory_key))
    else:
        print('operation not possible')

    return redirect('../{}'.format(directory_key))


@login_required(login_url='login')
def copy(request, directory_key):
    context = {
        'directory_key': directory_key
    }
    return render(request, 'mainapp/copy.html', context)


@login_required(login_url='login')
def copy_function(request, directory_key, file_key):
    request.session['operation_type'] = 'copy'
    request.session['operation_object'] = file_key
    return redirect('../../{}'.format(directory_key))


@login_required(login_url='login')
def download(request, directory_key):
    context = {
        'directory_key': directory_key
    }
    return render(request, 'mainapp/download.html', context)


@login_required(login_url='login')
def download_function(request, directory_key, file_key):
    file = File.objects.get(pk=file_key)
    content = file.content.path
    response = FileResponse(open(content, 'rb'))
    return response


@login_required(login_url='login')
def share_function(request, directory_key):
    if request.method == 'POST':
        file = request.POST.get('file_key', None)
        url = PublicLink()
        url.file_id = file
        url.generationDate = timezone.now()
        url.URL = '{}{}{}{}{}{}{}'.format(file, url.generationDate.year, url.generationDate.month, url.generationDate.day, url.generationDate.hour, url.generationDate.minute, url.generationDate.second)
        url.save()
        messages.info(request, 'Your generated link is: e-disk.herokuapp.com/share/{}'.format(url.URL))
        return redirect('../{}'.format(directory_key))

    context = {
        'directory_key': directory_key
    }
    return render(request, 'mainapp/share.html', context)


def share(request, url_path):
    url_query = PublicLink.objects.filter()
    for url in url_query:
        if str(url_path) == str(url):
            file_key = url.file_id
            file = File.objects.get(pk=file_key)
            content = file.content.path
            response = FileResponse(open(content, 'rb'))
            return response

    return HttpResponseNotFound('No such file shared')


@login_required(login_url='login')
def share_favourite_function(request):
    if request.method == 'POST':
        file = request.POST.get('file_key', None)
        url = PublicLink()
        url.file_id = file
        url.generationDate = timezone.now()
        url.URL = '{}{}{}{}{}{}{}'.format(file, url.generationDate.year, url.generationDate.month, url.generationDate.day, url.generationDate.hour, url.generationDate.minute, url.generationDate.second)
        url.save()
        messages.info(request, 'Your generated link is: localhost:8000/share/{}'.format(url.URL))
        return redirect('../favourites')

    return render(request, 'mainapp/share_favourite.html')


@login_required(login_url='login')
def download_favourite(request):
    return render(request, "mainapp/download_favourite.html")


@login_required(login_url='login')
def download_favourite_function(request, file_key):
    file = File.objects.get(pk=file_key)
    content = file.content.path
    response = FileResponse(open(content, 'rb'))
    return response
