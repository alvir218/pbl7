from django.db import models
from django.db.models.base import Model

# Create your models here.


class Editora(models.Model):
    EditoraId = models.AutoField(primary_key=True)
    NomeEditora = models.CharField(max_length=100)
    LocalEditora = models.CharField(max_length=100)


class EditoraLivro(models.Model):
    Id_Editora = models.CharField(max_length=100)
    Id_Livro = models.CharField(max_length=100)


class Livro(models.Model):
    LivroId = models.AutoField(primary_key=True)
