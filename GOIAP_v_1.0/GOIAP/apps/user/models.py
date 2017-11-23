from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Perfil(models.Model):
    rol=models.CharField(max_length=100)
    fk_authUser = models.OneToOneField(User, on_delete=models.CASCADE)
    

class Asignaciones(models.Model):
	perfil = models.ForeignKey(Perfil, null=True, blank=True, on_delete=models.CASCADE)
	fecha_solicitud = models.DateField()
	id_obra = models.IntegerField()
	descripcion = models.CharField(null=True, max_length=300)