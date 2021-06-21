from django.db import models
from proyecto.models import AuditarModel

class Atraccion (AuditarModel):
	nombre = models.CharField(max_length=100)
	precio = models.DecimalField(null=False, decimal_places=20, max_digits=100)
	estado = models.BooleanField(default=True,blank=False)
	descripcion = models.CharField(max_length=1200)
	imagen = models.CharField(max_length=200)