from django.db import models
from datetime import date
from django.contrib.auth.models import User


class AuditModel(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	class Meta:
		abstract = True


class Client(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	identificacion = models.PositiveBigIntegerField()
	date_birth = models.DateField()
	address = models.CharField(max_length=150)
	phone = models.PositiveBigIntegerField()

	@property
	def age(self):
		today = date.today()
		return today.year - self.date_birth.year - ((today.month, today.day) < (self.date_birth.month, self.date_birth.day))


class Attraction (AuditModel):
	name = models.CharField(max_length=100)
	capacity = models.SmallIntegerField(default=1)
	price = models.DecimalField(null=False, decimal_places=20, max_digits=100)


class Sale(AuditModel):
	price = models.DecimalField(decimal_places=20, max_digits=100)
	client = models.ForeignKey(Client, on_delete=models.DO_NOTHING)


class Carrito(AuditModel):
	attractions = models.ForeignKey(Attraction, on_delete=models.DO_NOTHING)
	sales = models.ForeignKey(Sale, on_delete=models.DO_NOTHING)
	costo = models.DecimalField(null=False, decimal_places=20, max_digits=100)
	cantidad = models.IntegerField(null=False)
	total = models.DecimalField(null=False, decimal_places=20, max_digits=100)
