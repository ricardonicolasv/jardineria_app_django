from django.contrib import admin
from .models import *
from .forms import ProductoForm, User

# Register your models here.
class AdmProducto(admin.ModelAdmin):
        list_display=['codigo_producto','nombre_producto','cantidad','tipo','precio','imagen']
        list_editable=['nombre_producto','cantidad','tipo','precio','imagen']
        list_filter=['cantidad','tipo','precio']
        form = ProductoForm

class AdmUser(admin.ModelAdmin):
        filter_horizontal = ('groups', 'user_permissions')

admin.site.register(Producto, AdmProducto)
admin.site.register(User, AdmUser)