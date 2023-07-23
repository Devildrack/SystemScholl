from django.contrib import admin

#Importar los modelos creados en el models.py
from .models import Estudiante, Profesor, Curso, Asignacion, Calificacion, Evento, Noticia

# Register your models here.

admin.site.register(Estudiante)
admin.site.register(Profesor)
admin.site.register(Curso)
admin.site.register(Asignacion)
admin.site.register(Calificacion)
admin.site.register(Evento)
admin.site.register(Noticia)

