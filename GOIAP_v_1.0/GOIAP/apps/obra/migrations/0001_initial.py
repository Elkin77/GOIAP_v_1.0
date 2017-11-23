# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-23 04:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Obra',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('direccion', models.CharField(max_length=50)),
                ('tipo', models.CharField(max_length=50)),
                ('estado', models.CharField(max_length=50)),
                ('nroApartamentos', models.IntegerField()),
                ('fechaInicio', models.DateField()),
                ('fechaFin', models.DateField(null=True)),
                ('imagen', models.FileField(null=True, upload_to='obra/Imagenes/')),
                ('fk_administrador_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='user.Perfil')),
            ],
        ),
    ]
