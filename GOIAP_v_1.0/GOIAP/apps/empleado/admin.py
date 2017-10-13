from django.contrib import admin

# Register your models here.
from apps.empleado.models import Empleado
admin.site.register(Empleado)