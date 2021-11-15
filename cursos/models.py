from django.db import models

# Create your models here.

class Cursos(models.Model):
  cod_curso = models.IntegerField()
  nome_curso = models.CharField(max_length=50)
  cod_curso_5e = models.IntegerField()
  cod_grade = models.IntegerField()
  cod_coordenador = models.CharField(max_length=50)
  modalidade = models.CharField(max_length=50)
  nivel = models.CharField(max_length=50)

  def __str__(self):
    return self.nome_curso
