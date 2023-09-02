from django.contrib import admin
from .models import Orden, ItemOrden

# Register your models here.

class OrdenItemInLine(admin.TabularInline):
    model = ItemOrden
    campos_id = ['producto']

@admin.register(Orden)
class OrdenAdmin(admin.ModelAdmin):
    lista_despl = ['id', 'nombre', 'primer_apellido',
                   'segundo_apellido', 'correo', 'direccion',
                   'codigo_postal', 'ciudad', 'pagado',
                   'creado', 'actualizado']
    lista_filtro = ['pagado', 'creado', 'actualizado']
    inlines = [OrdenItemInLine]