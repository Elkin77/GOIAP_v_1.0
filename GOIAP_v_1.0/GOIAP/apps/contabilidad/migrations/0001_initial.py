# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-23 04:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('empleado', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cuenta_cobro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pagador', models.CharField(max_length=50)),
                ('documento_pagador', models.CharField(max_length=50)),
                ('neto_pagar', models.CharField(max_length=50)),
                ('neto_pagar_letra', models.CharField(max_length=100)),
                ('fecha', models.DateField()),
                ('concepto', models.CharField(max_length=50)),
                ('retenciones', models.CharField(max_length=50)),
                ('fk_empleado', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='empleado.EmpleadoUser')),
            ],
        ),
        migrations.CreateModel(
            name='Nomina',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dias_laborados', models.IntegerField()),
                ('basico', models.CharField(max_length=50)),
                ('bonificaciones', models.CharField(max_length=50)),
                ('nro_horas_diurnas', models.IntegerField()),
                ('nro_horas_nocturnas', models.IntegerField()),
                ('nro_horas_dominicales', models.IntegerField()),
                ('valor_horas_diurnas', models.CharField(max_length=50)),
                ('valor_horas_nocturnas', models.CharField(max_length=50)),
                ('valor_horas_dominicales', models.CharField(max_length=50)),
                ('aux_transporte', models.CharField(max_length=50)),
                ('aux_alimentacion', models.CharField(max_length=50)),
                ('aporte_salud', models.CharField(max_length=50)),
                ('aporte_pension', models.CharField(max_length=50)),
                ('retencion_fuente', models.CharField(max_length=50)),
                ('total_devengado', models.CharField(max_length=50)),
                ('total_deducciones', models.CharField(max_length=50)),
                ('neto_pagar', models.CharField(max_length=50)),
                ('archivo', models.FileField(upload_to='contabilidad/Documentos/')),
                ('fecha', models.DateField()),
                ('fk_empleado', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='empleado.EmpleadoUser')),
            ],
        ),
    ]
