from django.http import HttpResponse, HttpResponseRedirect
from .models import *
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic


class DetailedView(generic.DetailView):

    model = User
    template_name = 'mainapp/base.html'


class IndexView(generic.ListView):
    template_name = 'mainapp/home.html'
    context_object_name = 'homeIndex'

    def get_queryset(self):
        return User.objects.order_by('-username')
