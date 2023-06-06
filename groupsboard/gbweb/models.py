'''
Models classes
'''
from django.db import models

# Create your models here.
options_type=(
    (1,'Público'),
    (2,'Privado')
    )

class Persona(models.Model):
    nombre = models.CharField(max_length=100, verbose_name='Nombre:')
    apellido = models.CharField(max_length=100, verbose_name='Apellido:')
    email = models.EmailField(max_length=150, verbose_name='Email')
    dni = models.BigIntegerField(verbose_name='DNI:')
    username = models.CharField(max_length=50, verbose_name="Nombre de usuario", null=True)
    password = models.CharField(max_length=50, verbose_name="Contraseña", null=True)

    def __str__(self):
        return self.nombre

class Grupo(models.Model):
    groupname = models.CharField(max_length=200, verbose_name='Nombre del grupo:')
    grouptype = models.CharField(max_length=1, choices=options_type)
    grouptheme =models.CharField(max_length=200, verbose_name='Tema del grupo')
    groupdescription = models.CharField(max_length=200, verbose_name='Descripción del grupo')
    next_meeting = models.DateField(verbose_name='Próxima reunión')

    def __str__(self):
        return self.groupname

class Estudiante(models.Model):
    persona = models.OneToOneField(Persona, on_delete=models.CASCADE, primary_key=True)
    legajo = models.CharField(max_length=100, verbose_name='Legajo')
    cursos = models.ManyToManyField(Grupo)

    def __str__(self):
        return self.persona.nombre
    
class Instructor(models.Model):
    persona = models.OneToOneField(Persona, on_delete=models.CASCADE, primary_key=True)
    legajo = models.CharField(max_length=100, verbose_name='Legajo')
    cursos = models.ManyToManyField(Grupo)

    def __str__(self):
        return self.persona.nombre
    
class Tarea(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, verbose_name='Descripcion')
    group = models.ForeignKey(Grupo, on_delete=models.CASCADE)
    done = models.BooleanField(default=False)

    def __str__(self):
        return self.title + ' - ' + self.group.groupname