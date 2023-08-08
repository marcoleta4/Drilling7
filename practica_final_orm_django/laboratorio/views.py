from django.shortcuts import render, redirect
from .models import Laboratorio


def lista_laboratorios(request):
    laboratorios = Laboratorio.objects.all()
    return render(request, 'laboratorios/lista.html', {'laboratorios': laboratorios})


def crear_laboratorio(request):
  if request.method == 'POST':
    nombre = request.POST['nombre']
    laboratorio = Laboratorio(nombre=nombre)
    laboratorio.save()
    return redirect('lista_laboratorios')
  return render(request, 'laboratorios/crear.html') 

def editar_laboratorio(request, id):
  laboratorio = Laboratorio.objects.get(id=id)
  if request.method == 'POST':
    laboratorio.nombre = request.POST['nombre']
    laboratorio.save()
    return redirect('lista_laboratorios')
  return render(request, 'laboratorios/editar.html', {'laboratorio': laboratorio})  

def eliminar_laboratorio(request, id):
  laboratorio = Laboratorio.objects.get(id=id)
  laboratorio.delete()
  return redirect('lista_laboratorios')