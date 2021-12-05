#editado do zero

from rest_framework import serializers
from professores import models

class ProfessoresSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Professores
        fields = '__all__'