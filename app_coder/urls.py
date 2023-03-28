from django.urls import path
from app_coder.views import inicio
urlpatterns = [
    path('index/', inicio, name = 'inicio' ),
]