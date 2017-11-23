# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-22 20:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documentos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documento_arquitectura',
            name='archivo',
            field=models.FileField(upload_to='documentos/DocumentoArquitectura/'),
        ),
        migrations.AlterField(
            model_name='documento_contable',
            name='archivo',
            field=models.FileField(upload_to='documentos/DocumentoContable/'),
        ),
        migrations.AlterField(
            model_name='documento_ingenieria',
            name='archivo',
            field=models.FileField(upload_to='documentos/DocumentoIngenieria/'),
        ),
        migrations.AlterField(
            model_name='reporte',
            name='imagen',
            field=models.FileField(upload_to='documentos/Reporte/Imagenes/'),
        ),
    ]
