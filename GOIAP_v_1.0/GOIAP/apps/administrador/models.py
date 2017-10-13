from django.db import models

# Create your models here.

class Administrador(models.Model):
	telefono = models.CharField(max_length=50)
	permisos_documentos = models.BooleanField()
	permisos_facturas = models.BooleanField()
	permisos_inventarios = models.BooleanField()
	permisos_empleados = models.BooleanField()
	permisos_obras = models.BooleanField()