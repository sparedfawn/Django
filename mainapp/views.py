from django.http import HttpResponse, HttpResponseRedirect
from .models import *
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic


class Detailed(generic.DetailView):

    def __index__(self):
        return HttpResponse("test 1 2 3")
