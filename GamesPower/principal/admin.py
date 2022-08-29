from django.contrib import admin
from .models import Producto, Proveedores, Comunidad

# Register your models here.

class adminProducto(admin.ModelAdmin):
    list_display= ('nombre', 'categoria', 'existencia')
    search_fields= ('nombre', 'categoria')
    list_filter= ('nombre', 'categoria')
    date_hierarchy= 'created'
    
class adminProveedores(admin.ModelAdmin):
    list_display= ('nombre', 'mensaje', 'archivo')
    search_fields= ('nombre',)
    list_filter= ('nombre', 'mensaje')
    date_hierarchy= 'creacion'

class adminComunidad(admin.ModelAdmin):
    list_display= ('nombre', 'producto', 'mensaje')
    search_fields= ('nombre', 'producto')
    date_hierarchy= 'creacion'

admin.site.site_header = 'GamerPower'
admin.site.index_title = 'Panel de control de GamesPower'
admin.site.site_title = 'Panel de control'

admin.site.register(Producto, adminProducto)

admin.site.register(Proveedores, adminProveedores)

admin.site.register(Comunidad, adminComunidad)