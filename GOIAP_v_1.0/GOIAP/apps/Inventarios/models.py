from django.db import models
from apps.Obra.models import Obra
from apps.Arquitecto.models import Arquitecto
from apps.Inventario.models import Inventario

# Create your models here.

class Inventario(models.Model):
	fk_obra = models.ForeignKey(Obra, null=True, blank=True, on_delete=models.CASCADE)
	fk_arquitecto = models.ForeignKey(Arquitecto, null=True, blank=True, on_delete=models.CASCADE)
	nombre = models.CharField(max_length=50)
	tipo_inventario = models.CharField(max_length=50)
	fecha_creacion = models.DateField()
	estado = models.CharField(max_length=50)
	descripcion = models.CharField(max_length=300)
	nro_articulos = models.IntegerField()


class Contenido(models.Model):
	fk_inventario = models.ForeignKey(Inventario, null=True, blank=True, on_delete=models.CASCADE)
	articulo = models.CharField(max_length=50)
	cantidad = models.IntegerField()
	valor = models.CharField(max_length=50)
	tipo_articulo = models.CharField(max_length=50)
	fecha_ingreso = models.DateField()
	estado = models.CharField(max_length=50)
	descripcion = models.CharField(max_length=300)
	imagen = models.CharField(max_length=100)