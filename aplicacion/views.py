from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse
from rest_framework import viewsets
from . import models
from . import serializers


def index(request):
    return render(request, 'aplicacion/index.html')
