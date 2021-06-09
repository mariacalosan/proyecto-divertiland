from django.urls import path
from django.contrib import admin

from . import views

app_name = 'aplicacion'

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.index, name='index'),
]