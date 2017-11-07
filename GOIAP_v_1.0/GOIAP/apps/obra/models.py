from django.db import models
from apps.user.models import Perfil

# Create your models here.


class Obra (models.Model):
	nombre = models.CharField(max_length=50)
	direccion = models.CharField(max_length=50)
	tipo = models.CharField(max_length=50)
	estado = models.CharField(max_length=50)
	nroApartamentos = models.IntegerField()
	fechaInicio = models.DateField()
	fechaFin = models.DateField()
	imagen = models.CharField(max_length=50)
	fk_administrador = models.ForeignKey(Perfil, null=True, blank=True, on_delete=models.CASCADE)