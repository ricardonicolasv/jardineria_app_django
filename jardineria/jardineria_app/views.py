#views.py
from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect
from django.views import View
from .forms import  UserForm,ProductoForm,UpdProductoForm
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.models import User
from .models import Producto,Pedido
from .tipos import TIPO_PRODUCTO
from django.contrib.auth.decorators import login_required, permission_required
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
### FUNCIONES DE PRODUCTOS-------------------------############################################################
def producto (request):
    producto=Producto.objects.all()

    datos={
        "producto":producto
    }
    return render(request,'crud/productos.html', datos)

@permission_required('jardineria.add_producto')
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
@permission_required('jardineria.change_producto')
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
### FUNCIONES DE PEDIDO-------------------------############################################################
@login_required
def agregar_a_pedido(request, producto_id):
    producto = get_object_or_404(Producto, pk=producto_id)
    usuario = request.user
    cantidad = 1  # Aquí puedes adaptar la lógica para obtener la cantidad deseada

    pedido, created = Pedido.objects.get_or_create(usuario=usuario, producto=producto, defaults={'cantidad': cantidad})
    if not created:
        pedido.cantidad += 1
        pedido.save()

    messages.success(request, f"{producto.nombre_producto} ha sido agregado a tu pedido!")
    return redirect('pedidoscli')  # Redirigir a la vista de pedidos del cliente
@login_required
def pedidoscli(request):
    pedidos = Pedido.objects.filter(usuario=request.user)
    
    total_pedido = sum(pedido.producto.precio * pedido.cantidad for pedido in pedidos)
    
    context = {
        'pedidos': pedidos,
        'total_pedido': total_pedido,
    }
    
    return render(request, 'crud/pedidoscli.html', context)

@login_required
def actualizar_cantidad(request, pedido_id):
    pedido = get_object_or_404(Pedido, pk=pedido_id, usuario=request.user)
    if request.method == "POST":
        nueva_cantidad = int(request.POST.get('cantidad'))
        if nueva_cantidad > 0 and nueva_cantidad <= pedido.producto.cantidad:
            pedido.cantidad = nueva_cantidad
            pedido.save()
            messages.success(request, "Cantidad actualizada correctamente.")
        else:
            messages.error(request, "Cantidad inválida.")
    return redirect('pedidoscli')

@login_required
def eliminar_pedido(request, pedido_id):
    pedido = get_object_or_404(Pedido, pk=pedido_id, usuario=request.user)
    if request.method == "POST":
        pedido.delete()
        messages.success(request, "Producto eliminado del pedido.")
    return redirect('pedidoscli')

### FUNCIONES DE USUARIO-------------------------############################################################
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

def pedido(request):
    return render(request, 'crud/pedidoscli.html')

def home(request):
    return render(request, 'crud/home.html')
