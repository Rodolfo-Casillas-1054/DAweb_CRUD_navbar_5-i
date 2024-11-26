from django.urls import path
from sucursal_app import views

urlpatterns = [
    path('sucursal', views.Inicio_vistaSucursal, name='sucursal'),
    path('RegistrarSucursal/' ,views.RegistrarSucursal, name='RegistrarSucursal' ),
    path("SeleccionarSucursal/<id_sucursal>",views.SeleccionarSucursal,name="SeleccionarSucursal"),
    path("EditarSucursal/",views.EditarSucursal,name="EditarSucursal"),
    path("BorrarSucursal/<id_sucursal>",views.BorrarSucursal,name="BorrarSucursal")
]