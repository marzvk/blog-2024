from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User, Posts, Comentarios


class RegistroForm(UserCreationForm):
    username = forms.CharField(
        max_length=200,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Nombre de usuario"},
        ),
    )
    email = forms.EmailField(
        max_length=200,
        help_text="Required",
        widget=forms.EmailInput(
            attrs={"class": "form-control", "placeholder": "name@example.com"}
        ),
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control"}), required=True
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control"}), required=True
    )
    icono = forms.ImageField(
        label="Imagen de perfil",
        required=False,
        widget=forms.FileInput(attrs={"class": "form-control form-control-lg"}),
    )

    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "password1",
            "password2",
            "icono",
        ]

class CrearForm(forms.ModelForm):
    
    class Meta:
        model = Posts
        fields = "__all__"
        exclude = ["autor"]



class ModificarForm(forms.ModelForm):

    class Meta:
        model = Posts
        fields = ("contenido",)


# Formulario Comentarios

class ComentarioForm(forms.ModelForm):

    class Meta:
        model = Comentarios
        fields = ["contenido",]


class ModificarComentarioForm(forms.ModelForm):

    class Meta:
        model = Comentarios
        fields = [
            "contenido",
        ]