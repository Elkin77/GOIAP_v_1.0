# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-23 08:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documentos', '0002_auto_20171123_0756'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reporte',
            name='fecha_carga',
            field=models.DateField(null=True),
        ),
    ]
