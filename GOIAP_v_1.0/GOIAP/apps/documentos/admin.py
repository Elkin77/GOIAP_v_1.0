from django.contrib import admin

# Register your models here.
from apps.documentos.models import Documento_arquitectura, Documento_ingenieria, Documento_contable, Reporte
admin.site.register(Documento_arquitectura)
admin.site.register(Documento_ingenieria)
admin.site.register(Documento_contable)
admin.site.register(Reporte)
