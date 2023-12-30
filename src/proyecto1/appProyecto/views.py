from django.http import HttpResponse
from django.shortcuts import render
from appProyecto.models import Profesor

from appProyecto.models import Profesor, Curso


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

def profesores(request):
    return render(request, 'profesores.html')

def estudiantes(request):
    return render(request, 'estudiantes.html')

def cursos(request):
    return render(request, 'cursos.html')

def entregables(request):
    return render(request, 'entregables.html')

def formulario(request):

    #Path de la ruta
    print(f"path: {request.path}")
    print(f"full path: {request.get_full_path()}")
    print(f"host: {request.get_host()}")
    print(f"si es segura: {request.is_secure()}")
    print(f"metodo: {request.method}")
    ua = request.META.get("HTTP_USER_AGENT")
    print(f"ua: {ua}")

    if request.method == "POST":

        nombre = request.POST.get("curso")
        camada = request.POST.get("camada")

        curso = Curso(nombre=nombre, camada=camada)
        curso.save()
        return render(request,'index.html')

    return render(request, "formulario.html")

def busqueda_camada(request):
    if request.method == "GET":
        camada = request.GET.get("camada")
        print(f"Vamos a buscar la camada: {camada}")


    return render(request, "busqueda_camada.html")

def buscar_camada(request):
    if request.method == "GET":

        camada = request.GET.get("camada")

        if camada is None:
            return HttpResponse("Enviar la camada a buscar")
        
        #Siguiente paso buscar los datos

        cursos = Curso.objects.filter(camada_icontains =camada)
        contexto = {
            "cursos": cursos,
            "camada": camada,
        }
        return render(request, "busqueda.html", contexto)
    
    return HttpResponse(f"Se busco la camada : {camada}")
