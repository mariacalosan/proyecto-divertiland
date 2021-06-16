from django.urls import path, include
from django.contrib import admin
from rest_framework import routers

from . import views

app_name = 'aplicacion'

router = routers.DefaultRouter()
router.register(r'sales', views.SaleViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.index, name='index'),

    path('api/', include(router.urls))
]