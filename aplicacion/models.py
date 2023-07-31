from django.db import models

# Create your models here.

class maquinaria(models.Model):
    nombre=models.CharField(max_length=20)
    precio=models.DecimalField(max_digits=6,decimal_places=3)

class Implementos(models.Model):
    nombre=models.CharField(max_length=20)
    precio=models.DecimalField(max_digits=6,decimal_places=3)

class Suplementos(models.Model):
    nombre=models.CharField(max_length=20)
    precio=models.DecimalField(max_digits=6,decimal_places=3)