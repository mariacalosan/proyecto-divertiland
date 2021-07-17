from modulos.venta.models import Carrito, ItemCarrito
from modulos.usuario.models import Cliente

def informacion_carrito(request):
    if request.user.is_authenticated and not request.user.is_staff:
      cliente = Cliente.objects.get(usuario_id = request.user.id)
      carrito = Carrito.objects.filter(cliente = cliente, pagado = False).first()
      cantidadItems = ItemCarrito.objects.filter(carrito = carrito).count()
      return { 'carrito': carrito, 'cantidadItems': cantidadItems }
    return {}