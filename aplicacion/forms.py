#importe el models importe la libreria de forms para poder tranajar en los formularios he importe el campode fields 
from django import forms
from django.db import models
from django.forms import fields
from .models import Clientes,Promociones,Atracciones

class PromocionesForm(forms.ModelForm):
    class Meta:
        model=Promociones
        fields='__all__'

class ClienteForm(forms.ModelForm):
    class Meta:
        model=Clientes
        fields= '__all__'

class AtraccionesForm(forms.ModelForm):
    class Meta:
        model=Atracciones
        fields='__all__'

