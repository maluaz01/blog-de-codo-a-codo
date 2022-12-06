from django.urls import path
from . import views

urlpatterns = [
    path('inicio/', views.inicio, name='inicio'),
    path('', views.lista_de_post, name='lista_de_post'),
    path('juego/', views.juego, name='juego'),
    path('cargar/', views.cargar, name='cargar'),
    path('ver_contenido/', views.ver_contenido, name='contenido'),
    path('perfil/', views.perfil, name='perfil'),


]
