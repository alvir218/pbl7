"""pbl URL Configuration

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
from django.urls import path, include

from rest_framework import routers
from editoraApp.api import viewsets as editoraviewsets
from disciplinaApp.api import viewsets as disciplinaviewsets
from cursos.api import viewsets as cursosviewsets
from Livros.api import viewsets as livrosviewsets
from professores.api import viewsets as professoresviewsets

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
    openapi.Info(
        title="PBL VII",
        default_version='v1',
        description="Problem Based Learning VII Uninter Engenharia da Computação",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


route = routers.DefaultRouter()
route.register(r'pbl/editora', editoraviewsets.EditoraViewSet,
               basename="editora")

route.register(r'pbl/disciplina', disciplinaviewsets.DisciplinaViewSet,
               basename="disciplina")

route.register(r'pbl/cursos', cursosviewsets.CursosViewSets,
               basename="cursos")

route.register(r'pbl/livros', livrosviewsets.LivrosViewSet,
               basename="livros")

route.register(r'pbl/biblioteca', livrosviewsets.BibliotecaViewSet,
               basename="biblioteca")

route.register(r'pbl/professores', professoresviewsets.ProfessoresViewSet,
               basename="professores")


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(route.urls)),
    path('swagger.yaml',
         schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger',
         cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc',
         cache_timeout=0), name='schema-redoc'),
]
