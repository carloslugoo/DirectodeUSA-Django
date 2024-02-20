from django.db import models

# Create your models here.
class Producto(models.Model):
    dispositivo = models.CharField(max_length=255)
    almacenamiento = models.CharField(max_length=5 , default='')
    precio =  models.CharField(max_length=8, default = "0")
    
class Actualizacion(models.Model):
    ultima_act = models.IntegerField()
