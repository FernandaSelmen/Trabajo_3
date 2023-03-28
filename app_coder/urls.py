from django.urls import path
from app_coder.views import inicio , bucadorCurso
urlpatterns = [
    path('index/', inicio, name = 'inicio' ),
    path('buscador_curso/', bucadorCurso, name = 'curso' ),
]