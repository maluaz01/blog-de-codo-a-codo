from django.shortcuts import render
from django.utils import timezone
from .models import Post
from django.shortcuts import render, get_object_or_404
from .forms import Formulario_Admin
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.views.generic.base import TemplateView

def lista_de_post(request):

    posts = Post.objects.filter(fecha_de_publicacion__lte=timezone.now()).order_by('fecha_de_publicacion')
    return render(request, 'blog/lista_de_post.html', {'posts': posts})


def detalle_de_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/detalle_de_post.html', {'post': post})

@login_required
def nuevo_post(request):
    if request.method == "POST":
      form = Formulario_Admin(request.POST)
      if form.is_valid():
            post = form.save(commit=False)
            post.autor = request.user
            post.fecha_de_publicacion = timezone.now()
            post.save()
            return redirect('detalle_de_post', pk=post.pk)
    else:
            form = Formulario_Admin()
    return render(request, 'blog/post_edit.html', {'form': form})

@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = Formulario_Admin(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.autor = request.user
            post.fecha_de_publicacion = timezone.now()
            post.save()
            return redirect('detalle_de_post', pk=post.pk)
    else:
        form = Formulario_Admin(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})
'''
@login_required
def remover_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('lista_de_post')
'''
@login_required
def post_remove(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('lista_de_post')

def piedra(request):
    return render(request, 'blog/piedra.html')

def stonepaper(request):
    return render(request, 'blog/stonepaper.html')
