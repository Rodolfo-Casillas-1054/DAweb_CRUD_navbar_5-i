from django.db import models

# Create your views here.

class Sucursal(models.Model):
    id_sucursal=models.CharField(primary_key=True, max_length=6)
    nombre=models.CharField(max_length=100)
    direccion=models.CharField(max_length=100)
    aforo=models.CharField(max_length=1000)
    numeroempleados=models.CharField(max_length=1000)

    def __str__(self):
        return self.nombre