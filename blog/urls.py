from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_de_post, name='lista_de_post'),
    path('juego/', views.juego, name='juego'),
    path('cargar/', views.cargar, name='cargar'),
]
