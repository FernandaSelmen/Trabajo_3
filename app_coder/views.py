from django.shortcuts import render
from app_coder.models import Curso, Alumno, Profesor, Entregables, After
from app_coder.forms import ProfesorForm, AlumnoForm, EntregablesForm, AfterForm

 

# Create your views here.

def inicio(request):
    return render(request, 'app_coder/index.html')


def bucadorCurso( request):
     
     if request.method == 'POST':

            curso = request.POST['curso']
            camada = request.POST['camada']

            cursos =  Curso(curso = curso, camada = camada)
 
            cursos.save()

           

     return render(request, 'app_coder/buscador_curso.html')

            

def bucadorAlumno( request):
     
      if request.method == "POST":
 
            miFormulario = AlumnoForm(request.POST) 
            print(miFormulario)
 
            if miFormulario.is_valid:
                  informacion = miFormulario.cleaned_data

                  nombre=informacion["nombre"]
                  apellido = informacion["apellido"]
                  correo =informacion["correo"]
                 

                  alumno = Alumno(nombre= nombre, apellido = apellido, correo = correo)

                  alumno.save()

                  return render(request, "app_coder/buscador_alumno.html")
      else:
            miFormulario = AlumnoForm()
 
      return render(request, "app_coder/buscador_alumno.html", {"miFormulario": miFormulario})

     



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

        return render(request, "app_coder/resultadosProfesor.html", {'data': profebuscado})
    
       # miFormulario = ProfesorForm()
    return render(request, "app_coder/resultadosProfesor.html", {})



     

def entrega(request):

      if request.method == "POST":
 
            miFormulario = EntregablesForm(request.POST) 
            print(miFormulario)
 
            if miFormulario.is_valid:

                  informacion = miFormulario.cleaned_data

                  nombre=informacion["nombre"]
                  apellido = informacion["apellido"]
                  proyecto =informacion["proyecto"]
                  hora =informacion["hora"]
                 

                  entregalo = Entregables(nombre= nombre, apellido = apellido, proyecto = proyecto, hora = hora)
                  entregalo.save()

                  return render(request, "app_coder/entregacion.html")
      else:
            miFormulario = EntregablesForm()
 
      return render(request, "app_coder/entregacion.html", {"miFormulario": miFormulario})
    
       
  
def aff(request):

      if request.method == "POST":
 
            formulario = AfterForm(request.POST) 
            print(formulario)
 
            if formulario.is_valid:

                  info = formulario.cleaned_data

                  nombre_del_after = info["nombre_del_after"]
                  tema_a_tocar = info["tema_a_tocar"]
                  hora_de_inicio =info["hora_de_inicio"]
                  zoom =info["zoom"]
                 

                  
                  after = After(nombre_del_after = nombre_del_after, tema_a_tocar = tema_a_tocar, hora_de_inicio = hora_de_inicio, zoom = zoom )
                  
                  after.save()

                  return render(request, "app_coder/after.html")
      else:
            formulario = AfterForm()
 
      return render(request, "app_coder/after.html", {"formulario": formulario})
    
       
   
