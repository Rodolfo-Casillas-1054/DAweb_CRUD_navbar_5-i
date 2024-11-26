from django.shortcuts import render, redirect
from .models import Sucursal

# Create your views here.

def Inicio_vistaSucursal(request):
    lassucursales=Sucursal.objects.all()
    return render(request, 'gestionarSucursal.html', {'missucursales' : lassucursales})

def RegistrarSucursal(request):
    id_sucursal=request.POST['txtid_sucursal']
    nombre=request.POST['txtnombre']
    direccion=request.POST['txtdireccion']
    aforo=request.POST['numaforo']
    numeroempleados=request.POST['numnumeroempleados']

    guardarsucursales=Sucursal.objects.create(id_sucursal=id_sucursal, nombre=nombre, direccion=direccion, aforo=aforo, numeroempleados=numeroempleados)
    return redirect ("sucursal")



def EditarSucursal(request):
    id_sucursal=request.POST['txtid_sucursal']
    nombre=request.POST['txtnombre']
    direccion=request.POST['txtdireccion']
    aforo=request.POST['numaforo']
    numeroempleados=request.POST['numnumeroempleados']

    sucursales=Sucursal.objects.get(id_sucursal=id_sucursal)
    sucursales.nombre=nombre
    sucursales.direccion=direccion
    sucursales.aforo=aforo
    sucursales.numeroempleados=numeroempleados
    sucursales.save()
    return redirect ("sucursal")

def SeleccionarSucursal(request,id_sucursal):
    sucursales=Sucursal.objects.get(id_sucursal=id_sucursal)
    return render(request,"EditarSucursal.html",{"missucursales":sucursales})

def BorrarSucursal(request,id_sucursal):
    sucursales=Sucursal.objects.get(id_sucursal=id_sucursal)
    sucursales.delete()
    return redirect("sucursal")