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
        return redirect('drive')

    context = {
        'form': form,
        'directory_key': pk,
    }
    return render(request, 'mainapp/upload_file.html', context)
