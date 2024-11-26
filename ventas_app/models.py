from django.db import models

# Create your views here.

class Ventas(models.Model):
    id_ventas=models.CharField(primary_key=True, max_length=6)
    id_proveedores=models.CharField(max_length=100)
    id_cliente=models.CharField(max_length=100)
    id_empleado=models.CharField(max_length=100)
    cantidad=models.CharField(max_length=1000)
    precioventas=models.CharField(max_length=100)
    fechaventas=models.DateField(max_length=100)
    metodopago=models.CharField(max_length=100)

    def __str__(self):
        return self.nombre