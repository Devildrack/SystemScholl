from django.shortcuts import render

#imoortar el viewsets de restframework, los serializers del modelo, y los modelos creados
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets
from .models import Estudiante, Profesor, Curso, Asignacion, Calificacion, Evento, Noticia
from .serializers import EstudianteSerializer, ProfesorSerializer, CursoSerializer, AsignacionSerializer, CalificacionSerializer, EventoSerializer, NoticiaSerializer


# Create your views here.

#crear los viewsets
class EstudianteViewSet(viewsets.ModelViewSet):
    queryset = Estudiante.objects.all()
    serializer_class = EstudianteSerializer

class ProfesorViewSet(viewsets.ModelViewSet):
    queryset = Profesor.objects.all()
    serializer_class = ProfesorSerializer

class CursoViewSet(viewsets.ModelViewSet):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

class AsignacionViewSet(viewsets.ModelViewSet):
    queryset = Asignacion.objects.all()
    serializer_class = AsignacionSerializer

class CalificacionViewSet(viewsets.ModelViewSet):
    queryset = Calificacion.objects.all()
    serializer_class = CalificacionSerializer

class EventoViewSet(viewsets.ModelViewSet):
    queryset = Evento.objects.all()
    serializer_class = EventoSerializer

class NoticiaViewSet(viewsets.ModelViewSet):
    queryset = Noticia.objects.all()
    serializer_class = NoticiaSerializer