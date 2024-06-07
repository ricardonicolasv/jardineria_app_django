from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from .tipos import *

class Producto (models.Model):
    codigo_producto=models.CharField(max_length=50,primary_key=True)
    nombre_producto=models.CharField(max_length=50, null=False)
    cantidad=models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(250)])
    tipo=models.CharField(max_length=25, choices=TIPO_PRODUCTO)
    precio=models.IntegerField(validators=[MinValueValidator(1000),MaxValueValidator(10000000)])
    imagen=models.ImageField(upload_to='producto', null=True)
    def __str__(self):
        return f"{self.codigo_producto} - {self.nombre_producto} {self.cantidad} {self.tipo}"