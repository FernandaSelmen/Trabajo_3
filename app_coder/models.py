from django.db import models

# Create your models here.

class Curso(models.Model):
    curso = models.CharField(max_length=30)
    camada = models.IntegerField()
    def __str__(self):
           
         return f'Curso: {self.curso} - Camada: {self.camada}'

class Profesor(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=20)
    correo = models.EmailField()
    profesion = models.CharField(max_length=30)

    def __str__(self):
           
         return f'Nombre:  {self.nombre} - Apellido:  {self.apellido} - Profesion:  {self.profesion} - Correo: {self.correo}'


class Alumno(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=20)
    correo = models.EmailField()
    def __str__(self):
           

         return f'Nombre: {self.nombre} - Apellido: {self.apellido} - Correo: {self.correo}'


class Entregables(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=20)
    proyecto = models.CharField(max_length=60)
    hora = models.TimeField()
    def __str__(self):
           
         return f'Nombre: {self.nombre} - Apellido: {self.apellido} - Proyecto: {self.proyecto} -Hora: {self.hora}'

    
    
    