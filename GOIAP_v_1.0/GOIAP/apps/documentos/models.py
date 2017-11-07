from django.db import models
from apps.obra.models import Obra
from apps.user.models import Perfil
# Create your models here.


# tablas para la gestión de documentos
class Documento_arquitectura(models.Model):
	nombre = models.CharField(max_length=50)
	tipo_doc = models.CharField(max_length=50)
	fecha_carga = models.DateField()
	archivo = models.CharField(max_length=100)
	nro_paginas = models.IntegerField()
	estado = models.CharField(max_length=50)
	descripcion = models.CharField(max_length=300)
	observacion = models.CharField(max_length=300)
	fk_obra = models.ForeignKey(Obra, null=True, blank=True, on_delete=models.CASCADE)
	fk_arquitecto = models.ForeignKey(Perfil, null=True, blank=True, on_delete=models.CASCADE)


class Documento_ingenieria(models.Model):
	nombre = models.CharField(max_length=50)	
	tipo_doc = models.CharField(max_length=50)
	fecha_carga = models.DateField()
	archivo = models.CharField(max_length=100)
	nro_paginas = models.IntegerField()
	estado = models.CharField(max_length=50)
	descripcion = models.CharField(max_length=300)
	observacion = models.CharField(max_length=300)
	fk_obra = models.ForeignKey(Obra, null=True, blank=True, on_delete=models.CASCADE)
	fk_ingeniero = models.ForeignKey(Perfil, null=True, blank=True, on_delete=models.CASCADE)


class Documento_contable(models.Model):
	nombre = models.CharField(max_length=50)
	tipo_doc = models.CharField(max_length=50)
	fecha_carga = models.DateField()
	archivo = models.CharField(max_length=100)
	nro_paginas = models.IntegerField()
	estado = models.CharField(max_length=50)
	descripcion = models.CharField(max_length=300)
	observacion = models.CharField(max_length=300)
	fk_obra = models.ForeignKey(Obra, null=True, blank=True, on_delete=models.CASCADE)
	fk_contador = models.ForeignKey(Perfil, null=True, blank=True, on_delete=models.CASCADE)


class Reporte(models.Model):
	nombre = models.CharField(max_length=50)
	tipo_reporte = models.CharField(max_length=50)
	fecha_carga = models.DateField()
	imagen = models.CharField(max_length=100)
	horas_empleadas = models.IntegerField()
	descripcion = models.CharField(max_length=300)
	observacion = models.CharField(max_length=300)
	fk_obra = models.ForeignKey(Obra, null=True, blank=True, on_delete=models.CASCADE)
	fk_empleado = models.ForeignKey(Perfil, null=True, blank=True, on_delete=models.CASCADE)	
