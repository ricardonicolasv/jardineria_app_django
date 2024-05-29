from django.shortcuts import render

def acceder(request):
    return render(request, 'acceder.html')

def admin_page(request):
    return render(request, 'admin.html')

def carro(request):
    return render(request, 'carro.html')

def flores(request):
    return render(request, 'flores.html')

def florescli(request):
    return render(request, 'florescli.html')

def base(request):
    return render(request, 'base.html')

def indexcliente(request):
    return render(request, 'indexcliente.html')

def listaprod(request):
    return render(request, 'listaprod.html')

def maceteros(request):
    return render(request, 'maceteros.html')

def maceteroscli(request):
    return render(request, 'maceteroscli.html')

def nuevopd(request):
    return render(request, 'nuevopd.html')

def nuevousuario(request):
    return render(request, 'nuevousuario.html')

def pedidosad(request):
    return render(request, 'pedidosad.html')

def pedidoscli(request):
    return render(request, 'pedidoscli.html')

def recuperar(request):
    return render(request, 'recuperar.html')

def recuperardos(request):
    return render(request, 'recuperardos.html')

def registro(request):
    return render(request, 'registro.html')

def suculentas(request):
    return render(request, 'suculentas.html')

def suculentascli(request):
    return render(request, 'suculentascli.html')

def sustratos(request):
    return render(request, 'sustratos.html')

def sustratoscli(request):
    return render(request, 'sustratoscli.html')

def tierra(request):
    return render(request, 'tierra.html')

def tierradli(request):
    return render(request, 'tierradli.html')

def usuarios(request):
    return render(request, 'usuarios.html')
def home(request):
    return render(request, 'home.html')