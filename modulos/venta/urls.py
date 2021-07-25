from django.urls import path, include
from . import views

# Cart Urls
urlpatterns = [
    path('ver/<int:pk>/', views.DetalleCarrito.as_view(), name='carrito'),
    path('agregar/<int:pk>/', views.agregar_a_carrito, name='agregar-a-carrito'),
    path('eliminar/<int:pk>/', views.eliminar_de_carrito, name='eliminar-de-carrito'),
    path('historico/', views.HistorialCompras.as_view(), name='historial'),
    path('admin/pagado/<int:pk>/', views.marcar_pagado, name='pagado'),
    path('admin/eliminar/<int:pk>/', views.eliminar_carrito, name='eliminar-carrito'),
    path('admin/historico/', views.AdminHistorialCompras.as_view(), name='historial-admin'),
]
