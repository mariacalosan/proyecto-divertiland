from django.urls import path, include
from . import views


app_name = 'aplicacion'

urlpatterns = [
    path('', views.index, name='index'),
]