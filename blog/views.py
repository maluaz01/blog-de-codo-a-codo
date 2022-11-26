from django.shortcuts import render
from .models import Post
from django.utils import timezone

from datetime import datetime
from multiprocessing import context
from django.http import HttpResponse, JsonResponse
from django.urls import reverse
from django.template import loader
from blog.forms import ContenidoForm
from django.contrib import messages


def inicio(request):
    return render(request, 'blog/index.html', {})

def ver_contenido(request):
    lista_posts = [
        {
            'titulo':'Titulo',
            'autor':'Autor',
            'categoria':'Categoria',
            'contenido':'Contenido'
        },
        {
            'titulo':'Titulo',
            'autor':'Autor',
            'categoria':'Categoria',
            'contenido':'Contenido'
        },
         {
            'titulo':'Titulo',
            'autor':'Autor',
            'categoria':'Categoria',
            'contenido':'Contenido'
        },
         {
            'titulo':'Titulo',
            'autor':'Autor',
            'categoria':'Categoria',
            'contenido':'Contenido'
        },
         {
            'titulo':'Titulo',
            'autor':'Autor',
            'categoria':'Categoria',
            'contenido':'Contenido'
        },
          {
            'titulo':'Titulo',
            'autor':'Autor',
            'categoria':'Categoria',
            'contenido':'Contenido'
        },
         {
            'titulo':'Titulo',
            'autor':'Autor',
            'categoria':'Categoria',
            'contenido':'Contenido'
        },
         {
            'titulo':'Titulo',
            'autor':'Autor',
            'categoria':'Categoria',
            'contenido':'Contenido'
        },
        {
            'titulo':'Titulo',
            'autor':'Autor',
            'categoria':'Categoria',
            'contenido':'Contenido'
        },
        
    ]

    return render(request, 'blog/ver_contenido.html', {'contenidos':lista_posts})


def perfil(request):
    return render(request, 'blog/perfil.html', {})

def lista_de_post(request):
    posts =Post.objects.filter(fecha_de_publicacion__lte=timezone.now()).order_by('fecha_de_publicacion')
    return render(request, 'blog/lista_de_post.html', {'posts': posts})

def juego(request):
    return render(request, 'blog/juego.html', {})

def cargar(request):
    
    if(request.method == 'POST'):
        contenido_form = ContenidoForm(request.POST)
        if(contenido_form.is_valid()):
            #enviar un email al administrado con los datos
            #guardar los datos en la base
            messages.success(request,'Muchas gracias compartir tu contenido')
            messages.info(request,'Otro mensajito')
            #deberia validar y realizar alguna accion
        else:
            messages.warning(request,'Por favor revisa los errores')
    else:
        contenido_form = ContenidoForm()

    return render(request,'blog/cargar.html',
                {'contenido_form':contenido_form})
