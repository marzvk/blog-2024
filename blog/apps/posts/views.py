from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .models import Posts, User
from .form import RegistroForm


# Create your views here.

# vistas basadas en funciones
def posts(request):
    context = {}
    noticias = Posts.objects.all() # seleccionamos todos los objetos de posts
    context['noticias'] = noticias
    return render(request, "Posts/posts.html", context)

def about_us(request):
    return render(request, "Posts/about_us.html")

def perfil(request, id):
    context = {}
    usuarios = User.objects.get(id=id)
    context['usuarios']= usuarios
    # print(usuarios)
    return render(request, "usuarios/perfil.html", context)

# vista basada en clase

class Registro(CreateView):
    form_class = RegistroForm
    success_url = reverse_lazy("noticias")
    template_name = "usuarios/registro.html"


def post_id(request, id):
    contexto = {}
    noticia = Posts.objects.get(id=id)
    contexto["noticia"] = noticia
    return render(request, "Posts/detalle.html", contexto)
