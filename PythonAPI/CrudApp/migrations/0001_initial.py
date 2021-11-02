# Generated by Django 3.2.8 on 2021-10-29 04:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Editora',
            fields=[
                ('EditoraId', models.AutoField(primary_key=True, serialize=False)),
                ('NomeEditora', models.CharField(max_length=100)),
                ('LocalEditora', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Livro',
            fields=[
                ('LivroId', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='EditoraLivro',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('Id_Editora', models.CharField(max_length=100)),
                ('Id_Livro', models.CharField(max_length=100)),
            ],
        ),
    ]
