from django.db import models
from rest_framework import viewsets
from editoraApp.api import serializers
from editoraApp import models


class EditoraViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.EditoraSerializer
    queryset = models.Editora.objects.all()
