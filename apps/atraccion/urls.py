from django.urls import path
from .views import Lista

urlpatterns=[
  path('', Lista.as_view(), name='lista'),
]