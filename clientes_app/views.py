from django.shortcuts import render, redirect
from .models import Materia

# Create your views here.

def Inicio_vistaCliente(request):
    lasmaterias=Materia.objects.all()
    return render(request, 'gestionarMateria.html', {'mismaterias' : lasmaterias})

def RegistrarCliente(request):
    id_cliente=request.POST['txtid_cliente']
    nombre=request.POST['txtnombre']
    apellido=request.POST['txtapellido']
    edad=request.POST['numedad']
    telefono=request.POST['numtelefono']

    guardarmaterias=Materia.objects.create(id_cliente=id_cliente, nombre=nombre, apellido=apellido, edad=edad, telefono=telefono)
    return redirect ("cliente")



def EditarCliente(request):
    id_cliente=request.POST['txtid_cliente']
    nombre=request.POST['txtnombre']
    apellido=request.POST['txtapellido']
    edad=request.POST['numedad']
    telefono=request.POST['numtelefono']

    cliente=Materia.objects.get(id_cliente=id_cliente)
    cliente.nombre=nombre
    cliente.apellido=apellido
    cliente.edad=edad
    cliente.telefono=telefono
    cliente.save()
    return redirect ("cliente")

def SeleccionarCliente(request,id_cliente):
    cliente=Materia.objects.get(id_cliente=id_cliente)
    return render(request,"EditarMateria.html",{"mismaterias":cliente})

def BorrarCliente(request,id_cliente):
    cliente=Materia.objects.get(id_cliente=id_cliente)
    cliente.delete()
    return redirect("cliente")