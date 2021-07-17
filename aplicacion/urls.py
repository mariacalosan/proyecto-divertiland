from django.urls import path, include
from django.contrib import admin
from . import views


app_name = 'aplicacion'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('usuario/', include(('modulos.usuario.urls', 'usuario'), namespace='usuario')),
    path('atraccion/', include(('modulos.atraccion.urls', 'atraccion'), namespace='atraccion')),
    path('venta/', include(('modulos.venta.urls','venta'), namespace='venta')),
]