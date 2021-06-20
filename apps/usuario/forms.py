from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.forms import widgets
from apps.usuario.models import Cliente
import datetime


class RegistroForm(UserCreationForm, forms.ModelForm):

	class Meta:
		model = User
		fields = [
			'username',
			'first_name',
			'last_name',
			'email',
		]
		labels = {
			'username': 'Nombre de usuario',
			'first_name': 'Nombre',
			'last_name': 'Apellidos',
			'email': 'Correo',
		}
		widgets = {
			'username': forms.TextInput(attrs={'class': 'form-control'}),
			'first_name': forms.TextInput(attrs={'class': 'form-control'}),
			'last_name': forms.TextInput(attrs={'class': 'form-control'}),
			'email': forms.TextInput(attrs={'class': 'form-control'}),
		}
	def __init__(self, *args, **kwargs):
		super(RegistroForm, self).__init__(*args, **kwargs)

		self.fields['password1'].widget.attrs['class'] = 'form-control'
		self.fields['password2'].widget.attrs['class'] = 'form-control'

class ClienteForm(forms.ModelForm):

	class Meta:
		model = Cliente

		fields = [
			'identificacion',
			'fecha_nacimiento',
			'direccion',
			'telefono',
		]

		labels = {
			'identificacion': 'Numero de identificacion',
			'fecha_nacimiento': 'Fecha de nacimiento',
			'direccion': 'Direccion',
			'telefono': 'Numero de telefono'
		}

		YEARS = [x for x in range(datetime.datetime.now().year - 100, datetime.datetime.now().year - 18)]

		widgets = {
			'identificacion': forms.TextInput(attrs={'class': 'form-control'}),
			'fecha_nacimiento': forms.SelectDateWidget(years=YEARS, attrs={'class': 'form-control fecha-control'}),
			'direccion': forms.TextInput(attrs={'class': 'form-control'}),
			'telefono': forms.TextInput(attrs={'class': 'form-control'}),
		}

		# exclude = ('usuario',)