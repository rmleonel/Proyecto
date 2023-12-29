from django.db import models

class Profesor(models.Model):

    nombre = models.CharField(max_length = 20)
    apellido = models.CharField(max_length = 30)
    email = models.EmailField()

    def __str__(self):
        return f"{self.nombre}, {self.apellido }"
    class Meta: 
        verbose_name_plural = "Profesores"

class Estudiantes(models.Model):
    nombre = models.CharField(max_length = 20)
    apellido = models.CharField(max_length = 20)
    email = models.EmailField()

    def __str__(self):
        return f"{self.nombre}, {self.apellido}"
    class Meta: 
        verbose_name_plural = "Estudiantes"

class Curso(models.Model):
    nombre = models.CharField(max_length = 20)
    camada = models.IntegerField()

    def __str__(self):
        return f"{self.nombre} -- {self.camada}"

class Entrgables(models.Model):
    nombre = models.CharField(max_length = 40)
    fechaDeEntrega = models.DateField()
    entregado = models.BooleanField()

    class Meta: 
        verbose_name_plural = "Entregables"