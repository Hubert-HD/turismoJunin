from django.db import models
from django.db.models.fields import BooleanField

# Create your models here.

class Provincia(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255, blank=False, null=False)

    def __str__(self):
        return self.nombre
    
class Distrito(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255, blank=False, null=False)
    provincia_id=models.ForeignKey(Provincia, on_delete=models.CASCADE, blank=False, null=False)

    def __str__(self):
        return self.nombre

class Categoria(models.Model):
    id = models.AutoField(primary_key = True)
    nombre = models.CharField(max_length=255, blank=False, null=False)
    tipo = BooleanField()

    def __str__(self):
        return self.nombre

class Recurso(models.Model):
    id = models.AutoField(primary_key = True)
    nombre = models.CharField(max_length=255, blank=False, null=False)
    image_URL = models.URLField(blank=True)
    subtitulo = models.CharField(max_length=255, blank=False, null=False)
    descripcion = models.TextField(max_length=255, blank=True, null=True)
    distrito_id = models.ForeignKey(Distrito, on_delete=models.CASCADE, blank=False, null=False)
    categoria_id = models.ForeignKey(Categoria, on_delete=models.CASCADE, blank=False, null=False)

    def __str__(self):
        return self.nombre

class Coordenadas(models.Model):
    id = models.AutoField(primary_key = True)
    recurso_id = models.OneToOneField(Recurso, on_delete=models.CASCADE, blank=False, null=False)
    latitud = models.FloatField(blank=True, null=True)
    longitud = models.FloatField(blank=True, null=True)