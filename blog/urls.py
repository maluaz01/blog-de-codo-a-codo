from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_de_post, name='lista_de_post'),
    path('post/<int:pk>/', views.detalle_de_post, name='detalle_de_post'),
    path('post/new', views.nuevo_post, name='nuevo_post'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('post/<pk>/remove/', views.post_remove, name='post_remove'),
    path('piedra/', views.piedra, name='piedra'),
]
