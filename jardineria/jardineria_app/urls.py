#urls.py
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import (
    carro, eliminar_del_carro, procesar_pago, vaciar_carro, agregar_al_carro,
    flores, base, maceteros, pedido, suculentas, sustratos, tierra, home,
    crearcuenta, salir, producto, crearproducto, detalles_producto, modificarproducto
)

urlpatterns = [
    path('carro/', carro, name='carro'),
    path('carro/agregar/<str:codigo_producto>/', agregar_al_carro, name='agregar_al_carro'),
    path('carro/eliminar/<int:id>/', eliminar_del_carro, name='eliminar_del_carro'),
    path('carro/procesar_pago/', procesar_pago, name='procesar_pago'),
    path('carro/vaciar/', vaciar_carro, name='vaciar_carro'),
    path('flores/', flores, name='flores'),
    path('base/', base, name='base'),
    path('', home, name='home'),
    path('maceteros/', maceteros, name='maceteros'),
    path('pedidoscli/', pedido, name='pedidoscli'),
    path('crearcuenta/', crearcuenta, name='crearcuenta'),
    path('suculentas/', suculentas, name='suculentas'),
    path('sustratos/', sustratos, name='sustratos'),
    path('tierra/', tierra, name='tierra'),
    path('salir/', salir, name='salir'),
    path('productos/', producto, name='productos'),
    path('detalles_producto/<id>', detalles_producto, name='detalles_producto'),
    path('modificarproducto/<id>', modificarproducto, name='modificarproducto'),
    path('crearproducto/', crearproducto, name='crearproducto'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)