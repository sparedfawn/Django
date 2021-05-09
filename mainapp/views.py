from .models import *
from django.shortcuts import render, redirect
from django.views import generic
from django.contrib.auth import authenticate, login, logout
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

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

        context = {'form':form}
        return render(request, 'mainapp/try3.html', context)


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
        return render(request, 'mainapp/Sing-in.html', context)


@login_required(login_url='login')
def drivePage(request):
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


# @login_required(login_url='login')
# def inDirectoryPage(request):
#     return render(request, 'mainapp/directory.html')

class InDirectoryView(generic.DetailView):
    model = Directory
    template_name = 'mainapp/directory.html'