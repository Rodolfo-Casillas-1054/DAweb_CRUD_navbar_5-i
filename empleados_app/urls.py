from django.urls import path
from empleados_app import views

urlpatterns = [
    path('empleados', views.Inicio_vistaEmpleados, name='empleados'),
    path('RegistrarEmpleados/' ,views.RegistrarEmpleados, name='RegistrarEmpleados' ),
    path("SeleccionarEmpleados/<id_empleados>",views.SeleccionarEmpleados,name="SeleccionarEmpleados"),
    path("EditarEmpleados/",views.EditarEmpleados,name="EditarEmpleados"),
    path("BorrarEmpleados/<id_empleados>",views.BorrarEmpleados,name="BorrarEmpleados")
]