from rest_framework import viewsets
from cursos.api import serializer
from cursos import models

class CursosViewSets(viewsets.ModelViewSet):
  serializer_class = serializer.CursosSerializer
  queryset = models.Cursos.objects.all()