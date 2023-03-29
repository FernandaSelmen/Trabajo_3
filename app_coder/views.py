from django.shortcuts import render
from app_coder.models import Curso, Alumno, Profesor
from app_coder.forms import ProfesorForm

 

# Create your views here.

def inicio(request):
    return render(request, 'app_coder/index.html')


def bucadorCurso( request):
     
     if request.method == 'POST':
      
            curso =  Curso(request.post['curso'],(request.post['camada']))
 
            curso.save()

           

     return render(request, 'app_coder/buscador_curso.html')


def bucadorAlumno( request):
     
     if request.method == 'POST':
      
            alumno =  Alumno(request.post['nombre'],(request.post['apellido']), (request.post['correo']))
 
            alumno.save()


     return render(request, 'app_coder/buscador_alumno.html')



def profesorForms(request):
 
      if request.method == "POST":
 
            miFormulario = ProfesorForm(request.POST) 
            print(miFormulario)
 
            if miFormulario.is_valid:
                  informacion = miFormulario.cleaned_data

                  nombre=informacion["nombre"]
                  apellido = informacion["apellido"]
                  correo =informacion["correo"]
                  profesion = informacion["profesion"]

                  profesor = Profesor(nombre= nombre, apellido = apellido, correo = correo, profesion= profesion)
                  profesor.save()

                  return render(request, "app_coder/profeFormulario.html")
      else:
            miFormulario = ProfesorForm()
 
      return render(request, "app_coder/profeFormulario.html", {"miFormulario": miFormulario})




def buscarProfe(request):

    if request.method == "POST":

        nombre = request.POST.get("nombre")
        apellido = request.POST.get("apellido")

        profebuscado = Profesor.objects.filter(nombre=nombre, apellido=apellido)

    return render(request, "app_coder/resultadosProfesor.html", {'data': [profebuscado]})
    #else:
       # miFormulario = ProfesorForm()
       # return render(request, "app_coder/resultadosProfesor.html", {"miFormulario": miFormulario})




