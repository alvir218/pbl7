#editado parcialmente

"""library URL Configuration

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
#incluido include para importar todas as rotas do projeto

from rest_framework import routers
import books
from books.api import viewsets as booksviewsets


#link com as urls do books
from django.conf.urls import url, include


#especificacao da url das imagens
###from django.conf.urls.static import static
###from django.conf import settings

#criando uma rota
#objeto sera adicionado depois nas rotas
route = routers.DefaultRouter()

route.register(r'books', booksviewsets.BooksViewSet, basename='Books')

#admin vem por padrao e nao foi modificado
#criado rota padrao em / com apostrofos ''
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(route.urls)),

    #incluindo as urls do books
    url(r'^', include('books.urls'))
] ###+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#soma com a rota das imagens

