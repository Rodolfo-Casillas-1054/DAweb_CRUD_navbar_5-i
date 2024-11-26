from django.urls import path
from clientes_app import views

urlpatterns = [
    path('cliente', views.Inicio_vistaCliente, name='cliente'),
    path('RegistrarCliente/' ,views.RegistrarCliente, name='RegistrarCliente' ),
    path("SeleccionarCliente/<id_cliente>",views.SeleccionarCliente,name="SeleccionarCliente"),
    path("EditarCliente/",views.EditarCliente,name="EditarCliente"),
    path("BorrarCliente/<id_cliente>",views.BorrarCliente,name="BorrarCliente")
]