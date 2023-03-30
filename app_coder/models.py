from django.db import models

# Create your models here.

class Curso(models.Model):
    curso = models.CharField(max_length=30)
    camada = models.IntegerField()

class Profesor(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=20)
    correo = models.EmailField()
    profesion = models.CharField(max_length=30)


class Alumno(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=20)
    correo = models.EmailField()
   



class Entregables(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=20)
    proyecto = models.CharField(max_length=60)
    hora = models.TimeField()

    
    
    