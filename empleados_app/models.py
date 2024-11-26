from django.db import models

# Create your views here.

class Empleados(models.Model):
    id_empleados=models.CharField(primary_key=True, max_length=6)
    nombre=models.CharField(max_length=100)
    apellido=models.CharField(max_length=100)
    fechanacimientpo=models.DateField(max_length=100)
    horario=models.CharField(max_length=1000)
    sueldo=models.CharField(max_length=100)
    numerotelefonico=models.CharField(max_length=100)

    def __str__(self):
        return self.nombre