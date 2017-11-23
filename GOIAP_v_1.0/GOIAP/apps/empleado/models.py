from django.db import models
from apps.obra.models import Obra
from apps.user.models import Perfil
# Create your models here.


class EmpleadoUser(models.Model):
	nombre = models.CharField(max_length=45)
	cargo = models.CharField(max_length=50)
	documento = models.CharField(max_length=100)
	salario = models.CharField(max_length=50)
	fecha_ingreso = models.DateField()
	telefono = models.CharField(max_length=50)
	rh = models.CharField(max_length=45)
	correo=models.CharField(null=True,max_length=50)
	fk_obra = models.ForeignKey(Obra, null=True, blank=True, on_delete=models.CASCADE)