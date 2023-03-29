from django.urls import path
from app_coder.views import inicio , bucadorCurso, bucadorAlumno, profesorForms, buscarProfe



urlpatterns = [
    path('index/', inicio, name = 'inicio' ),

    path('buscador_curso/', bucadorCurso, name = 'Curso' ),

    path('buscador_alumno/', bucadorAlumno, name = 'Alumno' ),

    path('profeFormulario/', profesorForms, name = 'Profesor' ),

    path('resultadosProfesor/', buscarProfe, name = 'BusquedaP' ),

]