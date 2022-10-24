from django.shortcuts import render
from .models import Post
from django.utils import timezone

def lista_de_post(request):
    posts =Post.objects.filter(fecha_de_publicacion__lte=timezone.now()).order_by('fecha_de_publicacion')
    return render(request, 'blog/lista_de_post.html', {'posts': posts})
