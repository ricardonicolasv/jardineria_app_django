from django.contrib import admin
from django.urls import path
from jardineria_app import views  # Asegúrate de que 'myapp' sea el nombre correcto de tu aplicación

urlpatterns = [
    path('admin/', admin.site.urls),
    path('acceder/', views.acceder, name='acceder'),
    path('admin_page/', views.admin_page, name='admin_page'),  # 'admin' is a reserved name, so using 'admin_page'
    path('carro/', views.carro, name='carro'),
    path('flores/', views.flores, name='flores'),
    path('florescli/', views.florescli, name='florescli'),
    path('base/', views.base, name='base'),
    path('', views.home, name='home'),
    path('indexcliente/', views.indexcliente, name='indexcliente'),
    path('listaprod/', views.listaprod, name='listaprod'),
    path('maceteros/', views.maceteros, name='maceteros'),
    path('maceteroscli/', views.maceteroscli, name='maceteroscli'),
    path('nuevopd/', views.nuevopd, name='nuevopd'),
    path('nuevousuario/', views.nuevousuario, name='nuevousuario'),
    path('pedidosad/', views.pedidosad, name='pedidosad'),
    path('pedidoscli/', views.pedidoscli, name='pedidoscli'),
    path('recuperar/', views.recuperar, name='recuperar'),
    path('recuperardos/', views.recuperardos, name='recuperardos'),
    path('registro/', views.registro, name='registro'),
    path('suculentas/', views.suculentas, name='suculentas'),
    path('suculentascli/', views.suculentascli, name='suculentascli'),
    path('sustratos/', views.sustratos, name='sustratos'),
    path('sustratoscli/', views.sustratoscli, name='sustratoscli'),
    path('tierra/', views.tierra, name='tierra'),
    path('tierradli/', views.tierradli, name='tierradli'),
    path('usuarios/', views.usuarios, name='usuarios'),
]
