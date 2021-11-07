#editado parcialmente


"""projeto_pbl7 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
#adicionando tambem o include
from django.urls import path, include

#importar o necessario para configurar as rotas
from rest_framework import routers
from professores.api import viewsets as professoresviewsets

route = routers.DefaultRouter()

route.register(r'professores', professoresviewsets.ProfessoresViewSet, basename='Professores')

urlpatterns = [
    path('admin/', admin.site.urls),
    
    #incluindo a rota previamente configurada
    path('', include(route.urls))
]
