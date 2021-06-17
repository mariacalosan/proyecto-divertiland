from django.shortcuts import render
from django.views.generic import CreateView
from apps.usuario.forms import RegistroForm
from django.contrib.auth.models import User
from django.urls import reverse_lazy


class RegistroUsuario(CreateView):
	model = User
	template_name = "usuario/registrar.html"
	form_class = RegistroForm
	success_url = reverse_lazy('mascota:mascota_listar')

