from django.db import models
from django.db.models import fields
from rest_framework import serializers
from disciplinaApp import models


class DisciplinaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Disciplina
        fields = '__all__'