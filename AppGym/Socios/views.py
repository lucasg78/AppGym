from django.http import HttpResponse
from Socios.models import Clase, Profesor

# Create your views here.
def vista_listado_clases2(request):
    clases = Clase.objects.all()
    
    cadena_respuesta = ""
    for clase in clases:
        cadena_respuesta += f"Clase: {clase.nombre} - Comisión: {clase.comision}" + " " +"<br/>"
    
    return HttpResponse(cadena_respuesta) 

def vista_listado_profesores(request):
    profesores = Profesor.objects.all()
    
    cadena_respuesta = ""
    for profesor in profesores:
        cadena_respuesta += f"Profesor: {profesor.nombre} {profesor.apellido}" + " " +"<br/>"
    
    return HttpResponse(cadena_respuesta) 
