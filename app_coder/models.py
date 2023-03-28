from django.db import models

# Create your models here.

class Curso(models.Model):
    curso = models.CharField(max_length=30)
    camada = models.IntegerField()

