from django.shortcuts import render
from .models import Project

# Create your views here.
def portafolio(request):
    #Recuperamos la lista de proyectos que esta almacenado con el ORM
    projects = Project.objects.all()#Nos devolvera todos los objs del proyecto
    
    return render(request, "proyectos/portafolio.html", {'projects' : projects})