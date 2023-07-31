from django.shortcuts import render
from .froms import *
from .models import maquinaria,Implementos,Suplementos
from django.http import HttpResponse

# Create your views here.

def inicio(request):
    return render(request,'aplicacion/inicio.html')

def maquinas(request):
    MAQUINAS=maquinaria.objects.all()
    return render(request,'aplicacion/maquinaria.html',{'machines':MAQUINAS})

def implementos(request):
    IMPLEMENTOS=Implementos.objects.all()
    return render(request,'aplicacion/implementos.html',{'implements':IMPLEMENTOS})

def suplementos(request):
    SUPLEMENTOS=Suplementos.objects.all()
    return render(request,'aplicacion/suplementos.html',{'supplements':SUPLEMENTOS})

def crearobjeto2(request):
    return render(request,'aplicacion/crearobjeto2.html')

def crearobjeto(request):
    if request.method=='POST':
        form=formulario(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            if info['tipo'] == '1':
                nuevo_objeto = maquinaria(nombre=info['nombre'], precio=info['precio'])
                nuevo_objeto.save()
            elif info['tipo'] == '2':
                nuevo_objeto = Implementos(nombre=info['nombre'], precio=info['precio'])
                nuevo_objeto.save()
            elif info['tipo'] == '3':
                nuevo_objeto = Suplementos(nombre=info['nombre'], precio=info['precio'])
                nuevo_objeto.save()
            return HttpResponse('El objeto se grabó con éxito')
    else:
     form=formulario()             
    return render(request,'aplicacion/formulario.html',{'forms':form})

def buscarobjeto(request):
    fbuscar=Buscarobjeto()
    return render(request,'aplicacion/buscarobjeto.html',{'buscar':fbuscar})

def encontrarobjeto(request):
    if request.method == 'POST':
        form = Buscarobjeto(request.POST)
        if form.is_valid():
            tipo = form.cleaned_data['tipo']
            nombre = form.cleaned_data['nombre']
            resultados = None

            if tipo == '1':
                resultados = maquinaria.objects.filter(nombre__icontains=nombre)
            elif tipo == '2':
                resultados = Implementos.objects.filter(nombre__icontains=nombre)
            elif tipo == '3':
                resultados = Suplementos.objects.filter(nombre__icontains=nombre)    
            return render(request, 'aplicacion/resultados.html', {'resultados': resultados})
    else:
        form = Buscarobjeto()

    return render(request, 'aplicacion/buscarobjeto.html', {'buscar': form})
