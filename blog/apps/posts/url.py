from django.urls import path
from . import views


urlpatterns = [
    path("",views.posts, name="noticias"),
    path("about/", views.about_us, name="about"),
    path("registro/", views.Registro.as_view(), name="registro"),
    path("detalle/<int:id>", views.post_id, name="detalle"),
    path("perfil/<int:id>", views.perfil, name="perfil"),
]