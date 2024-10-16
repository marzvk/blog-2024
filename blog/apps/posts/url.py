from django.urls import path
from . import views

urlpatterns = [
    path("", views.posts, name="noticias"),
    path("about/", views.about_us, name="about"),
    path("registro/", views.Registro.as_view(), name="registro"),
    path("detalle/<int:id>", views.post_id, name="detalle"),
    # perfil usuario
    path("perfil/<int:id>", views.perfil, name="perfil"),
    # crear nuevo post
    path("nuevo_post/", views.CrearPost.as_view(), name="nuevo_post"),
    # eliminar
    path("eliminar/<int:pk>",
         views.EliminarPost.as_view(),
         name="eliminar_post"),
    # modificar
    path("modificar/<int:pk>",
         views.ModificarPost.as_view(),
         name="modificar_post"),
    # url de comentario
    path("comentar/", views.comentar_post, name="comentar"),
    # eliminar comentario
    path("borrar/<int:pk>",
         views.EliminarComentario.as_view(),
         name="borrar_comentario"),
    # url modificar el comentario
    path(
        "modificar_com/<int:pk>",
        views.ModificarComentario.as_view(),
        name="modificar_comentario",
    ),
]
