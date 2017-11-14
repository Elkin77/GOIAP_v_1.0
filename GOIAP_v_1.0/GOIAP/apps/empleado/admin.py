from django.contrib import admin

# Register your models here.
from apps.empleado.models import EmpleadoUser
admin.site.register(EmpleadoUser)