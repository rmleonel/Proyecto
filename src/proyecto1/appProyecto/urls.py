from django.urls import path
from appProyecto.views import (profesores , estudiantes, cursos, entregables, index, formulario, busqueda_camada, buscar_camada)

urlpatterns = [
    path("profesores/", profesores, name ='profesores'),
    path("estudiantes/", estudiantes, name = 'estudiantes'),
    path("cursos/", cursos, name = 'cursos'),
    path("entregables/", entregables, name = 'entregables'),
    path("formulario/", formulario, name = 'formulario'),
    path("busquedaCamada", busqueda_camada, name="busqueda_camada"),
    path("buscar", buscar_camada, name="buscar_camada"),
    path("", index, name = 'index'),
]