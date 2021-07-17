from django.db import models
from django.contrib.auth.models import User
from aplicacion.models import AuditarModel
from datetime import date


# Create your models here.
class Cliente(AuditarModel):
	usuario = models.OneToOneField(User, on_delete=models.CASCADE)
	identificacion = models.PositiveBigIntegerField()
	fecha_nacimiento = models.DateField()
	direccion = models.CharField(max_length=150)
	telefono = models.CharField(max_length=50)

	@property
	def edad(self):
		hoy = date.today()
		return hoy.year - self.fecha_nacimiento.year - ((hoy.month, hoy.day) < (self.fecha_nacimiento.month, self.fecha_nacimiento.day))
