from django.shortcuts import render
from app_coder.models import Curso, Alumno
# Create your views here.

def inicio(request):
    return render(request, 'app_coder/index.html')


def bucadorCurso( request):
     
     if request.method == 'POST':
      
            curso =  Curso(request.post['curso'],(request.post['camada']))
 
            curso.save()

            return render(request, 'app_coder/buscador_curso.html')

     return render(request, 'app_coder/buscador_curso.html')


def bucadorAlumno( request):
     
     if request.method == 'POST':
      
            alumno =  Alumno(request.post['nombre'],(request.post['apellido']), (request.post['correo']))
 
            alumno.save()

            return render(request, 'app_coder/buscador_alumno.html')

     return render(request, 'app_coder/buscador_alumno.html')



