# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-13 16:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('administrador', '0001_initial'),
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
                ('fechaFin', models.DateField()),
                ('imagen', models.CharField(max_length=50)),
                ('fk_administrador', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='administrador.Administrador')),
            ],
        ),
    ]
