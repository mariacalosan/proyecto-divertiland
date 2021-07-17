from django.db import models
from django.utils import timezone

class AuditarModel(models.Model):
	fecha_creacion = models.DateTimeField(editable=False)
	fecha_actualizacion = models.DateTimeField(editable=False)

	def save(self, *args, **kwargs):
			if not self.fecha_creacion:
					self.fecha_creacion = timezone.now()
					self.fecha_actualizacion = timezone.now()

			self.fecha_actualizacion = timezone.now()
			return super(AuditarModel, self).save(*args, **kwargs)

	class Meta:
		abstract = True