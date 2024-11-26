from django.shortcuts import render, redirect
from .models import Empleados

# Create your views here.

def Inicio_vistaEmpleados(request):
    losempleados=Empleados.objects.all()
    return render(request, 'gestionarEmpleados.html', {'misempleados' : losempleados})

def RegistrarEmpleados(request):
    id_empleados=request.POST['txtid_empleados']
    nombre=request.POST['txtnombre']
    apellido=request.POST['txtapellido']
    fechanacimientpo=request.POST['numfechanacimientpo']
    horario=request.POST['txthorario']
    sueldo=request.POST['numsueldo']
    numerotelefonico=request.POST['numtele']

    guardarempleados=Empleados.objects.create(id_empleados=id_empleados, nombre=nombre, apellido=apellido, fechanacimientpo=fechanacimientpo, horario=horario, sueldo=sueldo, numerotelefonico=numerotelefonico)
    return redirect ("empleados")



def EditarEmpleados(request):
    id_empleados=request.POST['txtid_empleados']
    nombre=request.POST['txtnombre']
    apellido=request.POST['txtapellido']
    fechanacimientpo=request.POST['numfechanacimientpo']
    horario=request.POST['txthorario']
    sueldo=request.POST['numsueldo']
    numerotelefonico=request.POST['numtele']

    empleados=Empleados.objects.get(id_empleados=id_empleados)
    empleados.nombre=nombre
    empleados.apellido=apellido
    empleados.fechanacimientpo=fechanacimientpo
    empleados.horario=horario
    empleados.sueldo=sueldo
    empleados.numerotelefonico=numerotelefonico
    empleados.save()
    return redirect ("empleados")

def SeleccionarEmpleados(request,id_empleados):
    empleados=Empleados.objects.get(id_empleados=id_empleados)
    return render(request,"EditarEmpleados.html",{"misempleados":empleados})

def BorrarEmpleados(request,id_empleados):
    empleados=Empleados.objects.get(id_empleados=id_empleados)
    empleados.delete()
    return redirect("empleados")