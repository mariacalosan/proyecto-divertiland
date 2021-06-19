from apps.usuario.models import Cliente
from django.shortcuts import render
from django.views.generic import CreateView
from apps.usuario.forms import ClienteForm, RegistroForm
from django.contrib.auth.models import User
from django.urls import reverse_lazy


class RegistroUsuario(CreateView):
		model = User

		form_class = RegistroForm
		second_form_class = ClienteForm

		template_name = "usuario/registrar.html"
		success_url = reverse_lazy('aplicacion:index')

		def get_context_data(self, **kwargs):
			context = super(RegistroUsuario, self).get_context_data(**kwargs)
			if 'form' not in context:
				context['form'] = self.form_class(self.request.GET)
			if 'form2' not in context:
				context['form2'] = self.second_form_class(self.request.GET)
			return context
