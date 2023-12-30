from django.urls import path
from appProyecto.views import (profesores , estudiantes, cursos, entregables, index, formulario)

urlpatterns = [
    path("profesores/", profesores, name ='profesores'),
    path("estudiantes/", estudiantes, name = 'estudiantes'),
    path("cursos/", cursos, name = 'cursos'),
    path("entregables/", entregables, name = 'entregables'),
    path("formulario/", formulario, name = 'formulario'),
    path("", index, name = 'index'),
]