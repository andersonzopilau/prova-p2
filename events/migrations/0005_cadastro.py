# Generated by Django 2.0.8 on 2018-10-10 03:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0004_auto_20180927_2125'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cadastro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=80)),
                ('idade', models.CharField(max_length=80)),
                ('nacionalidade', models.CharField(max_length=80)),
                ('pebom', models.CharField(max_length=80)),
                ('posicao', models.CharField(max_length=80)),
                ('sexo', models.CharField(choices=[('0', 'masculino'), ('1', 'feminino'), ('2', 'outro')], max_length=1)),
                ('raca', models.CharField(choices=[('0', 'afro'), ('1', 'branco'), ('2', 'pardo')], max_length=1)),
            ],
        ),
    ]