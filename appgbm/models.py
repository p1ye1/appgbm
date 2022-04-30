from distutils.command.upload import upload
from tabnanny import verbose
from django.db import models
import datetime

# Create your models here.
# ¿Pará que sirve un modelo en Django?
# Tipos de clases para ayudar a construir una DB

# ¿Comó quieres que guarde los datos?
#descripcion = models.TextField(blank=False, null=False)
#descripcion_corta = models.CharField(max_length=100, blank=False, null=False)
#fecha_creacion = models.DateField(default=datetime.date.today, blank=False, null=False) #Datetime
#email = models.EmailField()
#disponible = models.BooleanField(default=True)
#cantidad = models.IntegerField(null=False, default=100)
#enlaces = models.URLField(blank=False, null=False)
#video = models.FileField(upload_to="videos")
#imagen_todo_tipo = models.ImageField(null=True, upload_to='carpeta donde se va a guardar')

## def __str__(self): #Nos dice que va a ser el elemento principal del modelo.

    ###COMANDOS NUEVOS###
    #MOTIVO: Como ya se hicieron modelos se debe hacer este nuevo proceso de activación.
    #python manage.py makemigrations
    #python magane.py migrate
    #python manage.py runserver
    #python manage.py createsuperuser

#Comando para installar PILLOW que es necesario par este caso
#python -m pip install pillow

class Planes(models.Model):
    icono = models.ImageField(null=True, upload_to='img_planes')
    titulo = models.CharField(max_length=100, blank=False, null=False)
    descripcion = models.TextField(blank=False, null=False, default="Ups tenemos un problema")
    
    class Meta:
        verbose_name = ("Plan")
        verbose_name_plural = ("Planes")
        
    def __str__(self):
        return self.titulo

class Contacto_footer(models.Model):
    cuenta = models.TextField(max_length=80, blank=False, null=False)
    correo_e = models.EmailField(max_length=80, blank=False, null=False)
    class Meta:
        verbose_name = ("Cuenta")
        verbose_name_plural = ("Cuentas")
    def __str__(self):
        return self.cuenta

class Comentarios_inicio(models.Model):
    persona = models.CharField(max_length=80, blank=False, null=False)
    comentario = models.TextField(max_length=280, blank=False, null=False)
    class Meta:
        verbose_name = ("Comentario")
        verbose_name_plural = ("Comentarios")
    def __str__(self):
        return self.persona

class Usuarios_register(models.Model):
    nombre = models.CharField(max_length=80, blank=False, null=False)
    apellido = models.CharField(max_length=80, blank=False, null=False)
    usuario = models.CharField(max_length=80, blank=False, null=False)
    correo_e = models.EmailField(max_length=100, blank=False, null=False)
    contraseña = models.CharField(max_length=80, blank=False, null=False)
    class Meta:
        verbose_name = ("Usuario")
        verbose_name_plural = ("Usuarios")
    def __str__(self):
        return self.usuario