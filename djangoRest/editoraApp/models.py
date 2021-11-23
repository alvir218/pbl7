from django.db import models


class Editora(models.Model):
    EditoraId = models.AutoField(primary_key=True)
    NomeEditora = models.CharField(max_length=100)
    LocalEditora = models.CharField(max_length=100)
