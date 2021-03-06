# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-23 04:06
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
            name='EmpleadoUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=45)),
                ('cargo', models.CharField(max_length=50)),
                ('documento', models.CharField(max_length=100)),
                ('salario', models.CharField(max_length=50)),
                ('fecha_ingreso', models.DateField()),
                ('telefono', models.CharField(max_length=50)),
                ('rh', models.CharField(max_length=45)),
                ('correo', models.CharField(max_length=50, null=True)),
                ('fk_obra', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='obra.Obra')),
            ],
        ),
    ]
