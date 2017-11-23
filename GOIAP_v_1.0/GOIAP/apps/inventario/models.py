from django.db import models

# Create your models here.

from apps.obra.models import Obra


# Create your models here.

class Inventario(models.Model):
	nombre = models.CharField(max_length=50)
	tipo_inventario = models.CharField(max_length=50)
	fecha_creacion = models.DateField()
	estado = models.CharField(max_length=50)
	descripcion = models.CharField(max_length=300)
	nro_articulos = models.IntegerField()
	fk_obra = models.ForeignKey(Obra, null=True, blank=True, on_delete=models.CASCADE)


class Contenido(models.Model):
	articulo = models.CharField(max_length=50)
	cantidad = models.IntegerField()
	valor = models.CharField(max_length=50)
	tipo_articulo = models.CharField(max_length=50)
	fecha_ingreso = models.DateField()
	estado = models.CharField(max_length=50)
	descripcion = models.CharField(max_length=300)
	imagen = models.FileField(upload_to='inventario/Imagenes/')
	fk_inventario = models.ForeignKey(Inventario, null=True, blank=True, on_delete=models.CASCADE)