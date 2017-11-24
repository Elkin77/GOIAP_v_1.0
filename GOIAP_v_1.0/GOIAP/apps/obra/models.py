from django.db import models
from django.db.models.signals import pre_delete, post_delete
from django.dispatch import receiver
from django.conf import settings
import os
from apps.user.models import Perfil

# Create your models here.


class Obra (models.Model):
	nombre = models.CharField(max_length=50)
	direccion = models.CharField(max_length=50)
	tipo = models.CharField(max_length=50)
	estado = models.CharField(max_length=50)
	nroApartamentos = models.IntegerField()
	fechaInicio = models.DateField()
	fechaFin = models.DateField(null=True)
	imagen = models.FileField(null=True, upload_to='obra/Imagenes/')
	fk_administrador_id = models.ForeignKey(Perfil, null=True, blank=True, on_delete=models.CASCADE)

	def __str__(self):
		return self.nombre

@receiver(pre_delete, sender=Obra)
def _directorios_deleteObra(sender, instance, using, **kwargs):
	file_path = settings.MEDIA_ROOT +'/'+ str(instance.imagen)
	print(file_path)
	if os.path.isfile(file_path):
		os.remove(file_path)
