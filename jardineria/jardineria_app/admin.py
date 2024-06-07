from django.contrib import admin
from .models import *

# Register your models here.
class AdmProducto(admin.ModelAdmin):
        list_display=['codigo_producto','nombre_producto','cantidad','tipo','precio','imagen']
        list_editable=['nombre_producto','cantidad','tipo','precio','imagen']
        list_filter=['cantidad','tipo','precio']

admin.site.register(Producto, AdmProducto)
