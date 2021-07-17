from django.db import models
from datetime import datetime
from aplicacion.models import AuditarModel
from modulos.atraccion.models import Atraccion
from modulos.usuario.models import Cliente

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

