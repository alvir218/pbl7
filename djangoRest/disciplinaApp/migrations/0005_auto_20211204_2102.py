# Generated by Django 3.2.9 on 2021-12-05 00:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('disciplinaApp', '0004_auto_20211203_0147'),
    ]

    operations = [
        migrations.AlterField(
            model_name='disciplina',
            name='CodCronograma',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='disciplina',
            name='CodProcedimentos',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='disciplina',
            name='CodSistematica',
            field=models.IntegerField(),
        ),
    ]
