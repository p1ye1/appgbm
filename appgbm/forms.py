from asyncio import current_task
from dataclasses import field
from enum import auto
from pyexpat import model
from .models import Contacto_footer as cuenta, Comentarios_inicio as comenta, Usuarios_register as registro
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class PersonasForm(forms.ModelForm):
    class Meta:
     model = cuenta
     fields = ["cuenta","correo_e"]
     #fields = '__all__'  ###Sirve para mostrar todos los campos###

#Comentarios Form ABAJO⬇
class ComentaForm(forms.ModelForm):
    class Meta:
     model = comenta
     fields = ["persona","comentario"]
    
class RegisterForm(forms.ModelForm):
    class Meta:
        model = registro
        fields = ["nombre", "apellido", "usuario", "correo_e", "contraseña"]

class userForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password', 'password2']

class loginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'remember_me']
    username = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'placeholder': 'Username','class': 'form-control',}))
    password = forms.CharField(max_length=50, required=True, widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'class': 'form-control', 'data-toggle': 'password', 'id': 'password', 'name': 'password', }))
    remember_me = forms.BooleanField(required=False)

# Liberías de Crispy para Formularios con Bootstrap
# pip install django_crispy_forms
#python -m pip install django_crispy_forms

# 1.Se instala python -m pip install django_crispy_forms
# 2.Vamos a ssettings.py y agregamos en INSTALLED_APPS = ['crispy_forms',]
# Y también CRISPY_TEMPLATE_PACK = 'bootstrap4'
# 3.En la plantilla HTML pones los tabs de Crispy {% load crispy_froms_tags %} al principio
# 4.Aplicas en los formularios {{ form | crispy }}