from django.http import HttpResponse
from django.shortcuts import render
from appProyecto.models import Profesor


def leer_profesor(request):
    profesor = Profesor(nombre = "Marcos", apellido = "Leguizamon", email= "mlegui@gmail.com")
    profesor.save()
    return HttpResponse("El profesor se creo exitosamente")

def leer_alumnos(request):
    
    contexto = {
        "nombre": "Juan",
        "apellido": "Hernandez",
        "edad": 67,
        "cursos": ["Python", "SQL", "R"],
    }
    return render(request, "plantilla.html", contexto )

def index(request):
    return render (request, "index.html")