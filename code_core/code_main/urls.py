from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.cesar_cipher, name='cesar_cipher'),
]