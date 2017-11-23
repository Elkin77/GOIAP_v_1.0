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
            name='Factura',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('empresa', models.CharField(max_length=50)),
                ('nit_empresa', models.CharField(max_length=50)),
                ('codigo_factura', models.CharField(max_length=50)),
                ('valor', models.CharField(max_length=50)),
                ('fecha', models.DateField()),
                ('descripcion', models.CharField(max_length=50)),
                ('imagen', models.FileField(upload_to='facturas/Imagenes/')),
                ('fk_obra', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='obra.Obra')),
            ],
        ),
    ]
