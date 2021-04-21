from .models import *
from django.shortcuts import render
from django.views import generic


class IndexView(generic.ListView):
    template_name = 'mainapp/home.html'
    context_object_name = 'homeIndex'

    def get_queryset(self):
        return User.objects.order_by('-username')


class DetailedView(generic.DetailView):
    model = User
    template_name = 'mainapp/personal.html'


class InDirectoryView(generic.DetailView):
    model = Directory
    template_name = 'mainapp/directory.html'


class BinView(generic.DetailView):
    model = User
    template_name = 'mainapp/bin.html'


class FavouriteView(generic.DetailView):
    model = User
    template_name = 'mainapp/favourites.html'


def register(request):
    return render(request, 'mainapp/register.html')
