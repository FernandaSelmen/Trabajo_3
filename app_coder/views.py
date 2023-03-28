from django.shortcuts import render
from app_coder.models import Curso
# Create your views here.

def inicio(request):
    return render(request, 'app_coder/index.html')


def bucadorCurso( request):
     
     if request.method == 'POST':
      
            curso =  Curso(request.post['curso'],(request.post['camada']))
 
            curso.save()

            return render(request, 'app_coder/buscador_curso.html')

     return render(request, 'app_coder/buscador_curso.html')

