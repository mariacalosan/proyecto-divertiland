from django.contrib import admin
from .models import *


admin.site.register(Attraction)
admin.site.register(Carrito)
admin.site.register(Sale)


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('identificacion', 'phone', 'age')
