from apps.usuario.models import Cliente
from django.shortcuts import render
from django.views.generic import CreateView
from apps.usuario.forms import ClienteForm, RegistroForm
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect


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

# Get = traer, post = guardar, put = actualizar (completo), patch actualizar (parcial) y delete (borrar)
		def post(self, request, *args, **kwargs):
			self.object = self.get_object

			form = self.form_class(request.POST) # Formulario: Usuario - traer informacion que tenia en el formulario
			form2 = self.second_form_class(request.POST) # Formulario: Cliente


			if form.is_valid() and form2.is_valid():
				try:
						usuario = form.save()
						cliente = form2.save(commit=False)
						form2.usuario = usuario
						form2.save()
						# print('usuario', usuario)
						# print('form2.usuario', form2.usuario)
						# print('cliente', cliente)
						# print('cliente.usuario', cliente.usuario)
						print('cliente.identificacion', cliente.identificacion)
				except Exception as e:
					print('eeex', e)
				return HttpResponseRedirect(self.get_success_url())#si el usuario se registra exitosamente entonces lo va a dirigir a el index(home )
			else:
				return self.render_to_response(self.get_context_data(form=form, form2=form2))#si el formulario no esta correcto lo va a dirigir a la data que el usario ya tenia para que vuelva a ingresar los datos correctamente 
