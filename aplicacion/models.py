from django.db import models
from datetime import date
from django.contrib.auth.models import User

'''
class Sale(AuditModel):
	price = models.DecimalField(decimal_places=20, max_digits=100)
	client = models.ForeignKey(Client, on_delete=models.DO_NOTHING)

class Carrito(AuditModel):
	attractions = models.ForeignKey(Attraction, on_delete=models.DO_NOTHING)
	sales = models.ForeignKey(Sale, on_delete=models.DO_NOTHING)
	costo = models.DecimalField(null=False, decimal_places=20, max_digits=100)
	cantidad = models.IntegerField(null=False)
	total = models.DecimalField(null=False, decimal_places=20, max_digits=100)
'''