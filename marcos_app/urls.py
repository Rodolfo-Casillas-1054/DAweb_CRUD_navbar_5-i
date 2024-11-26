from django.urls import path
from marcos_app import views

urlpatterns = [
    path('marcos', views.Inicio_vistaMarcos, name='marcos'),
    path('RegistrarMarcos/' ,views.RegistrarMarcos, name='RegistrarMarcos' ),
    path("SeleccionarMarcos/<id_marcos>",views.SeleccionarMarcos,name="SeleccionarMarcos"),
    path("EditarMarcos/",views.EditarMarcos,name="EditarMarcos"),
    path("BorrarMarcos/<id_marcos>",views.BorrarMarcos,name="BorrarMarcos")
]