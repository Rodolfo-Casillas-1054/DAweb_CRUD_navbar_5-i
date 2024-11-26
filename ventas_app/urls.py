from django.urls import path
from ventas_app import views

urlpatterns = [
    path('ventas', views.Inicio_vistaVentas, name='ventas'),
    path('RegistrarVentas/' ,views.RegistrarVentas, name='RegistrarVentas' ),
    path("SeleccionarVentas/<id_ventas>",views.SeleccionarVentas,name="SeleccionarVentas"),
    path("EditarVentas/",views.EditarVentas,name="EditarVentas"),
    path("BorrarVentas/<id_ventas>",views.BorrarVentas,name="BorrarVentas")
]