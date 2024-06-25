from django.shortcuts import render
from datetime import date, datetime
from django.shortcuts import get_object_or_404, redirect
from .forms import  UserForm,ProductoForm,UpdProductoForm
from django.contrib import messages
from os import remove, path
from django.conf import settings
from django.contrib.auth import logout
from django.contrib.auth.models import User
from .models import Producto

def admin_page(request):
    return render(request, 'crud/administrador.html')

def carro(request):
    return render(request, 'crud/carro.html')

def flores(request):
    return render(request, 'crud/flores.html')

def base(request):
    return render(request, 'crud/base.html')

def listaprod(request):
    return render(request, 'crud/listaprod.html')

def maceteros(request):
    return render(request, 'crud/maceteros.html')

def nuevopd(request):
    return render(request, 'crud/nuevopd.html')

def nuevousuario(request):
    return render(request, 'crud/nuevousuario.html')

def pedidosad(request):
    return render(request, 'crud/pedidosad.html')

def pedidoscli(request):
    return render(request, 'crud/pedidoscli.html')

def recuperar(request):
    return render(request, 'crud/recuperar.html')

def recuperardos(request):
    return render(request, 'crud/recuperardos.html')

def suculentas(request):
    return render(request, 'crud/suculentas.html')

def sustratos(request):
    return render(request, 'crud/sustratos.html')

def tierra(request):
    return render(request, 'crud/tierra.html')

def usuarios(request):
    return render(request, 'crud/usuarios.html')
def home(request):
    return render(request, 'crud/home.html')

def crearcuenta(request):
    form=UserForm()
    if request.method=="POST":
        form=UserForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(to="login")
    datos={
        "form":form
    }
    return render(request, 'registration/crearcuenta.html',datos)

def salir(request):
    logout(request)
    return redirect(to='home')

def producto(request):
    productos = Producto.objects.all()

    # Filtrar productos de flores
    productos_flores = productos.filter(tipo='flores')

    datos = {
        "productos_generales": productos,
        "productos_flores": productos_flores
    }

    if request.path == '/productos/':
        return render(request, 'crud/productos.html', datos)
    elif request.path == '/flores/':
        return render(request, 'crud/flores.html', datos)
    else:
        return render(request, 'error.html', {'message': 'Página no encontrada'})

def crearproducto(request):
    formulario=ProductoForm()
    if request.method=="POST":
        formulario=ProductoForm(request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            #from django.contrib import messages
            messages.set_level(request,messages.SUCCESS)
            messages.success(request, "Producto creado con exito!!!")
            return redirect(to="productos")
        
    datos={
        "formulario":formulario
    }
    return render(request,'crud/crearproducto.html', datos)

def detalles_producto(request, id):
    #persona=Persona.objects.get(rut=id)
    producto=get_object_or_404(Producto,codigo_producto=id)
    datos={
        "producto":producto
    }
    return render(request,'crud/detalles_producto.html',datos)

def modificarproducto(request,id):
    producto=get_object_or_404(Producto, codigo_producto=id)
    form=UpdProductoForm(instance=producto)
    if request.method=="POST":
         form=UpdProductoForm(request.POST, files=request.FILES, instance=producto)
         if form.is_valid():
             form.save()
             messages.set_level(request,messages.WARNING)
             messages.warning(request,"Producto modificado")
             return redirect(to="productos")
    datos={
        'producto':producto,
        'form':form
    }
    return render(request,'crud/modificarproducto.html',datos)