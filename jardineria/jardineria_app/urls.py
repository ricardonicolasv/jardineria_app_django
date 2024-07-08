from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import (
    detalle_pedido, 
    flores, base, maceteros, pedido, suculentas, sustratos, tierra, home,seguimiento_pedido,ListadoUsuariosView,detalles_usuario,modificar_usuario,
    crearcuenta, salir, producto, crearproducto, detalles_producto, modificarproducto, agregar_a_pedido, pedidoscli, actualizar_cantidad, eliminar_pedido, 
)
urlpatterns = [
    path('usuarios/', ListadoUsuariosView.as_view(), name='listado_usuarios'),
    path('usuarios/detalles/<int:user_id>/', detalles_usuario, name='detalles_usuario'),
    path('usuarios/modificar/<int:user_id>/', modificar_usuario, name='modificar_usuario'),
    path('detalle_pedido/', detalle_pedido, name='detalle_pedido'),
    path('flores/', flores, name='flores'),
    path('base/', base, name='base'),
    path('', home, name='home'),
    path('maceteros/', maceteros, name='maceteros'),
    path('pedidoscli/', pedidoscli, name='pedidoscli'),
    path('crearcuenta/', crearcuenta, name='crearcuenta'),
    path('suculentas/', suculentas, name='suculentas'),
    path('sustratos/', sustratos, name='sustratos'),
    path('tierra/', tierra, name='tierra'),
    path('salir/', salir, name='salir'),
    path('productos/', producto, name='productos'),
    path('detalles_producto/<id>', detalles_producto, name='detalles_producto'),
    path('modificarproducto/<id>', modificarproducto, name='modificarproducto'),
    path('crearproducto/', crearproducto, name='crearproducto'),
    path('agregar_a_pedido/<str:producto_id>/', agregar_a_pedido, name='agregar_a_pedido'),
    path('actualizar_cantidad/<int:pedido_id>/', actualizar_cantidad, name='actualizar_cantidad'),
    path('eliminar_pedido/<int:pedido_id>/', eliminar_pedido, name='eliminar_pedido'),
    path('seguimiento_pedido/', seguimiento_pedido, name='seguimiento_pedido'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
