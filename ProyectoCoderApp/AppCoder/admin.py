# from math import floor
from datetime import datetime
from django.contrib import admin
from .models import Curso, Entregable, Estudiante, Profesor, Avatar

class CursoAdmin(admin.ModelAdmin):
    
    list_display = ['nombre', 'camada']
    search_fields = ['nombre', 'camada']
    list_filter = ['nombre', 'camada']


class EntregableAdmin(admin.ModelAdmin):
    
    list_display = ['nombre', 'antiguedad']

    def antiguedad(self, object):
      print('*****', object)
      if object.fecha_entrega:
          return (datetime.now().date() - object.fecha_entrega).days

class ProfesorAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'apellido', 'email']
    list_filter = ['nombre', 'apellido']
    filter_horizontal = ['cursos']


# Register your models here.
admin.site.register(Curso, CursoAdmin)
admin.site.register(Entregable, EntregableAdmin)
admin.site.register(Estudiante)
admin.site.register(Profesor, ProfesorAdmin)
admin.site.register(Avatar)


