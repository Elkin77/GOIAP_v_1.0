from django.db import models
from apps.obra.models import Obra

# Create your models here.


class Factura(models.Model):
	empresa = models.CharField(max_length=50)
	nit_empresa = models.CharField(max_length=50)
	codigo_factura = models.CharField(max_length=50)
	valor = models.CharField(max_length=50)
	fecha = models.DateField()
	descripcion = models.CharField(max_length=50)
	imagen = models.CharField(max_length=50)
	fk_obra = models.ForeignKey(Obra, null=True, blank=True, on_delete=models.CASCADE)