# Generated by Django 5.0.4 on 2024-04-21 23:07

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Autores',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_autor', models.CharField(max_length=255)),
                ('data_nascimento', models.DateField(blank=True, null=True)),
                ('data_falecimento', models.DateField(blank=True, null=True)),
                ('biografia', models.TextField(blank=True, null=True)),
                ('data_hora_insercao', models.DateTimeField(auto_now_add=True)),
                ('data_hora_atualizacao', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Editoras',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_editora', models.CharField(max_length=100)),
                ('cnpj', models.CharField(blank=True, max_length=14, null=True, unique=True)),
                ('data_hora_insercao', models.DateTimeField(auto_now_add=True)),
                ('data_hora_atualizacao', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Generos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_genero', models.CharField(max_length=100)),
                ('data_hora_insercao', models.DateTimeField(auto_now_add=True)),
                ('data_hora_atualizacao', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Livros',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=255)),
                ('slug', models.SlugField()),
                ('capa', models.ImageField(blank=True, default='', upload_to='livros/capas/%Y/%m/%d')),
                ('resumo', models.TextField(blank=True, null=True)),
                ('isbn', models.CharField(max_length=13, unique=True)),
                ('data_publicacao', models.DateField(blank=True, null=True)),
                ('data_hora_insercao', models.DateTimeField(auto_now_add=True)),
                ('data_hora_atualizacao', models.DateTimeField(auto_now=True)),
                ('autor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='acervo.autores')),
                ('editora', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='acervo.editoras')),
                ('genero', models.ManyToManyField(to='acervo.generos')),
            ],
        ),
        migrations.CreateModel(
            name='AcervoLivrosUsuarios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('livro_lido', models.BooleanField()),
                ('livro_favorito', models.BooleanField()),
                ('data_hora_insercao', models.DateTimeField(auto_now_add=True)),
                ('data_hora_atualizacao', models.DateTimeField(auto_now=True)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('livro', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='acervo.livros')),
            ],
        ),
    ]