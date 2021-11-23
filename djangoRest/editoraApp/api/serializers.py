from django.db import models
from django.db.models import fields
from rest_framework import serializers
from editoraApp import models


class EditoraSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Editora
        fields = '__all__'
