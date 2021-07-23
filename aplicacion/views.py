from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse
from . import models


def index(request):
    return render(request, 'aplicacion/index.html')
