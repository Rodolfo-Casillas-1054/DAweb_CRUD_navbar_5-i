from django.db import models

# Create your views here.

class Marcos(models.Model):
    id_marcos=models.CharField(primary_key=True, max_length=6)
    medidas=models.CharField(max_length=100)
    material=models.CharField(max_length=100)
    diseno=models.CharField(max_length=100)
    precio=models.CharField(max_length=1000)
    tiempo=models.CharField(max_length=100)

    def __str__(self):
        return self.nombre