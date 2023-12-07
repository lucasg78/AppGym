from django.urls import path
from Socios.views import *

urlpatterns = [
    path("clases/", clases),
    path("profesores/", profesores),
    path("alumnos/", alumnos)
]
