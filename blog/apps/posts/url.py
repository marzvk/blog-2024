from django.urls import path
from . import views


urlpatterns = [
    path("",views.posts, name="noticias"),
    path("about/", views.about_us, name="about"),
    path("registro/", views.registro, name="registro"),
]