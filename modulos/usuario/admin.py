from django.contrib import admin
from .models import Cliente


@admin.register(Cliente)
class Cliente(admin.ModelAdmin):
    list_display = 'usuario', 'identificacion', 'telefono', 'fecha_nacimiento', 'edad',
