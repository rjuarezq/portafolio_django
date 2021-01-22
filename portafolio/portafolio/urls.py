"""portafolio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from core import views as core_views
from proyectos import views as project_views


#Para buscar dentro de la configuración de django para poder acceder a las variables MEDIA_URL y MEDIA_ROOT
from django.conf import settings

urlpatterns = [
    path('', core_views.home, name="index"),
    path('about-me/', core_views.aboutMe, name="about"),
    path("portafolio/", project_views.portafolio, name = "portafolio"),
    path("contact/", core_views.contactMe, name="contact"),
    path('admin/', admin.site.urls),
]

#Configuración extendido solo en modo DEBUG
if settings.DEBUG == True:
    #Import para servir ficheros estaticos
    from django.conf.urls.static import static
    #Servir imagen de turno(URL_FICHEROS_MEDIA, RAIZ_FICHEROS)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
