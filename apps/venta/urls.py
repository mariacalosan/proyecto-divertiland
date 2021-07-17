from django.urls import path, include
from . import views

# Cart Urls
urlpatterns = [
    path('<int:pk>/', views.DetalleCarrito.as_view(), name='carrito'),
    path('agregar/<int:pk>/', views.agregar_a_carrito, name='agregar-a-carrito'),
    path('eliminar/<int:pk>/', views.eliminar_de_carrito, name='eliminar-de-carrito'),
]