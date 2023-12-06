from django.contrib import admin
from django.urls import path
from AppGym.views import *
from Socios.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('inicio/', vista_plantilla),
    #path('alumnos/', vista_listado_alumnos),
    path('alumnos/', vista_listado_alumnos2),   
    path("clases/", vista_listado_clases),
    path("clases2/", vista_listado_clases2),
    path("profesores/", vista_listado_profesores),
]
