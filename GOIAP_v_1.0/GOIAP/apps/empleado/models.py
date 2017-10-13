from django.db import models
from apps.obra.models import Obra
# Create your models here.


class Empleado(models.Model):
	cargo = models.CharField(max_length=50)
	documento = models.CharField(max_length=100)
	salario = models.CharField(max_length=50)
	fecha_ingreso = models.DateField()
	telefono = models.CharField(max_length=50)
	rh = models.CharField(max_length=45)
	permisos_documentos = models.BooleanField()
	permisos_facturas = models.BooleanField()
	permisos_inventarios = models.BooleanField()
	permisos_empleados = models.BooleanField()
	permisos_obras = models.BooleanField()
	fk_obra = models.ForeignKey(Obra, null=True, blank=True, on_delete=models.CASCADE)