from django.db import models
from django.db.models import fields
from rest_framework import serializers
from Livros import models
from Livros.models import Livros, Biblioteca, DisciplinaLivro



class LivrosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Livros
        fields='__all__'


class BibliotecaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Biblioteca
        fields='__all__'


class DisciplinaLivroSerializers(serializers.ModelSerializer):
    class Meta:
        model = DisciplinaLivro
        fields='__all__'
