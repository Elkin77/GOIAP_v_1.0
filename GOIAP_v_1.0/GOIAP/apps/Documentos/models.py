from django.db import models
from apss.Obra.models import Obra
from apps.Arquitecto.models import Arquitecto
from apps.Ingeniero.models import Ingeniero
from apps.Contador.models import Contador
from apps.Empleado.models import Empleado
# Create your models here.


# tablas para la gestión de documentos
class Documento_arquitectura(models.Model):
	fk_obra = models.ForeignKey(Obra, null=True, blank=True, on_delete=models.CASCADE)
	fk_arquitecto = models.ForeignKey(Arquitecto, null=True, blank=True, on_delete=models.CASCADE)
	nombre = models.CharField(max_length=50)
	tipo_doc = models.CharField(max_length=50)
	fecha_carga = models.DateField()
	archivo = models.CharField(max_length=100)
	nro_paginas = models.IntegerField()
	estado = models.CharField(max_length=50)
	descripcion = models.CharField(max_length=300)
	observacion = models.CharField(max_length=300)


class Documento_ingenieria(models.Model):
	fk_obra = models.ForeignKey(Obra, null=True, blank=True, on_delete=models.CASCADE)
	fk_ingeniero = models.ForeignKey(Ingeniero, null=True, blank=True, on_delete=models.CASCADE)
	nombre = models.CharField(max_length=50)	
	tipo_doc = models.CharField(max_length=50)
	fecha_carga = models.DateField()
	archivo = models.CharField(max_length=100)
	nro_paginas = models.IntegerField()
	estado = models.CharField(max_length=50)
	descripcion = models.CharField(max_length=300)
	observacion = models.CharField(max_length=300)


class Documento_contable(models.Model):
	fk_obra = models.ForeignKey(Obra, null=True, blank=True, on_delete=models.CASCADE)
	fk_contador = models.ForeignKey(Contador, null=True, blank=True, on_delete=models.CASCADE)
	nombre = models.CharField(max_length=50)
	tipo_doc = models.CharField(max_length=50)
	fecha_carga = models.DateField()
	archivo = models.CharField(max_length=100)
	nro_paginas = models.IntegerField()
	estado = models.CharField(max_length=50)
	descripcion = models.CharField(max_length=300)
	observacion = models.CharField(max_length=300)


class Reporte(models.Model):
	fk_obra = models.ForeignKey(Obra, null=True, blank=True, on_delete=models.CASCADE)
	fk_empleado = models.ForeignKey(Empleado, null=True, blank=True, on_delete=models.CASCADE)	
	nombre = models.CharField(max_length=50)
	tipo_reporte = models.CharField(max_length=50)
	fecha_carga = models.DateField()
	imagen = models.CharField(max_length=100)
	horas_empleadas = models.IntegerField()
	descripcion = models.CharField(max_length=300)
	observacion = models.CharField(max_length=300)
