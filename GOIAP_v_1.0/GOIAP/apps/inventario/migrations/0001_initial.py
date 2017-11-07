# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-07 03:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('obra', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contenido',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('articulo', models.CharField(max_length=50)),
                ('cantidad', models.IntegerField()),
                ('valor', models.CharField(max_length=50)),
                ('tipo_articulo', models.CharField(max_length=50)),
                ('fecha_ingreso', models.DateField()),
                ('estado', models.CharField(max_length=50)),
                ('descripcion', models.CharField(max_length=300)),
                ('imagen', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Inventario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('tipo_inventario', models.CharField(max_length=50)),
                ('fecha_creacion', models.DateField()),
                ('estado', models.CharField(max_length=50)),
                ('descripcion', models.CharField(max_length=300)),
                ('nro_articulos', models.IntegerField()),
                ('fk_obra', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='obra.Obra')),
            ],
        ),
        migrations.AddField(
            model_name='contenido',
            name='fk_inventario',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='inventario.Inventario'),
        ),
    ]
