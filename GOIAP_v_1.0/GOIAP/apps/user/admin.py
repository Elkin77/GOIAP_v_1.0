from django.contrib import admin


from apps.user.models import Perfil
admin.site.register(Perfil)

from apps.user.models import Asignaciones
admin.site.register(Asignaciones)