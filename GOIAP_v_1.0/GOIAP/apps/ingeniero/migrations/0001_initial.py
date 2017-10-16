# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-16 04:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '__first__'),
        ('obra', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ingeniero',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('telefono', models.CharField(max_length=50)),
                ('permisos_documentos', models.BooleanField()),
                ('permisos_facturas', models.BooleanField()),
                ('permisos_inventarios', models.BooleanField()),
                ('permisos_empleados', models.BooleanField()),
                ('permisos_obras', models.BooleanField()),
                ('fk_Perfil', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='user.Perfil')),
                ('fk_obra', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='obra.Obra')),
            ],
        ),
    ]
