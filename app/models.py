from django.db import models

# Create your models here.
class Carros(models.Model):
    modelo = models.CharField(max_length=36)
    marca = models.CharField(max_length=36)
    ano = models.IntegerField()
