from django.shortcuts import render
from app_coder.models import Curso, Alumno
# Create your views here.

def inicio(request):
    return render(request, 'app_coder/index.html')


def bucadorCurso( request):
     
     if request.method == 'POST':
            
        curso = request.POST['curso']

        camada = request.POST['camada']
      
        cursos =  Curso(curso = curso, camada =camada)
        

        cursos.save()
           

     return render(request, 'app_coder/buscador_curso.html')

 
           


def bucadorAlumno( request):
     
     if request.method == 'POST':
        
            nombre = request.POST['nombre']

            apellido = request.POST['apellido']

            correo = request.POST['correo']


            alumno =  Alumno(nombre = nombre, apellido = apellido, correo = correo)
 
            alumno.save()


     return render(request, 'app_coder/buscador_alumno.html')



