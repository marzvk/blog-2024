from django.urls import path
from . import views


urlpatterns = [
    path("",views.posts, name="noticias"),
    path("about/", views.about_us, name="about"),
    path("registro/", views.Registro.as_view(), name="registro"),
    path("detalle/<int:id>", views.post_id, name="detalle"),
    # perfil usuario
    path("perfil/<int:id>", views.perfil, name="perfil"),
    # crear nuevo post
    path("nuevo_post/", views.CrearPost.as_view(), name="nuevo_post"),
    # eliminar
    path("eliminar/<int:pk>", views.EliminarPost.as_view(), name="eliminar_post"),
]