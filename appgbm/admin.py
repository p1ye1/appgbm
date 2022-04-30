from xmlrpc.server import list_public_methods
from django.contrib import admin
from .models import Contacto_footer, Planes, Comentarios_inicio, Usuarios_register

# Register your models here.
#Vamos a registrar los modelos que hice en models.py
#Hay que importarlos primero

    ##Estas clases intervienen del área de administración lo personalizan
#class como_quieres_se_llame(admin.ModelAdmin):
#    list_display = ["","",""]
#    list_editable = [""]
#    search_fields = [""]
#    list_fields = ["",""]
#    list_filter = [""]
#    list_per_page = 10

class descrip_planes(admin.ModelAdmin):
    list_display = ["titulo","descripcion"]
#    list_editable = [""]
#    search_fields = [""]
#    list_fields = ["",""]
#    list_filter = [""]
#    list_per_page = 10

class descrip_coment(admin.ModelAdmin):
    list_display = ["persona","comentario"]


admin.site.register(Planes,descrip_planes)
admin.site.register(Contacto_footer)
admin.site.register(Comentarios_inicio)
admin.site.register(Usuarios_register)