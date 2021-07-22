from django.shortcuts import render, redirect
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from modulos.atraccion.models import Atraccion
from .models import Carrito, ItemCarrito
from django.contrib.auth.mixins import PermissionRequiredMixin
from modulos.usuario.models import Cliente

#Detalles de el carrito 
class DetalleCarrito(DetailView):
    model = Carrito
    template_name='venta/detalle_carrito.html'
    context_object_name = 'venta'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['items'] = ItemCarrito.objects.filter(carrito=self.object)
        return context


    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        if not self.request.user.is_authenticated:
            return redirect('index')

        if not self.object.cliente.usuario.id == self.request.user.id:
            return redirect('index')

        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)

#agregara a el carrito las atraciones 
def agregar_a_carrito(request, pk):
    atraccion = Atraccion.objects.get(pk=pk)
    cliente = Cliente.objects.get(usuario_id = request.user.id)
    carrito = Carrito.objects.filter(cliente = cliente, pagado = False).first()
    if not carrito:
        carrito = Carrito.objects.create(cliente = cliente)
        carrito.save()
    carritoItem = ItemCarrito.objects.create(carrito = carrito, atraccion = atraccion)
    carritoItem.save()
    return redirect('venta:carrito', pk = carrito.pk)

#eliminar de el carrito 
def eliminar_de_carrito(request, pk):
    carritoItem = ItemCarrito.objects.get(id = pk)
    carrito = carritoItem.carrito.pk
    if carritoItem:
        carritoItem.delete()
    return redirect('venta:carrito', pk = carrito)