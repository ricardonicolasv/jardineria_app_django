#views.py
from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect
from .forms import  UserForm,ProductoForm,UpdProductoForm
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.models import User
from .models import Producto,Pedido
from .tipos import TIPO_PRODUCTO
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect


@login_required
def flores(request):
    productos_flores = Producto.objects.filter(tipo='FLORES')
    datos = {
        "productos_flores": productos_flores
    }
    return render(request, 'crud/flores.html', datos)
@login_required
def maceteros(request):
    productos_maceteros = Producto.objects.filter(tipo='MACETEROS')
    datos = {
        "productos_maceteros": productos_maceteros
    }
    return render(request, 'crud/maceteros.html', datos)
@login_required
def suculentas(request):
    productos_suculentas = Producto.objects.filter(tipo='SUCULENTAS')
    datos = {
        "productos_suculentas": productos_suculentas
    }
    return render(request, 'crud/suculentas.html', datos)
@login_required
def sustratos(request):
    productos_sustratos = Producto.objects.filter(tipo='SUSTRATOS')
    datos = {
        "productos_sustratos": productos_sustratos
    }
    return render(request, 'crud/sustratos.html', datos)
@login_required
def tierra(request):
    productos_tierras = Producto.objects.filter(tipo='TIERRA DE HOJA')
    datos = {
        "productos_tierras": productos_tierras
    }
    return render(request, 'crud/tierra.html', datos)
def producto (request):
    producto=Producto.objects.all()

    datos={
        "producto":producto
    }
    return render(request,'crud/productos.html', datos)

@login_required
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
@login_required
def detalles_producto(request, id):
    #persona=Persona.objects.get(rut=id)
    producto=get_object_or_404(Producto,codigo_producto=id)
    datos={
        "producto":producto
    }
    return render(request,'crud/detalles_producto.html',datos)
@login_required
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

@login_required
def carro(request, id):
    producto = get_object_or_404(Producto, codigo_producto=id)
    pedido, creado = Pedido.objects.get_or_create(usuario=request.user, producto=producto)
    if not creado:
        pedido.cantidad += 1
        pedido.save()
    messages.success(request, f"{producto.nombre_producto} ha sido añadido al carro.")
    
    # Redirigir a la página anterior
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

@login_required
def eliminar_del_carro(request, id):
    pedido = get_object_or_404(Pedido, id=id, usuario=request.user)
    pedido.delete()
    messages.success(request, 'Producto eliminado del carro.')
    return redirect('carro')

@login_required
def procesar_pago(request):
    # Lógica para procesar el pago
    messages.success(request, 'Pago procesado correctamente.')
    return redirect('carro')

@login_required
def vaciar_carro(request):
    Pedido.objects.filter(usuario=request.user).delete()
    messages.success(request, 'Carro vaciado correctamente.')
    return redirect('carro')

@login_required
def agregar_al_carro(request, codigo_producto):
    producto = get_object_or_404(Producto, codigo_producto=codigo_producto)
    pedido, created = Pedido.objects.get_or_create(usuario=request.user, producto=producto)
    if not created:
        pedido.cantidad += 1
        pedido.save()
    messages.success(request, 'Producto agregado al carro.')
    return redirect('carro')

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


def admin_page(request):
    return render(request, 'crud/administrador.html')

def carro(request):
    return render(request, 'crud/carro.html')

def base(request):
    return render(request, 'crud/base.html')

def listaprod(request):
    return render(request, 'crud/listaprod.html')

def nuevopd(request):
    return render(request, 'crud/nuevopd.html')

def nuevousuario(request):
    return render(request, 'crud/nuevousuario.html')

def pedidosad(request):
    return render(request, 'crud/pedidosad.html')

def pedido(request):
    return render(request, 'crud/pedidoscli.html')

def recuperar(request):
    return render(request, 'crud/recuperar.html')

def recuperardos(request):
    return render(request, 'crud/recuperardos.html')

def usuarios(request):
    return render(request, 'crud/usuarios.html')
def home(request):
    return render(request, 'crud/home.html')