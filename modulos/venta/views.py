from django.shortcuts import render, redirect
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from modulos.atraccion.models import Atraccion
from .models import Carrito, ItemCarrito
from django.contrib.auth.mixins import PermissionRequiredMixin
from modulos.usuario.models import Cliente

# Historial Compras
class HistorialCompras(ListView):
    paginate_by = 3
    template_name='venta/historial_compras.html'
    context_object_name = 'historial'
    def get_queryset(self):
        cliente = Cliente.objects.get(usuario_id = self.request.user.id)
        queryset = Carrito.objects.order_by('-fecha_creacion').filter(cliente = cliente)
        return queryset

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

        if (not self.object.cliente.usuario.id == self.request.user.id) and (not self.request.user.is_staff):
            return redirect('index')

        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)


class AdminHistorialCompras(ListView):
    paginate_by = 3
    template_name='venta/historial_compras.html'
    context_object_name = 'historial'
    def get_queryset(self):
        queryset = Carrito.objects.order_by('-fecha_creacion').all()
        return queryset

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
    return redirect('venta:carrito', pk = pk)

def marcar_pagado(request, pk):
    if request.user.is_staff:
        carrito = Carrito.objects.get(pk = pk)
        carrito.pagado = not carrito.pagado
        carrito.save()
    return redirect('venta:carrito', pk = pk)

def eliminar_carrito(request, pk):
    if request.user.is_staff:
        carrito = Carrito.objects.get(pk = pk)
        if carrito:
            carrito.delete()
    return redirect('index')