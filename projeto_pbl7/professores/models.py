#editado do zero

from django.db import models

#adicioando a biblioteca dos id automatizados
from uuid import uuid4

from django.db.models.fields import CharField

# Create your models here.


#estruturando as tabelas no banco de dados
class Professores(models.Model):
    cod_professor = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    nome_professor = models.CharField(max_length=320)
    ru = models.CharField(max_length=16)
    matricula = models.IntegerField()
    formacao = models.CharField(max_length=1024)
    titulacao = models.CharField(max_length=1024)
    area_titulacao = models.CharField(max_length=1024)
    endereco_completo = models.CharField(max_length=512)
    telefone_fixo = models.CharField(max_length=16)
    whatsapp = models.CharField(max_length=16)
    email = models.CharField(max_length=64)
    data_ingresso_instituicao = models.DateField(auto_now_add=True)
    data_docencia = models.DateField(blank=True, null=True)
    data_docencia_instituicao = models.DateField(blank=True, null=True)
    funcao = models.CharField(max_length=128)
    regime_trabalho = CharField(max_length=64)



#colocando o basico das tabelas dos outros grupos
#para fazer o relacionamento com as foreignkey

class Cursos(models.Model):
    cod_curso = models.UUIDField(primary_key=True, default=uuid4, editable=False)


class Disciplinas(models.Model):
    cod_disciplina = models.UUIDField(primary_key=True, default=uuid4, editable=False)



#criando as tabelas com as foreignkey muito pra muitos

#tentativa 1 erro

''' class Disciplina_Professor(models.Model):
    cod_disciplina = models.ManyToManyField(Disciplinas, through='cod_disciplina')
    cod_professor = models.ManyToManyField(Professores, through='cod_professor')

class Curso_Professor(models.Model):
    cod_curso = models.ManyToManyField(Cursos, through='cod_curso')
    cod_professor = models.ManyToManyField(Professores, through='cod_professor') '''


#tentativa 2

class Curso_Professor(models.Model):
    cod_curso = models.ForeignKey(Cursos, on_delete = models.CASCADE)
    cod_professor = models.ForeignKey(Professores, on_delete = models.CASCADE)


class Disciplina_Professor(models.Model):
    cod_disciplina = models.ForeignKey(Disciplinas, on_delete=models.CASCADE)
    cod_professor = models.ForeignKey(Professores, on_delete = models.CASCADE)


