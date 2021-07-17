from proyecto.models import AuditarModel
from django.db import models
from datetime import datetime
from proyecto.models import AuditarModel
from apps.atraccion.models import Atraccion
from apps.usuario.models import Cliente

# Create your models here.
# clase/modelo
class Carrito(AuditarModel):
    # atributos
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    pagado = models.BooleanField(default=False)


class ItemCarrito(AuditarModel):
    atraccion = models.ForeignKey(Atraccion, on_delete=models.CASCADE)
    carrito = models.ForeignKey(Carrito, on_delete=models.CASCADE)

    def __str__(self):
        return  self.carrito.cliente.usuario.username + " - " + self.atraccion.nombre

