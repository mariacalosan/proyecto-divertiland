from django.urls import path
from .views import Lista, Crear, Detalle, Eliminar, Editar

urlpatterns = [
    path('', Lista.as_view(), name='lista'),
    path('<int:pk>/', Detalle.as_view(), name='detalle'),
    path('editar/<int:pk>/', Editar, name='editar'),
    path('crear/', Crear, name='crear'),
    path('eliminar/<int:pk>/', Eliminar, name='eliminar'),
]
