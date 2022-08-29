from django.shortcuts import render, get_object_or_404
from .models import Producto, Proveedores, Comunidad
from .forms import formArchivos, formComunidad
from django.contrib import messages

# Create your views here.

def Inicio(request):
    return render(request, 'principal/index.html')


def Productos(request):
    productos= Producto.objects.all
    return render(request, 'principal/productos.html', {"productos": productos})


def Proveedor(request):
    if request.method== 'POST':
        form = formArchivos(request.POST, request.FILES)
        if form.is_valid():
            nombre= request.POST['nombre']
            mensaje= request.POST['mensaje']
            archivo= request.FILES['archivo']
            insert= Proveedores(nombre=nombre, mensaje=mensaje, archivo=archivo)
            insert.save()
            return render(request, "principal/proveedores.html")
        else:
            messages.error(request, "Error al mandar sugerencias")
    else:
        return render(request, 'principal/proveedores.html')


def comunidad(request):
    if request.method== 'POST':
        form= formComunidad(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'principal/comunidad.html')
    form = formComunidad()
    return render(request, 'principal/comunidad.html', {'form': form})


def Tabla(request):
    comunidad= Comunidad.objects.all()
    return render(request, 'principal/tabla.html', {'comunidad': comunidad})


def consultaTabla(request, id):
    comunidad= Comunidad.objects.get(id=id)
    return render(request, 'principal/editComunidad.html', {'comunidad': comunidad})

def editComunidad(request,id):
    comentario= get_object_or_404(Comunidad, id=id)
    form = formComunidad(request.POST, instance=comentario)
    if form.is_valid():
        form.save()
        comunidad= Comunidad.objects.all()
        return render(request, 'principal/tabla.html', {'comunidad': comunidad})
    
    return render(request, 'principal/editComunidad.html', {'comentario': comentario})


def eliminar(request, id, confirmacion='principal/deleteComunidad.html'):
    comentario= get_object_or_404(Comunidad, id=id)
    if request.method== 'POST':
        comentario.delete()
        comunidad=Comunidad.objects.all()
        return render(request, 'principal/tabla.html', {'comunidad': comunidad})

    return render(request, confirmacion, {'object': comentario})
