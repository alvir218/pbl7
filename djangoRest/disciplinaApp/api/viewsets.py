from django.db import models
from rest_framework import viewsets
from disciplinaApp.api import serializers
from disciplinaApp import models

class DisciplinaViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.DisciplinaSerializer
    queryset = models.Disciplina.objects.all()