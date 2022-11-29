from django.db import models

# Create your models here.
class Recomendacion(models.Model):
    nombre = models.CharField(max_length=40)
    correo = models.EmailField()
    comida = models.CharField(max_length=11)
    comentario = models.CharField(max_length=500)

class Post(models.Model):
    nombre = models.CharField(max_length=50)
    articulo = models.CharField(max_length=500)
    imagen = models.URLField()
    autor = models.CharField(max_length=50)

class Reclamos(models.Model):
    nombre = models.CharField(max_length=40)
    email = models.EmailField()
    categoria = models.CharField(max_length=11)
    nota = models.CharField(max_length=500)
    