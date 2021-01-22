from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=200, verbose_name="Titulo")
    description = models.TextField(verbose_name="Descripción");
    image = models.ImageField(verbose_name="Imagen", upload_to="projects");
    link = models.URLField(verbose_name="Direccion web", null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")#Solo se ejecuta la primera vez
    updated =  models.DateTimeField(auto_now=True, verbose_name="Fecha de modifiación")#Se ejecuta cada vez que se vuelva a hacer una instancia
    class Meta:
        verbose_name = "proyecto"
        verbose_name_plural = "proyectos"
        #Campo de ordenación 
        ordering = ["-created"]#Ordenamos de más nuevo  a más antiguo

    #Establecemos el titulo ingresado 
    def __str__(self):
        return self.title
    