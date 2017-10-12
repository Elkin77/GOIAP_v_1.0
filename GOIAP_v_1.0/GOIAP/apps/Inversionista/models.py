from django.db import models
from apps.Obra.models import Obra

# Create your models here.
class Inversionista(models.Model):
	fk_obra= models.ForeignKey(Obra, null=True, blank=True, on_delete=models.CASCADE)
	telefono = models.CharField(max_length=50)
	permisos_documentos = models.BooleanField()
	permisos_facturas = models.BooleanField()
	permisos_inventarios = models.BooleanField()
	permisos_empleados = models.BooleanField()
	permisos_obras = models.BooleanField()
