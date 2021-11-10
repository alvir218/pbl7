from django.db.models import fields
from django.db.models.base import Model
from rest_framework import serializers
from EditoraApp.models import Editora, EditoraLivro, Livro


class EditoraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Editora
        fields = ('EditoraId', 'NomeEditora', 'LocalEditora')


class LivroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Livro
        fields = ('LivroId')


class EditoraLivroSerializer(serializers.ModelSerializer):
    class Meta:
        model = EditoraLivro
        fields = ('Id_Editora', 'Id_Livro')
