from django.db import models
from django.db.models.signals import pre_delete, post_delete
from django.dispatch import receiver
from django.conf import settings
import os
from apps.obra.models import Obra

# Create your models here.


class Factura(models.Model):
	empresa = models.CharField(max_length=50)
	nit_empresa = models.CharField(max_length=50)
	codigo_factura = models.CharField(max_length=50)
	valor = models.CharField(max_length=50)
	fecha = models.DateField()
	descripcion = models.CharField(max_length=50)
	imagen = models.FileField(upload_to='facturas/Imagenes/')
	fk_obra = models.ForeignKey(Obra, null=True, blank=True, on_delete=models.CASCADE)

@receiver(pre_delete, sender=Factura)
def _directorios_deleteFactura(sender, instance, using, **kwargs):
	file_path = settings.MEDIA_ROOT +'/'+ str(instance.imagen)
	print(file_path)
	if os.path.isfile(file_path):
		os.remove(file_path)