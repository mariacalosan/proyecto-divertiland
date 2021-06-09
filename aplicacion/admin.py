from django.contrib import admin

from .models import usuario,ventas,Cliente,empleado,atracciones,carrito

admin.site.register(usuario)
admin.site.register(empleado)
admin.site.register(atracciones)
admin.site.register(carrito)
admin.site.register(ventas)
admin.site.register(Cliente)
# Register your models here.
