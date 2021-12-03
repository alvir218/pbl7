from django.db import models

from disciplinaApp.models import Disciplina
from editoraApp.models import Editora


# Create your models here.


class Livros(models.Model):
    cod_livro = models.AutoField(primary_key=True)
    editora_id = models.ForeignKey(
        Editora, related_name='Editora', on_delete=models.CASCADE)
    ISBN = models.CharField(max_length=100)
    Titulo_livro = models.CharField(max_length=100)
    autor_livro = models.CharField(max_length=100)
    edicao_livro = models.CharField(max_length=100)
    ano_ancamento = models.CharField(max_length=100)
    cod_biblioteca = models.CharField(max_length=100)
    link_livro = models.CharField(max_length=100)
    status_livro = models.CharField(max_length=100)


class Biblioteca(models.Model):
    cod_biblioteca = models.AutoField(primary_key=True)
    nome_biblioteca = models.CharField(max_length=100)
    sigla_biblioteca = models.CharField(max_length=100)
    modalidade_virtual = models.CharField(max_length=100)


class DisciplinaLivro(models.Model):
    DisciplinaId = models.ForeignKey(
        Disciplina, related_name='DisciplinaLivro', on_delete=models.CASCADE)
    cod_livro = models.ForeignKey(
        Livros, related_name='DisciplinaLivro', on_delete=models.CASCADE)
    bibliografia_basica = models.CharField(max_length=100)
