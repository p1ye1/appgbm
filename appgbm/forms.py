from asyncio import current_task
from .models import Contacto_footer as cuenta
from django import forms

class PersonasForm(forms.ModelForm):
    class Meta:
     model = cuenta
     fields = ["cuenta","correo_e"]
     #fields = '__all__'  ###Sirve para mostrar todos los campos###

# Liberías de Crispy para Formularios con Bootstrap
# pip install django_crispy_forms
#python -m pip install django_crispy_forms

# 1.Se instala python -m pip install django_crispy_forms
# 2.Vamos a ssettings.py y agregamos en INSTALLED_APPS = ['crispy_forms',]
# Y también CRISPY_TEMPLATE_PACK = 'bootstrap4'
# 3.En la plantilla HTML pones los tabs de Crispy {% load crispy_froms_tags %} al principio
# 4.Aplicas en los formularios {{ form | crispy }}