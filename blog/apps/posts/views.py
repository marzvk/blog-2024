from django.shortcuts import render, redirect
from django.views.generic import CreateView, DeleteView, UpdateView, ListView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from .models import Posts, User, Comentarios, Categorias
from .form import (
    RegistroForm,
    CrearForm,
    ModificarForm,
    ModificarComentarioForm,
    CustomLoginForm,
    )
from django.contrib.auth.views import LoginView


# Create your views here.

# vistas basadas en funciones

# def posts(request):
#     context = {}
#     noticias = Posts.objects.all().order_by("-id") # seleccionamos todos los objetos de posts
#     context['noticias'] = noticias
#     return render(request, "Posts/posts.html", context)

class Noticias(ListView):
    paginate_by = 2
    model = Posts
    template_name = "Posts/posts.html"
    

    def get_queryset(self):
        queryset = super().get_queryset()
        
        # fecha
        ordenar_por = self.request.GET.get("ordenar")
        print(ordenar_por)
        if ordenar_por == "fecha":
            queryset = queryset.order_by("-fecha_publicacion")

        # alfabeticamente
        elif ordenar_por == "alfabetico":
            queryset = queryset.order_by("-titulo")

        # por autor
        autor = self.request.GET.get("autor")
        if autor:
            queryset = queryset.filter(autor__username=autor)

        # por categorias
        categoria = self.request.GET.get("categoria")
        if categoria:
            queryset = queryset.filter(categoria__nombre=categoria)

        
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categorias"] = Categorias.objects.all()
        return context

def about_us(request):
    return render(request, "Posts/about_us.html")

def perfil(request, id):
    context = {}
    usuarios = User.objects.get(id=id)
    context['usuarios']= usuarios
    # print(usuarios)
    return render(request, "usuarios/perfil.html", context)

def post_id(request, id):
    contexto = {}
    noticia = Posts.objects.get(id=id)
    comentarios = Comentarios.objects.filter(post=noticia)
    contexto["noticia"] = noticia
    contexto["comentarios"] = comentarios
    return render(request, "Posts/detalle.html", contexto)


# vista basada en clase

class Registro(CreateView):
    form_class = RegistroForm
    success_url = reverse_lazy("noticias")
    template_name = "usuarios/registro.html"


class CrearPost(CreateView):
    form_class = CrearForm
    model = Posts
    template_name = "Posts/crear_post.html"
    success_url = reverse_lazy("noticias")


    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)



class EliminarPost(DeleteView):
    model = Posts
    success_url = reverse_lazy("noticias")
    template_name = "Posts/posts_confirm_delete.html"



class ModificarPost(UpdateView):
    model = Posts
    form_class = ModificarForm
    template_name = "Posts/modificar_post.html"
    success_url = reverse_lazy("noticias")


@login_required
def comentar_post(request):
    comentario = request.POST.get("comentario", None)
    user = request.user
    post = request.POST.get("id_noticia", None)
    get_post = Posts.objects.get(pk=post)
    coment = Comentarios.objects.create(autor=user, contenido=comentario, post=get_post)

    return redirect(reverse_lazy("detalle", kwargs={"id": post}))


class ModificarComentario(UpdateView):
    model = Comentarios
    form_class = ModificarComentarioForm
    template_name = "comentarios/modificar.html"
    success_url = reverse_lazy("noticias")


class EliminarComentario(DeleteView):
    model = Comentarios
    template_name = "comentarios/confirm_delete.html"
    success_url = reverse_lazy("noticias")

# views login
class CustomLoginView(LoginView):
    authentication_form = CustomLoginForm
