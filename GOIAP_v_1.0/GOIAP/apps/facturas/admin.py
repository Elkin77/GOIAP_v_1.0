from django.contrib import admin

# Register your models here.

from apps.facturas.models import Factura
admin.site.register(Factura)
