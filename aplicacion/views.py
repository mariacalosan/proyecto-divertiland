from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse
from .models import ventas,Cliente,atracciones,carrito,empleado,usuario
# Create your views here.

def index(request):
    return render(request, 'aplicacion/index.html')

