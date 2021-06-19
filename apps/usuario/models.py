from django.db import models
from datetime import date
from django.contrib.auth.models import User

# Create your models here.
class Cliente(models.Model):
	usuario = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
	identificacion = models.PositiveBigIntegerField()
	fecha_nacimiento = models.DateField()
	direccion = models.CharField(max_length=150)
	telefono = models.CharField(max_length=50)

	@property
	def age(self):
		hoy = date.today()
		return hoy.year - self.fecha_nacimiento.year - ((hoy.month, hoy.day) < (self.fecha_nacimiento.month, self.fecha_nacimiento.day))
