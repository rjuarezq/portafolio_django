from django.contrib import admin
from .models import Project
# Register your models here.
class ProjectAdmin(admin.ModelAdmin):
    #Mostramos los campos de lectura en el panel de administración
    readonly_fields = ('created', 'updated')

#Pasamos la configuración extendida al momento de registrar el modelo al panel admin
admin.site.register(Project, ProjectAdmin)