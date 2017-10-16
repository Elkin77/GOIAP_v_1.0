from django.db import models
from django.shortcuts import render_to_response
from apps.user.models import Perfil

# Create your models here.

class Administrador(models.Model):
	fk_Perfil = models.OneToOneField(Perfil, on_delete=models.CASCADE)
	telefono = models.CharField(max_length=50)
	permisos_documentos = models.BooleanField()
	permisos_facturas = models.BooleanField()
	permisos_inventarios = models.BooleanField()
	permisos_empleados = models.BooleanField()
	permisos_obras = models.BooleanField()