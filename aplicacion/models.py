from django.db import models

class atracciones (models.Model):
  id_atracciones=models.AutoField(primary_key=True)
  nombre=models.CharField(max_length=100,null=False)
  capacidad=models.SmallIntegerField(null=False)
  precio=models.DecimalField(null=False,decimal_places =20,max_digits=100)
  fecha=models.DateTimeField(null=False,max_length=150)

class Cliente(models.Model):
  id_cliente=models.AutoField(primary_key=True)
  identificacion=models.IntegerField(null=False,unique=True)
  nombre=models.CharField(max_length=50,null=False)
  apellido=models.CharField(max_length=50,null=False)
  edad=models.IntegerField(null=False)
  direccion=models.CharField(max_length=50,null=False)
  telefono=models.CharField(max_length=50,null=False)

class ventas(models.Model):
  id_ventas=models.AutoField(primary_key=True)
  fecha=models.DateTimeField(null=False,max_length=150)
  costo=models.DecimalField(null=False,decimal_places=20,max_digits=100)
  cliente=models.ForeignKey(Cliente,on_delete=models.DO_NOTHING)

class empleado(models.Model):
  id_empleado=models.AutoField(primary_key=True)
  nombre=models.CharField(max_length=50,null=False)
  apellido=models.CharField(max_length=50,null=False)
  correoelectronico=models.EmailField(max_length=100,unique=True)
  identificacion=models.IntegerField(null=False,unique=True)

class carrito(models.Model):
  carrito_id_atracciones=models.ForeignKey(atracciones,on_delete=models.DO_NOTHING)
  carrito_id_ventas=models.ForeignKey(ventas,on_delete=models.DO_NOTHING)
  costo=models.DecimalField(null=False,decimal_places=20,max_digits=100)
  cantidad=models.IntegerField(null=False)
  total=models.DecimalField(null=False,decimal_places=20,max_digits=100)

class usuario(models.Model):
  ROL = (
    (1,'administrador'),
    (2,'cliente'),
    (3,'empleado'),
  )
  usuario=models.CharField(max_length=50,unique=True)
  correo=models.EmailField(max_length=100,null=False,unique=True)
  contraseña=models.CharField(max_length=100,unique=True,null=False)
  ROL=models.IntegerField(choices=ROL,default=3)

#Create your models here.
#en este archivo he creado los modulos respectivos de mi proyecto he puesto el rol de el modulo usuario que le permite el imgreso a a los modulos de cliente,empleado y a el administrador de la aplicacion 
