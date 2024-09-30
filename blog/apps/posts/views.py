from django.shortcuts import render
from .models import Posts

# Create your views here.

# vistas basadas en funciones
def posts(request):
    context = {}
    noticias = Posts.objects.all() # seleccionamos todos los objetos de posts
    context['noticias'] = noticias
    return render(request, "Posts/posts.html", context)

def about_us(request):
    return render(request, "Posts/about_us.html")

def registro(request):
    return render(request, "usuarios/registro.html")