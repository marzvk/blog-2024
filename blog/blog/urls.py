"""
URL configuration for blog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.contrib.auth.views import  LogoutView
from apps.posts.views import CustomLoginView
from .configuraciones import settings
from .views import index



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    # las url de la app posts
    path("posts/", include("apps.posts.url")),
    # aqui para incluir otras apps
    #  path(
    #     "login/", LoginView.as_view(template_name="usuarios/login.html"), name="login"
    # ),
    path("login/",
        CustomLoginView.as_view(template_name="usuarios/login.html"),
        name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT) # lectura de imagenes y ruta
