from django.contrib import admin

# Register your models here.
from apps.contador.models import Contador
admin.site.register(Contador)