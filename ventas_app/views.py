from django.shortcuts import render, redirect
from .models import Ventas

# Create your views here.

def Inicio_vistaVentas(request):
    lasventas=Ventas.objects.all()
    return render(request, 'gestionarVentas.html', {'misventas' : lasventas})

def RegistrarVentas(request):
    id_ventas = request.POST['txtid_ventas']
    id_proveedores = request.POST['txtproveedor']
    id_cliente = request.POST['txtcliente']
    id_empleado = request.POST['txtempleado']
    cantidad = request.POST['txtcantidad']
    precioventas = request.POST['txtprecioventas']
    fechaventas = request.POST['txtfechaventas']
    metodopago = request.POST['txtmetodopago']


    guardarventas=Ventas.objects.create(id_ventas=id_ventas, id_proveedores=id_proveedores, id_cliente=id_cliente, id_empleado=id_empleado, cantidad=cantidad, precioventas=precioventas, fechaventas=fechaventas, metodopago=metodopago)
    return redirect ("ventas")



def EditarVentas(request):
    id_ventas = request.POST['txtid_ventas']
    id_proveedores = request.POST['txtproveedor']
    id_cliente = request.POST['txtcliente']
    id_empleado = request.POST['txtempleado']
    cantidad = request.POST['txtcantidad']
    precioventas = request.POST['txtprecioventas']
    fechaventas = request.POST['txtfechaventas']
    metodopago = request.POST['txtmetodopago']

    ventas=Ventas.objects.get(id_ventas=id_ventas)
    ventas.id_proveedores=id_proveedores
    ventas.id_cliente=id_cliente
    ventas.id_empleado=id_empleado
    ventas.cantidad=cantidad
    ventas.precioventas=precioventas
    ventas.fechaventas=fechaventas
    ventas.metodopago=metodopago
    ventas.save()
    return redirect ("ventas")

def SeleccionarVentas(request,id_ventas):
    ventas=Ventas.objects.get(id_ventas=id_ventas)
    return render(request,"EditarVentas.html",{"misventas":ventas})

def BorrarVentas(request,id_ventas):
    ventas=Ventas.objects.get(id_ventas=id_ventas)
    ventas.delete()
    return redirect("ventas")