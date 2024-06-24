from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import (
    admin_page, carro, flores, base, listaprod, maceteros, nuevopd,
    nuevousuario, pedidosad, pedidoscli, recuperar, recuperardos,
    suculentas, sustratos, tierra, usuarios, home, crearcuenta, salir, producto
)

urlpatterns = [
    path('administrador/', admin_page, name='admin_page'), 
    path('carro/', carro, name='carro'),
    path('flores/', flores, name='flores'),
    path('base/', base, name='base'),
    path('', home, name='home'),
    path('listaprod/', listaprod, name='listaprod'),
    path('maceteros/', maceteros, name='maceteros'),
    path('nuevopd/', nuevopd, name='nuevopd'),
    path('nuevousuario/', nuevousuario, name='nuevousuario'),
    path('pedidosad/', pedidosad, name='pedidosad'),
    path('pedidoscli/', pedidoscli, name='pedidoscli'),
    path('recuperar/', recuperar, name='recuperar'),
    path('recuperardos/', recuperardos, name='recuperardos'),
    path('crearcuenta/', crearcuenta, name='crearcuenta'),
    path('suculentas/', suculentas, name='suculentas'),
    path('sustratos/', sustratos, name='sustratos'),
    path('tierra/', tierra, name='tierra'),
    path('usuarios/', usuarios, name='usuarios'),
    path('salir/',salir,name='salir'),
    path('productos/',producto, name='producto')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
