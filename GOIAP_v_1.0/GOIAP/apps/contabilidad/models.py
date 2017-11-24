from django.db import models
from django.db.models.signals import pre_delete, post_delete
from django.dispatch import receiver
from django.conf import settings
import os
from apps.empleado.models import EmpleadoUser

# Create your models here.
class Nomina(models.Model):
	dias_laborados = models.IntegerField()
	basico = models.CharField(max_length=50)
	bonificaciones = models.CharField(max_length=50)
	nro_horas_diurnas = models.IntegerField()
	nro_horas_nocturnas = models.IntegerField()
	nro_horas_dominicales = models.IntegerField()
	valor_horas_diurnas = models.CharField(max_length=50)
	valor_horas_nocturnas = models.CharField(max_length=50)
	valor_horas_dominicales = models.CharField(max_length=50)
	aux_transporte = models.CharField(max_length=50)
	aux_alimentacion = models.CharField(max_length=50)
	aporte_salud = models.CharField(max_length=50)
	aporte_pension = models.CharField(max_length=50)
	retencion_fuente = models.CharField(max_length=50)
	total_devengado = models.CharField(max_length=50)
	total_deducciones = models.CharField(max_length=50)
	neto_pagar = models.CharField(max_length=50)
	archivo = models.FileField(upload_to='contabilidad/Documentos/')
	fecha = models.DateField()
	fk_empleado = models.ForeignKey(EmpleadoUser, null=True, blank=True, on_delete=models.CASCADE)

@receiver(pre_delete, sender=Nomina)
def _directorios_deleteNomina(sender, instance, using, **kwargs):
	file_path = settings.MEDIA_ROOT +'/'+ str(instance.archivo)
	print(file_path)
	if os.path.isfile(file_path):
		os.remove(file_path)

class Cuenta_cobro(models.Model):
	pagador = models.CharField(max_length=50)
	documento_pagador = models.CharField(max_length=50)
	neto_pagar = models.CharField(max_length=50)
	neto_pagar_letra = models.CharField(max_length=100)
	fecha = models.DateField()
	concepto = models.CharField(max_length=50)
	retenciones = models.CharField(max_length=50)
	fk_empleado = models.ForeignKey(EmpleadoUser, null=True, blank=True, on_delete=models.CASCADE)