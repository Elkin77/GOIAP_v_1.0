from django.db import models
from apps.Obra.models import Obra
from apps.Contador.models import Contador

# Create your models here.


class Factura(models.Model):
	fk_obra = models.ForeignKey(Obra, null=True, blank=True, on_delete=models.CASCADE)
	fk_contador = models.ForeignKey(Contador, null=True, blank=True, on_delete=models.CASCADE)
	empresa = models.CharField(max_length=50)
	nit_empresa = models.CharField(max_length=50)
	codigo_factura = models.CharField(max_length=50)
	valor = models.CharField(max_length=50)
	fecha = models.DateField()
	descripcion = models.CharField(max_length=50)
	imagen = models.CharField(max_length=50)