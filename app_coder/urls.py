from django.urls import path
from app_coder.views import inicio , bucadorCurso, bucadorAlumno
urlpatterns = [
    path('index/', inicio, name = 'inicio' ),
    path('buscador_curso/', bucadorCurso, name = 'Curso' ),

    path('buscador_alumno/', bucadorAlumno, name = 'Alumno' ),
]