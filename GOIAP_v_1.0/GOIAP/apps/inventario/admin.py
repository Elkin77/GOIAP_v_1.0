from django.contrib import admin

# Register your models here.


from apps.inventario.models import Inventario
admin.site.register(Inventario)
from apps.inventario.models import Contenido
admin.site.register(Contenido)