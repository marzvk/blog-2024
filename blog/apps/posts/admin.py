from django.contrib import admin
from .models import Categorias, Posts, User

# Register your models here.

class PostsAdmin(admin.ModelAdmin):
    search_fields = ("titulo",)
    list_filter = ["categoria", "autor__username"]# accede a fk, desde la tabla autor a la otra tabla
    list_display = ['titulo', 'autor', 'categoria']
    date_hierarchy = 'fecha_publicacion' 


admin.site.register(Categorias) # cargamos los modelos para que django los lea
admin.site.register(Posts, PostsAdmin)
admin.site.register(User)