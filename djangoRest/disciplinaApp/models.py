from django.db import models

class Disciplina(models.Model):
    DisciplinaId = models.AutoField(primary_key=True)
    NomeDisciplina = models.CharField(max_length=100)
    CargaHoraria = models.CharField(max_length=100)
    Ementa = models.CharField(max_length=1000)
    Habilidades = models.CharField(max_length=1000)
    Competencias = models.CharField(max_length=1000)
    CodProcedimentos = models.CharField(max_length=100)
    CodSistematica = models.CharField(max_length=100)
    CodCronograma = models.CharField(max_length=100)

# Create your models here.
