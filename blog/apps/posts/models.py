from django.db import models
from django.contrib.auth.models import AbstractUser, User

# Create your models here.

# Creacion de usuarios con otros atributos


class User(AbstractUser):
    icono = models.ImageField(upload_to='media/usuarios',
                              null=True,
                              blank=True)
    descripcion = models.TextField(max_length=250)

    def __str__(self):
        return self.username  # username hereda de la clase a la que llama

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'


class Categorias(models.Model):  # nombreapp_luego_nombreclase
    nombre = models.CharField(max_length=90)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = "Categorias"  # nombre que sale en indice de db
        verbose_name = "Categoria"  # nombre que sale en el admin
        verbose_name_plural = "Categorias"


class Posts(models.Model):
    titulo = models.CharField(max_length=150,
                              null=False,
                              blank=False,
                              verbose_name="Titulo")
    contenido = models.TextField(verbose_name="Contenido")
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categorias, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='posts/', null=True, blank=True)

    class Meta:
        db_table = "Posts"
        verbose_name = "Post"
        verbose_name_plural = "Posts"

    def __str__(self):
        return self.titulo


class Comentarios(models.Model):
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    contenido = models.TextField(max_length=250, verbose_name='Contenido')
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Posts, on_delete=models.CASCADE)
