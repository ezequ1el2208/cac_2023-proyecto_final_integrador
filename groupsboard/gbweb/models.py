'''
Models classes
'''
from django.contrib.auth.models import User
from django.db import models


# Create your models here.
options_type=(
    ('Público','Público'),
    ('Privado','Privado')
    )

class Lider(models.Model):
    lider = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    legajo = models.CharField(max_length=100, verbose_name='Legajo')
   
    
    def __str__(self):
        return self.lider.username

class Estudiante(models.Model):
    estudiante = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    legajo = models.CharField(max_length=100, verbose_name='Legajo')

    def __str__(self):
        return self.estudiante.username

class Grupo(models.Model):
    nombre = models.CharField(max_length=200, verbose_name='Nombre del grupo:')
    tipo = models.CharField(max_length=10, choices=options_type)
    tema =models.CharField(max_length=200, verbose_name='Tema del grupo')
    descripcion = models.CharField(max_length=200, verbose_name='Descripción del grupo')
    proximo_encuentro = models.DateField(verbose_name='Próxima reunión')
    lider= models.ForeignKey(Lider, on_delete=models.CASCADE)
    estudiante = models.ManyToManyField(Estudiante)

    def __str__(self):
        return self.nombre
    
class Tarea(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField(null=True, verbose_name='Descripción')
    grupo = models.ForeignKey(Grupo, on_delete=models.CASCADE)
    terminado = models.BooleanField(default=False)

    def __str__(self):
        return self.titulo + ' - ' + self.grupo.nombre