from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Curso(models.Model):
    
  nombre = models.CharField(max_length=50)
  camada = models.IntegerField()

  def __str__(self):
    return f'{self.nombre}'
  
  class Meta:

    verbose_name = 'Course'
    verbose_name_plural = 'The Courses'
    ordering = ('-nombre',)
    unique_together = ['nombre', 'camada']

class Estudiante(models.Model):

  nombre = models.CharField(max_length=50)
  apellido = models.CharField(max_length=50)
  email = models.EmailField(max_length=254)
  user_id = models.OneToOneField(User, on_delete=models.CASCADE)

  def __str__(self):
    return f'{self.nombre}'  

class Profesor(models.Model):

  nombre = models.CharField(max_length=50)
  apellido = models.CharField(max_length=50)
  email = models.EmailField(max_length=254)
  profesion = models.CharField(max_length=50)
  user_id = models.OneToOneField(User, on_delete=models.CASCADE)
  cursos = models.ManyToManyField(Curso)

  def __str__(self):
    return f'{self.nombre} {self.apellido}'

class Entregable(models.Model):

  nombre = models.CharField(max_length=50)
  fecha_entrega = models.DateField()
  entregado = models.BooleanField()
  estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)


class Avatar(models.Model):

  user = models.ForeignKey(User, on_delete=models.CASCADE)
  imagen = models.ImageField(upload_to='avatares', null=True, blank=True)