#incluir el path de django.urls, importar el default routers y los viesets
from django.urls import path, include
from rest_framework import routers
from api import views

router = routers.DefaultRouter()

router.register(r'estudiantes', views.EstudianteViewSet)
router.register(r'profesores', views.ProfesorViewSet)
router.register(r'cursos', views.CursoViewSet)
router.register(r'asignaciones', views.AsignacionViewSet)
router.register(r'calificaciones', views.CalificacionViewSet)
router.register(r'eventos', views.EventoViewSet)
router.register(r'noticias', views.NoticiaViewSet)

urlpatterns = [
    path('', include(router.urls)),
]