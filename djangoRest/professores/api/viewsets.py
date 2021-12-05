#editado do zero

from rest_framework import viewsets
from professores.api import serializers
from professores import models


class ProfessoresViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ProfessoresSerializer
    queryset = models.Professores.objects.all()