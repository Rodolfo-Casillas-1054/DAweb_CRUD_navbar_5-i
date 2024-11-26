from django.db import models

# Create your views here.

class Materia(models.Model):
    id_cliente=models.CharField(primary_key=True, max_length=6)
    nombre=models.CharField(max_length=100)
    apellido=models.CharField(max_length=100)
    edad=models.CharField(max_length=100)
    telefono=models.CharField(max_length=100)

    def __str__(self):
        return self.nombre