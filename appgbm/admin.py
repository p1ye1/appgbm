from xmlrpc.server import list_public_methods
from django.contrib import admin
from .models import Contacto_footer, Planes, Smart_cash, Wealth_management

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


admin.site.register(Planes,descrip_planes)
admin.site.register(Smart_cash)
admin.site.register(Wealth_management)
admin.site.register(Contacto_footer)