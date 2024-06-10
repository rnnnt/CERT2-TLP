from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Estudiante(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.name

class Profesor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, default="Profesor")
    especialidad = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Project(models.Model):
    name = models.CharField(max_length=200)
    theme = models.CharField(max_length=50, default=None)
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE, default=None)
    profesor = models.ForeignKey(Profesor, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name
    