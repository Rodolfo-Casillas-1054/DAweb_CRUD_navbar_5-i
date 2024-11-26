from django.urls import path
from app_base import views

urlpatterns = [
    #Inicio enmarcadería
    path('', views.Inicio),
]
