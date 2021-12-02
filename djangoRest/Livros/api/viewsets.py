from django.db import models
from rest_framework import viewsets
from Livros.api import serializers
from Livros import models



class LivrosViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.LivrosSerializer
    queryset = models.Livros.objects.all()

class BibliotecaViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.BibliotecaSerializers
    queryset = models.Biblioteca.objects.all()

class DisciplinaViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.DisciplinaLivroSerializers
    queryset = models.DisciplinaLivro.objects.all()
