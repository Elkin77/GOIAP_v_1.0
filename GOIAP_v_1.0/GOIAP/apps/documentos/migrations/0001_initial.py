# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-23 04:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('obra', '0001_initial'),
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Documento_arquitectura',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('tipo_doc', models.CharField(max_length=50)),
                ('fecha_carga', models.DateField()),
                ('archivo', models.FileField(upload_to='documentos/DocumentoArquitectura/')),
                ('nro_paginas', models.IntegerField()),
                ('estado', models.CharField(max_length=50)),
                ('descripcion', models.CharField(max_length=300)),
                ('observacion', models.CharField(max_length=300)),
                ('fk_arquitecto', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='user.Perfil')),
                ('fk_obra', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='obra.Obra')),
            ],
        ),
        migrations.CreateModel(
            name='Documento_contable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('tipo_doc', models.CharField(max_length=50)),
                ('fecha_carga', models.DateField()),
                ('archivo', models.FileField(upload_to='documentos/DocumentoContable/')),
                ('nro_paginas', models.IntegerField()),
                ('estado', models.CharField(max_length=50)),
                ('descripcion', models.CharField(max_length=300)),
                ('observacion', models.CharField(max_length=300)),
                ('fk_contador', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='user.Perfil')),
                ('fk_obra', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='obra.Obra')),
            ],
        ),
        migrations.CreateModel(
            name='Documento_ingenieria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('tipo_doc', models.CharField(max_length=50)),
                ('fecha_carga', models.DateField()),
                ('archivo', models.FileField(upload_to='documentos/DocumentoIngenieria/')),
                ('nro_paginas', models.IntegerField()),
                ('estado', models.CharField(max_length=50)),
                ('descripcion', models.CharField(max_length=300)),
                ('observacion', models.CharField(max_length=300)),
                ('fk_ingeniero', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='user.Perfil')),
                ('fk_obra', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='obra.Obra')),
            ],
        ),
        migrations.CreateModel(
            name='Reporte',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('tipo_reporte', models.CharField(max_length=50)),
                ('fecha_carga', models.DateField()),
                ('imagen', models.FileField(upload_to='documentos/Reporte/Imagenes/')),
                ('horas_empleadas', models.IntegerField()),
                ('descripcion', models.CharField(max_length=300)),
                ('observacion', models.CharField(max_length=300)),
                ('fk_empleado', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='user.Perfil')),
                ('fk_obra', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='obra.Obra')),
            ],
        ),
    ]
