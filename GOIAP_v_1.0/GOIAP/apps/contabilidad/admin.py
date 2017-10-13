from django.contrib import admin

# Register your models here.


from apps.contabilidad.models import Nomina, Cuenta_cobro
admin.site.register(Nomina)
admin.site.register(Cuenta_cobro)
