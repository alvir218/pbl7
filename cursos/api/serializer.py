from rest_framework import serializers
from cursos import models

class CursosSerializer(serializers.ModelSerializer):
  class Meta:
    model = models.Cursos
    fields = '__all__'
