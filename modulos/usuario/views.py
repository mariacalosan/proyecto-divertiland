from .models import Cliente
from django.shortcuts import render
from django.views.generic import CreateView
from modulos.usuario.forms import ClienteForm, RegistroForm
from modulos.usuario.models import Cliente
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.contrib.auth import logout


class RegistroUsuario(CreateView):
		model = User

		form_class = RegistroForm
		second_form_class = ClienteForm

		template_name = "usuario/registrar.html"
		success_url = reverse_lazy('index')

		def get_context_data(self, **kwargs):
			context = super(RegistroUsuario, self).get_context_data(**kwargs)
			if 'form' not in context:
				context['form'] = self.form_class(self.request.GET)
			if 'form2' not in context:
				context['form2'] = self.second_form_class(self.request.GET)
			return context

		# Get = traer, post = guardar, put = actualizar (completo), patch actualizar (parcial) y delete (borrar)
		def post(self, request, *args, **kwargs):
			self.object = self.get_object

			formulario_usuario = self.form_class(request.POST) # Formulario: Usuario - traer informacion que tenia en el formulario
			formulario_cliente = self.second_form_class(request.POST)

			if formulario_usuario.is_valid() and formulario_cliente.is_valid():
				usuario = formulario_usuario.save(commit=False)
				cliente = formulario_cliente.save(commit=False)

				#	este try control de errores si hay un error  va ejecutar la parte del except (linea 48)
				try:
					usuario.save()

					cliente.usuario = usuario
					cliente.save()

					# si el usuario se registra exitosamente entonces lo va a dirigir a el index(home)
					return HttpResponseRedirect(self.get_success_url())
				except Exception as e:
					# print imprime en la terminal lo que se le envie (le dicen logs)
					print('error', e)

			# si el formulario no esta correcto lo va a dirigir a la data que el usario ya tenia para que vuelva a ingresar los datos correctamente 
			return self.render_to_response(self.get_context_data(form=formulario_usuario, form2=formulario_cliente))

def logout_view(request):
    # Desconectar usuario
    logout(request)

    # Redirigir a la página de inicio
    return HttpResponseRedirect(reverse_lazy('index'))